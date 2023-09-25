import paramiko
from scp import SCPClient
import os.path

from config import Config
from localChecks import Checker


class SSHClient:
    client = None
    cfg = None

    def __init__(self, cfg: Config):
        self.cfg = cfg

    def connect(self, timeout: int = 3):
        user = self.cfg.machine['username']
        host = self.cfg.machine['address']
        port = self.cfg.machine['port']

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(
                hostname=host,
                port=port,
                username=user,
                key_filename=self.cfg.ssh_key['path'],
                passphrase=self.cfg.ssh_key['password'],
                timeout=timeout
            )
        except Exception as e:
            return f'Could not connect - {e}'

        self.client = ssh

    def test_connection(self):
        err = self.connect()
        if err: return err

        stdin, stdout, stderr = self.client.exec_command('cat /etc/os-release')
        return stdout.readline().strip()

    def put_file(self, file_path: str):
        err = self.connect()
        if err: return err

        scp = SCPClient(self.client.get_transport())

        abs_path = os.path.expanduser(file_path)
        scp.put(abs_path, remote_path="/tmp")

    def run_file(self, file_path: str):
        err = self.connect()
        if err: return err

        out = []

        def run_command(command: str):
            stdin, stdout, stderr = self.client.exec_command(command)
            _stdout, _stderr = list(), list()

            for line in stdout.readlines():
                if line != "\n":
                    _stdout.append(line)
            for line in stderr.readlines():
                if line != "\n":
                    _stderr.append(line)

            return _stdout + _stderr

        file_name = file_path.split("/")[-1]
        remote_file = "/tmp/" + file_name
        checker = Checker(file_path)

        out.append({
            "check_type": "setup",
            "command": f"chmod +x {remote_file}",
            "output": run_command(f"chmod +x '{remote_file}'")
        })
        out.append({
            "check_type": "test",
            "command": f"shellcheck {remote_file}",
            "output": run_command(f"shellcheck '{remote_file}'")
        })
        out.append({
            "check_type": "flags_check",
            "command": "наличие флагов docker и psql",
            "output": checker.check_for_flags(['-c'])
        })
        out.append({
            "check_type": "run",
            "command": f"bash -x {remote_file}",
            "output": run_command(f"bash -x '{remote_file}'")
        })

        return out


def test_connection():
    ssh = SSHClient(Config())
    out = ssh.test_connection()
    assert out == 'NAME="Ubuntu"'


def test_file_upload():
    file = "~/Desktop/scripts/ibs-undelete.sh"
    ssh = SSHClient(Config())
    ssh.put_file(file_path=file)


def test_run_file():
    file = "~/Desktop/scripts/ibs-undelete.sh"
    ssh = SSHClient(Config())
    ssh.run_file(file_path=file)
