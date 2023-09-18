import paramiko
from scp import SCPClient
import os.path

from config import Config


class SSHClient:
    client = None
    cfg = None

    def connect(self, timeout: int = 3):
        cfg = Config()

        user = cfg.machine['username']
        host = cfg.machine['address']
        port = cfg.machine['port']

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(
                hostname=host,
                port=port,
                username=user,
                key_filename=cfg.ssh_key['path'],
                passphrase=cfg.ssh_key['password'],
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

        out.append({
            "check_type": "setup",
            "command": "chmod +x",
            "output": run_command(f"chmod +x {remote_file}")
        })
        out.append({
            "check_type": "test",
            "command": "shellcheck",
            "output": run_command(f"shellcheck {remote_file}")
        })

        if out[1]['output'] == []:
            out.append({
                "check_type": "run",
                "command": "run",
                "output": run_command(f"bash -x {remote_file}")
            })

        return out


def test_connection():
    ssh = SSHClient()
    out = ssh.test_connection()
    assert out == 'NAME="Ubuntu"'


def test_file_upload():
    file = "~/Desktop/scripts/ibs-undelete.sh"
    ssh = SSHClient()
    ssh.put_file(file_path=file)


def test_run_file():
    file = "~/Desktop/scripts/ibs-undelete.sh"
    ssh = SSHClient()
    ssh.run_file(file_path=file)
