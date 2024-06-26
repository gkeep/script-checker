import os.path
import pyclip

from PySide6.QtWidgets import QDialogButtonBox, QFileDialog, QDialog
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression

from ui.mainWindow import Ui_MainWindow
from ui.checksOutput import Ui_scriptCheckWindow
from ui.settingsDialog import Ui_settingsDialog
from connection import SSHClient
from config import Config


class UIMain(Ui_MainWindow):
    def __init__(self, MainWindow, ssh_client: SSHClient, conf: Config):
        super().setupUi(MainWindow)
        self.ssh_client = ssh_client
        self.conf = conf

        # bind functions to buttons
        self.testConnectionButton.clicked.connect(self.__test_connection)
        self.selectScriptPushButton.clicked.connect(self.__launch_file_dialog)
        self.startTestsPushButton.clicked.connect(self.__start_tests)
        self.settingsButton.clicked.connect(self.__open_settings)

    def __launch_file_dialog(self):
        path_to_file = ""

        try:
            path_to_file, _ = QFileDialog.getOpenFileName(caption="Выберите скрипт", dir="~",
                                                          filter='Bash/Shell Скрипт(*.sh)')
            self.script_path = path_to_file
        except Exception as e:
            print(e)
        finally:
            self.currrentScriptLineEdit.setText(path_to_file)

    def __start_tests(self):
        if self.__test_connection() is False:
            return

        postgres_container = "ekd-postgresql"
        match self.releaseComboBox.currentText():
            case '65':
                postgres_container = "ekd-postgresql-65"

        self.ssh_client.put_file(self.script_path)
        out = self.ssh_client.run_file(self.script_path, postgres_container)
        widget = QDialog()
        ScriptCheckWindow(widget, out)
        widget.show()
        widget.exec()

    def __open_settings(self):
        widget = QDialog()
        SettingsDialog(widget, self.conf)
        widget.show()
        widget.exec()

        self.conf.load_config()

    def __test_connection(self):
        output = self.ssh_client.connect()
        if output == 0:
            self.testConnectionButton.setStyleSheet('background-color: green;')
            self.testConnectionButton.setText("Подключение успешно")
            return True
        self.testConnectionButton.setStyleSheet('background-color: red;')
        self.testConnectionButton.setText(f"Подключение не успешно: код ошибки {output[0]} ({output[1]})")
        return False


class SettingsDialog(Ui_settingsDialog):
    def __init__(self, window, old_config: Config):
        self.conf = old_config
        self.new_cfg = Config()
        super().setupUi(window)

        self.privateKeyInputBox.setText(self.conf.ssh_key["path"])
        self.passwordInputBox.setText(self.conf.ssh_key["password"])
        self.machinePortInputBox.setText(self.conf.machine["port"])
        self.machineDomainInputBox.setText(self.conf.machine["address"])
        self.usernameInputBox.setText(self.conf.machine["username"])

        self.saveButton.clicked.connect(lambda: self.new_cfg.save_config())
        self.machineSettingsCheckBox.stateChanged.connect(lambda: self.__enable_machine_settings())
        self.selectPrivateKeyButton.clicked.connect(lambda: self.__select_private_key())
        self.copyPublicKeyButton.clicked.connect(lambda: self.__copy_public_key())
        self.machinePortInputBox.setValidator(QRegularExpressionValidator(QRegularExpression("\d+")))
        self.saveButton.button(QDialogButtonBox.Save).setText("Сохранить")

        self.passwordInputBox.editingFinished.connect(
            lambda: self.__save_field(self.passwordInputBox.text(), 'ssh_key', 'password'))
        self.usernameInputBox.editingFinished.connect(
            lambda: self.__save_field(self.usernameInputBox.text(), 'machine', 'username'))
        self.machineDomainInputBox.editingFinished.connect(
            lambda: self.__save_field(self.machineDomainInputBox.text(), 'machine', 'address'))
        self.machinePortInputBox.editingFinished.connect(
            lambda: self.__save_field(self.machinePortInputBox.text(), 'machine', 'port'))

    def __save_field(self, value, section, field):
        if value == "":
            return
        match section:
            case 'machine':
                self.new_cfg.machine[field] = value
            case 'ssh_key':
                self.new_cfg.ssh_key[field] = value

    def __enable_machine_settings(self):
        state = False
        if self.machineSettingsCheckBox.isChecked():
            state = True

        self.machineSettingsGroupBox.setEnabled(state)
        self.machineGroupBox.setEnabled(state)
        self.machineUserGroupBox.setEnabled(state)

    def __select_private_key(self):
        path_to_file = ""

        try:
            path_to_file, _ = QFileDialog.getOpenFileName(caption="Выберите приватный SSH ключ",
                                                          dir=os.path.expanduser("$HOME/.ssh"),
                                                          filter='Все файлы(*)')
            self.new_cfg.ssh_key["path"] = path_to_file
        except Exception as e:
            print(e)
        finally:
            self.privateKeyInputBox.setText(path_to_file)

    def __copy_public_key(self):
        with open(f"{self.new_cfg.ssh_key['path']}.pub") as file:
            key = file.readlines()
            try:
                pyclip.copy(key[0])  # requires wl-clipboard on wayland
                self.copyPublicKeyButton.setText("Публичный ключ скопирован!")
            except pyclip.base.ClipboardSetupException:
                self.copyPublicKeyButton.setText("Не удалось скопировать, wl-clipboard установлен?")


class ScriptCheckWindow(Ui_scriptCheckWindow):
    def __init__(self, window, cmd_data):
        self.setupUi(window)
        self.data = cmd_data
        self.groupBox.setTitle(cmd_data[0]['command'][14:])

        for item in self.data:
            if item["check_type"] != "setup":
                self.checksList.addItem(f"{item['command']}")

        self.checksList.itemClicked.connect(lambda: self.list_show_output())

    def list_show_output(self):
        item = self.checksList.currentItem().text()

        self.outputView.setStyleSheet('background-color: #ffffff')
        self.outputView.setStyleSheet("font-family: 'Monaco', 'Ubuntu Mono', 'Courier New', monospace;")
        self.outputView.clear()

        for check in self.data:
            if check["command"] == item:
                out = check["output"]
                if out == [[], []] or out == {}:
                    self.outputView.setStyleSheet('background-color: #f1fce0')
                else:
                    if check["check_type"] == 'flags_check':
                        self.outputView.setStyleSheet('background-color: #fce0e0')
                        data = out
                        for item in data.values():
                            self.outputView.append(f"Строка {item['line_index']}: {item['line']}{item['error']}")
                            self.outputView.append("")
                    elif check['check_type'] == 'check':
                        self.outputView.setStyleSheet('background-color: #fceee0')
                        for line in out[0]:
                            self.outputView.append(line.rstrip())
                    else:
                        if out[0]:
                            self.outputView.append("STDOUT:")
                            for line in out[0]:
                                self.outputView.append(line.rstrip())
                            self.outputView.append("--------------------------------")

                        if out[1]:
                            self.outputView.append("STDERR:")
                            for line in out[1]:
                                self.outputView.append(line.rstrip())
