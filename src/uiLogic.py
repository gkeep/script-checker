import os.path
import pyclip
from PySide2.QtCore import QRegExp
from PySide2.QtGui import QRegExpValidator

from PySide2.QtWidgets import QFileDialog, QDialog

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

        self.ssh_client.put_file(self.script_path)
        out = self.ssh_client.run_file(self.script_path)
        widget = QDialog()
        ScriptCheckWindow(widget, out)
        widget.show()
        widget.exec_()

    @staticmethod
    def __open_settings():
        widget = QDialog()
        SettingsDialog(widget)
        widget.show()
        widget.exec_()

    def __test_connection(self):
        output = self.ssh_client.test_connection()
        if output == 'NAME="Ubuntu"':
            self.testConnectionButton.setStyleSheet('background-color: green;')
            self.testConnectionButton.setText("Подключение успешно")
            return True
        self.testConnectionButton.setStyleSheet('background-color: red;')
        self.testConnectionButton.setText(f"Подключение не успешно: {output}")
        return False


class SettingsDialog(Ui_settingsDialog):
    def __init__(self, window):
        self.new_cfg = Config()
        super().setupUi(window)

        self.saveButton.clicked.connect(lambda: self.new_cfg.save_config())
        self.selectPrivateKeyButton.clicked.connect(lambda: self.__select_private_key())
        self.copyPublicKeyButton.clicked.connect(lambda: self.__copy_public_key())
        self.machinePortInputBox.setValidator(QRegExpValidator(QRegExp("\d+")))

        self.passwordInputBox.editingFinished.connect(
            lambda: self.__save_field(self.passwordInputBox.text(), 'ssh_key', 'password'))
        self.usernameInputBox.editingFinished.connect(
            lambda: self.__save_field(self.usernameInputBox.text(), 'machine', 'username'))
        self.machineDomainInputBox.editingFinished.connect(
            lambda: self.__save_field(self.machineDomainInputBox.text(), 'machine', 'address'))
        self.machinePortInputBox.editingFinished.connect(
            lambda: self.__save_field(self.machinePortInputBox.text(), 'machine', 'port'))

    def __save_field(self, value, section, field):
        match section:
            case 'machine':
                self.new_cfg.machine[field] = value
            case 'ssh_key':
                self.new_cfg.ssh_key[field] = value

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
                pyclip.copy(key)  # does not work in Wayland for some reason
                self.copyPublicKeyButton.setText("Публичный ключ скопирован!")
            except pyclip.base.ClipboardSetupException:
                self.copyPublicKeyButton.setText("Не удалось скопировать :(")


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
        self.outputView.clear()
        for check in self.data:
            if check["command"] == item:
                for line in check["output"]:
                    self.outputView.append(line.rstrip())
