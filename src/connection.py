import paramiko

from config import Config


class SSHClient:
    client = None

    def __init__(self):
        self.get_connection()

    def get_connection(self):
        cfg = Config()

        user = cfg.machine['username']
        host = cfg.machine['address']
        port = cfg.machine['port']

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
            hostname=host,
            port=port,
            username=user,
            key_filename=cfg.ssh_key['path'],
            passphrase=cfg.ssh_key['password']
        )

        self.client = ssh

    def test_connection(self):
        stdin, stdout, stderr = self.client.exec_command('cat /etc/os-release')
        return stdout.readline().strip()


def test_connection():
    ssh = SSHClient()
    out = ssh.test_connection()
    assert out == 'NAME="Ubuntu"'
