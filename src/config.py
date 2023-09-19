import json
import os.path
import appdirs
from pathlib import Path


class Config:
    ssh_key = {
        "path": "",
        "password": ""
    }
    machine = {
        "username": "",
        "address": "",
        "port": ""
    }

    def __init__(self):
        json_path = DirManager().config_dir() / 'config.json'
        self.cfg_path = json_path
        self.load_config()

    def load_config(self):
        path = self.cfg_path
        if not os.path.exists(path):
            self.__create_empty_config()

        with open(path, 'r') as file:
            cfg = json.load(file)

        self.ssh_key = cfg["ssh_key"]
        self.machine = cfg["machine"]

    def save_config(self):
        new_cfg = {'ssh_key': {}, 'machine': {}}
        for key, value in self.ssh_key.items():
            if value != "":
                new_cfg['ssh_key'][key] = value
        for key, value in self.machine.items():
            if value != "":
                new_cfg['machine'][key] = value

        with open(self.cfg_path, 'w') as file:
            file.write(json.dumps(new_cfg, indent=2))

    def __create_empty_config(self):
        self.ssh_key['path'] = '/home/dev/.ssh/id_rsa'
        self.machine['username'] = 'scriptchecker'
        self.machine['address'] = 'ya.hr-link.ru'
        self.machine['port'] = '10058'

        self.save_config()


class DirManager:
    def __init__(self):
        author = "script-checker"
        app_name = "script-checker"

        self.config_directory = appdirs.user_config_dir(app_name, author)

        os.makedirs(self.config_directory, exist_ok=True)

    def config_dir(self) -> Path:
        return Path(self.config_directory)
