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

    def connect(self, timeout: int = 1):
        """
        exit коды:
            1 - ошибка SSH ключа
            2 - таймаут
            3 - неизвестно
        """

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
        except AttributeError and ValueError:
            return [1, "ошибка SSH ключа"]
        except TimeoutError:
            return [2, "таймаут"]
        except Exception as e:
            return [3, e]

        self.client = ssh
        return 0

    def put_file(self, file_path: str):
        err = self.connect()
        if err: return err

        scp = SCPClient(self.client.get_transport())

        abs_path = os.path.expanduser(file_path)
        scp.put(abs_path, remote_path="/tmp")

    def run_file(self, file_path: str, postgres_container: str):
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

            return [_stdout, _stderr]

        file_name = file_path.split("/")[-1]
        remote_file = "/tmp/" + file_name
        checker = Checker(file_path)

        if postgres_container != "ekd-postgresql":
            run_command(f"sed -i s/ekd-postgresql/ekd-postgresql-65/g {remote_file}")

        out.append({
            "check_type": "setup",
            "command": f"chmod +x {remote_file}",
            "output": run_command(f"chmod +x '{remote_file}'")
        })
        out.append({
            "check_type": "check",
            "command": f"shellcheck {remote_file}",
            "output": run_command(f"shellcheck --severity warning '{remote_file}'")
        })
        out.append({
            "check_type": "flags_check",
            "command": "флаги psql",
            "output": checker.check_for_flags(['-c'])
        })
        out.append({
            "check_type": "flags_check",
            "command": "кириллица",
            "output": checker.check_for_cyrillic_letters()
        })
        out.append({
            "check_type": "run",
            "command": f"bash -x {remote_file}",
            "output": run_command(f"bash -x '{remote_file}'")
        })

        return out
