# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'runOutputsDcNNG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_scriptCheckWindow(object):
    def setupUi(self, scriptCheckWindow):
        if not scriptCheckWindow.objectName():
            scriptCheckWindow.setObjectName(u"scriptCheckWindow")
        scriptCheckWindow.resize(1293, 614)
        self.verticalLayout = QVBoxLayout(scriptCheckWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(scriptCheckWindow)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checksList = QListWidget(self.groupBox)
        self.checksList.setObjectName(u"checksList")
        self.checksList.setMaximumSize(QSize(250, 16777215))
        font = QFont()
        font.setPointSize(11)
        self.checksList.setFont(font)
        self.checksList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.horizontalLayout.addWidget(self.checksList)

        self.outputView = QTextEdit(self.groupBox)
        self.outputView.setObjectName(u"outputView")
        self.outputView.setLineWidth(0)
        self.outputView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.outputView.setUndoRedoEnabled(False)
        self.outputView.setLineWrapMode(QTextEdit.NoWrap)
        self.outputView.setReadOnly(True)

        self.horizontalLayout.addWidget(self.outputView)


        self.verticalLayout.addWidget(self.groupBox)

        self.buttonBox = QDialogButtonBox(scriptCheckWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(scriptCheckWindow)
        self.buttonBox.accepted.connect(scriptCheckWindow.accept)
        self.buttonBox.rejected.connect(scriptCheckWindow.reject)

        QMetaObject.connectSlotsByName(scriptCheckWindow)
    # setupUi

    def retranslateUi(self, scriptCheckWindow):
        scriptCheckWindow.setWindowTitle(QCoreApplication.translate("scriptCheckWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430 \u0441\u043a\u0440\u0438\u043f\u0442\u0430", None))
        self.groupBox.setTitle(QCoreApplication.translate("scriptCheckWindow", u"Script name", None))
    # retranslateUi

