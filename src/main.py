from config import Config
from connection import SSHClient
import sys
from PySide2.QtWidgets import QMainWindow, QApplication
from uiLogic import UIMain

if __name__ == '__main__':
    config = Config()
    ssh_client = SSHClient(config)

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    content = UIMain(MainWindow, ssh_client, config)

    MainWindow.show()
    sys.exit(app.exec_())
