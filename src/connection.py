import paramiko

from config import Config


def get_connection():
    cfg = Config()

    user = cfg.machine['username']
    host = cfg.machine['address']
    port = cfg.machine['port']

    print(f"Connecting to {user}@{host}:{port}...")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        hostname=host,
        port=port,
        username=user,
        key_filename=cfg.ssh_key['path'],
        passphrase=cfg.ssh_key['password']
    )

    stdin, stdout, stderr = ssh.exec_command('uname -a')
    print(stdout.read())


if __name__ == "__main__":
    get_connection()