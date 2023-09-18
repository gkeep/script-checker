from config import Config
from connection import SSHClient, SCPClient
import sys
from PySide2.QtWidgets import QMainWindow, QApplication
from uiLogic import UI_Main

if __name__ == '__main__':
    ssh_client = SSHClient()

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    content = UI_Main(MainWindow, ssh_client)

    MainWindow.show()
    sys.exit(app.exec_())