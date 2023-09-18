from PySide2.QtWidgets import QFileDialog, QDialog

from ui.mainWindow import Ui_MainWindow
from ui.checksOutput import Ui_scriptCheckWindow
from connection import SSHClient

class UI_Main(Ui_MainWindow):
    def __init__(self, MainWindow, ssh_client: SSHClient):
        super().setupUi(MainWindow)
        self.ssh_client = ssh_client

        # bind functions to buttons
        self.testConnectionButton.clicked.connect(self.__test_connection)
        self.selectScriptPushButton.clicked.connect(self.__launch_file_dialog)
        self.startTestsPushButton.clicked.connect(self.__start_tests)

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

    def __test_connection(self):
        output = self.ssh_client.test_connection()
        if output == 'NAME="Ubuntu"':
            self.testConnectionButton.setStyleSheet('background-color: green;')
            self.testConnectionButton.setText("Подключение успешно")
            return True
        self.testConnectionButton.setStyleSheet('background-color: red;')
        self.testConnectionButton.setText(f"Подключение не успешно: {output}")
        return False


class ScriptCheckWindow(Ui_scriptCheckWindow):
    def __init__(self, window, cmd_data):
        self.setupUi(window)
        self.data = cmd_data

        for item in self.data:
            if item["check_type"] != "setup":
                self.checksList.addItem(f"{item['command']}")

        self.checksList.itemActivated.connect(self.list_show_output)
        self.checksList.setCurrentRow(0)

    def list_show_output(self):
        item = self.checksList.currentItem().text()
        self.outputView.clear()
        for check in self.data:
            if check["command"] == item:
                for line in check["output"]:
                    self.outputView.append(line.rstrip())
