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
        self.load_config(json_path)

    def load_config(self, path):
        with open(path, 'r') as file:
            cfg = json.load(file)

        self.ssh_key = cfg["ssh_key"]
        self.machine = cfg["machine"]

if __name__ == "__main__":
    cfg = Config()
