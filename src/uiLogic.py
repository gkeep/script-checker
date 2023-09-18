from PySide2.QtCore import QObject
from PySide2.QtWidgets import QFileDialog

from ui.mainWindow import Ui_MainWindow
from connection import SSHClient

class UI_Main(Ui_MainWindow):
    def __init__(self, MainWindow, ssh_client: SSHClient):
        super().setupUi(MainWindow)
        self.ssh_client = ssh_client

        # bind functions to buttons
        self.testConnectionButton.clicked.connect(self.__test_connection)
        self.selectScriptPushButton.clicked.connect(self.__launch_file_dialog)

    def __launch_file_dialog(self):
        path_to_file = ""

        try:
            path_to_file, _ = QFileDialog.getOpenFileName(caption="Выберите скрипт", dir="~", filter='Bash/Shell Скрипт(*.sh)')
            self.script_path = path_to_file
        except Exception as e:
            print(e)
        finally:
            self.currrentScriptLineEdit.setText(path_to_file)

    def __test_connection(self):
        output = self.ssh_client.test_connection()
        if output == 'NAME="Ubuntu"':
            self.testConnectionButton.setStyleSheet('background-color: green;')
            self.testConnectionButton.setText("Подключение успешно")
        else:
            self.testConnectionButton.setStyleSheet('background-color: red;')
            self.testConnectionButton.setText(f"Подключение не успешно: {output}")
