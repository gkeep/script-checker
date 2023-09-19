import json
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
        json_path = Path(__file__).parent.parent.absolute() / 'config.json'
        self.cfg_path = json_path
        self.load_config(json_path)

    def load_config(self, path):
        with open(path, 'r') as file:
            cfg = json.load(file)

        self.ssh_key = cfg["ssh_key"]
        self.machine = cfg["machine"]

    def save_config(self):
        new_cfg = dict()
        new_cfg["ssh_key"] = self.ssh_key
        new_cfg["machine"] = self.machine

        with open(self.cfg_path, 'w') as file:
            file.write(json.dumps(new_cfg, indent=2))
