class Checker:
    def __init__(self, path):
        data = None
        with open(path, 'r', encoding='utf-8') as file:
            data = file.readlines()

        self.data = data

    def check_for_flags(self, flags: list) -> {}:
        out = {}
        for i in range(0, len(self.data)):
            line = self.data[i]
            if line.startswith('docker exec --user postgres ekd-postgresql psql') and any(flag not in line for flag in flags):
                out[i] = {
                    "line_index": i,
                    "line": line,
                    "error": f"!!! Нет флага(ов) {flags} в строке! Скрипт будет выполнен с ошибкой!!!"
                }

        return out
