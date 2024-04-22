# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindoweJRnHv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.10
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(600, 300))
        MainWindow.setMaximumSize(QSize(600, 300))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, 6)
        self.releaseLabel = QLabel(self.centralwidget)
        self.releaseLabel.setObjectName(u"releaseLabel")
        font = QFont()
        font.setPointSize(11)
        self.releaseLabel.setFont(font)

        self.verticalLayout_4.addWidget(self.releaseLabel)

        self.releaseComboBox = QComboBox(self.centralwidget)
        self.releaseComboBox.addItem("")
        self.releaseComboBox.addItem("")
        self.releaseComboBox.setObjectName(u"releaseComboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.releaseComboBox.sizePolicy().hasHeightForWidth())
        self.releaseComboBox.setSizePolicy(sizePolicy1)
        self.releaseComboBox.setMaximumSize(QSize(16777215, 30))
        self.releaseComboBox.setFont(font)

        self.verticalLayout_4.addWidget(self.releaseComboBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.settingsButton = QPushButton(self.centralwidget)
        self.settingsButton.setObjectName(u"settingsButton")
        sizePolicy1.setHeightForWidth(self.settingsButton.sizePolicy().hasHeightForWidth())
        self.settingsButton.setSizePolicy(sizePolicy1)
        self.settingsButton.setMaximumSize(QSize(50, 50))
        font1 = QFont()
        font1.setPointSize(22)
        self.settingsButton.setFont(font1)
        self.settingsButton.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.settingsButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.testConnectionButton = QPushButton(self.centralwidget)
        self.testConnectionButton.setObjectName(u"testConnectionButton")
        self.testConnectionButton.setFont(font)

        self.verticalLayout.addWidget(self.testConnectionButton)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(600, 100))
        self.groupBox.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, -1, 5, -1)
        self.selectScriptPushButton = QPushButton(self.groupBox)
        self.selectScriptPushButton.setObjectName(u"selectScriptPushButton")

        self.verticalLayout_2.addWidget(self.selectScriptPushButton)

        self.currrentScriptLineEdit = QLineEdit(self.groupBox)
        self.currrentScriptLineEdit.setObjectName(u"currrentScriptLineEdit")
        self.currrentScriptLineEdit.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.currrentScriptLineEdit.sizePolicy().hasHeightForWidth())
        self.currrentScriptLineEdit.setSizePolicy(sizePolicy2)
        self.currrentScriptLineEdit.setMaximumSize(QSize(16777215, 30))
        self.currrentScriptLineEdit.setEchoMode(QLineEdit.Normal)
        self.currrentScriptLineEdit.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.currrentScriptLineEdit)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout.addWidget(self.groupBox)

        self.startTestsPushButton = QPushButton(self.centralwidget)
        self.startTestsPushButton.setObjectName(u"startTestsPushButton")

        self.verticalLayout.addWidget(self.startTestsPushButton)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Script-checker", None))
        self.releaseLabel.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u043b\u0438\u0437", None))
        self.releaseComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"66+", None))
        self.releaseComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"65", None))

        self.settingsButton.setText(QCoreApplication.translate("MainWindow", u"\u2699\ufe0f", None))
        self.testConnectionButton.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0440\u0438\u043f\u0442", None))
        self.selectScriptPushButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0441\u043a\u0440\u0438\u043f\u0442", None))
        self.startTestsPushButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0443 \u0441\u043a\u0440\u0438\u043f\u0442\u0430", None))
    # retranslateUi

