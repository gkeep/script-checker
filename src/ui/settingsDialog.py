# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsWindowpoyvZO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_settingsDialog(object):
    def setupUi(self, settingsDialog):
        if not settingsDialog.objectName():
            settingsDialog.setObjectName(u"settingsDialog")
        settingsDialog.resize(650, 520)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(settingsDialog.sizePolicy().hasHeightForWidth())
        settingsDialog.setSizePolicy(sizePolicy)
        settingsDialog.setMinimumSize(QSize(650, 520))
        settingsDialog.setMaximumSize(QSize(650, 520))
        self.verticalLayout = QVBoxLayout(settingsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(settingsDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.selectPrivateKeyButton = QPushButton(self.groupBox_3)
        self.selectPrivateKeyButton.setObjectName(u"selectPrivateKeyButton")

        self.horizontalLayout.addWidget(self.selectPrivateKeyButton)

        self.privateKeyInputBox = QLineEdit(self.groupBox_3)
        self.privateKeyInputBox.setObjectName(u"privateKeyInputBox")

        self.horizontalLayout.addWidget(self.privateKeyInputBox)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.copyPublicKeyButton = QPushButton(self.groupBox)
        self.copyPublicKeyButton.setObjectName(u"copyPublicKeyButton")

        self.verticalLayout_2.addWidget(self.copyPublicKeyButton)

        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.passwordInputBox = QLineEdit(self.groupBox_4)
        self.passwordInputBox.setObjectName(u"passwordInputBox")
        self.passwordInputBox.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.passwordInputBox)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.passwordWarning = QLabel(self.groupBox)
        self.passwordWarning.setObjectName(u"passwordWarning")
        palette = QPalette()
        brush = QBrush(QColor(224, 27, 36, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(190, 190, 190, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.passwordWarning.setPalette(palette)
        self.passwordWarning.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.passwordWarning)


        self.verticalLayout.addWidget(self.groupBox)

        self.machineSettingsCheckBox = QCheckBox(settingsDialog)
        self.machineSettingsCheckBox.setObjectName(u"machineSettingsCheckBox")

        self.verticalLayout.addWidget(self.machineSettingsCheckBox)

        self.machineSettingsGroupBox = QGroupBox(settingsDialog)
        self.machineSettingsGroupBox.setObjectName(u"machineSettingsGroupBox")
        self.machineSettingsGroupBox.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.machineSettingsGroupBox.sizePolicy().hasHeightForWidth())
        self.machineSettingsGroupBox.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.machineSettingsGroupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.machineUserGroupBox = QGroupBox(self.machineSettingsGroupBox)
        self.machineUserGroupBox.setObjectName(u"machineUserGroupBox")
        self.machineUserGroupBox.setEnabled(False)
        self.horizontalLayout_3 = QHBoxLayout(self.machineUserGroupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.usernameInputBox = QLineEdit(self.machineUserGroupBox)
        self.usernameInputBox.setObjectName(u"usernameInputBox")

        self.horizontalLayout_3.addWidget(self.usernameInputBox)


        self.verticalLayout_3.addWidget(self.machineUserGroupBox)

        self.machineGroupBox = QGroupBox(self.machineSettingsGroupBox)
        self.machineGroupBox.setObjectName(u"machineGroupBox")
        self.machineGroupBox.setEnabled(False)
        self.horizontalLayout_4 = QHBoxLayout(self.machineGroupBox)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.machineDomainInputBox = QLineEdit(self.machineGroupBox)
        self.machineDomainInputBox.setObjectName(u"machineDomainInputBox")

        self.horizontalLayout_4.addWidget(self.machineDomainInputBox)

        self.machinePortInputBox = QLineEdit(self.machineGroupBox)
        self.machinePortInputBox.setObjectName(u"machinePortInputBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.machinePortInputBox.sizePolicy().hasHeightForWidth())
        self.machinePortInputBox.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.machinePortInputBox)


        self.verticalLayout_3.addWidget(self.machineGroupBox)


        self.verticalLayout.addWidget(self.machineSettingsGroupBox)

        self.saveButton = QDialogButtonBox(settingsDialog)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.saveButton.setOrientation(Qt.Horizontal)
        self.saveButton.setStandardButtons(QDialogButtonBox.Save)
        self.saveButton.setCenterButtons(True)

        self.verticalLayout.addWidget(self.saveButton)


        self.retranslateUi(settingsDialog)
        self.saveButton.accepted.connect(settingsDialog.accept)
        self.saveButton.rejected.connect(settingsDialog.reject)

        QMetaObject.connectSlotsByName(settingsDialog)
    # setupUi

    def retranslateUi(self, settingsDialog):
        settingsDialog.setWindowTitle(QCoreApplication.translate("settingsDialog", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 script-checker", None))
        self.groupBox.setTitle(QCoreApplication.translate("settingsDialog", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 SSH \u043a\u043b\u044e\u0447\u0430", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("settingsDialog", u"\u041f\u0443\u0442\u044c \u043a \u043f\u0440\u0438\u0432\u0430\u0442\u043d\u043e\u043c\u0443 \u043a\u043b\u044e\u0447\u0443", None))
        self.selectPrivateKeyButton.setText(QCoreApplication.translate("settingsDialog", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.privateKeyInputBox.setPlaceholderText(QCoreApplication.translate("settingsDialog", u"~/.ssh/id_rsa", None))
        self.copyPublicKeyButton.setText(QCoreApplication.translate("settingsDialog", u"\u0421\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u0443\u0431\u043b\u0438\u0447\u043d\u044b\u0439 \u043a\u043b\u044e\u0447", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("settingsDialog", u"\u041f\u0430\u0440\u043e\u043b\u044c \u043a \u043f\u0440\u0438\u0432\u0430\u0442\u043d\u043e\u043c\u0443 \u043a\u043b\u044e\u0447\u0443", None))
        self.passwordInputBox.setPlaceholderText(QCoreApplication.translate("settingsDialog", u"\u0431\u0435\u0437 \u043f\u0430\u0440\u043e\u043b\u044f", None))
        self.passwordWarning.setText(QCoreApplication.translate("settingsDialog", u"\u041f\u0430\u0440\u043e\u043b\u044c \u0445\u0440\u0430\u043d\u0438\u0442\u0441\u044f \u0432 plaintext \u0444\u043e\u0440\u043c\u0430\u0442\u0435!!! \u041d\u0438\u043a\u043e\u043c\u0443 \u043d\u0435 \u043f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0439\u0442\u0435 \u0441\u0432\u043e\u0439 config.json!", None))
        self.machineSettingsCheckBox.setText(QCoreApplication.translate("settingsDialog", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f", None))
        self.machineSettingsGroupBox.setTitle(QCoreApplication.translate("settingsDialog", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u043a \u0432\u0438\u0440\u0442\u0443\u0430\u043b\u044c\u043d\u043e\u0439 \u043c\u0430\u0448\u0438\u043d\u0435", None))
        self.machineUserGroupBox.setTitle(QCoreApplication.translate("settingsDialog", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.usernameInputBox.setPlaceholderText(QCoreApplication.translate("settingsDialog", u"scriptchecker", None))
        self.machineGroupBox.setTitle(QCoreApplication.translate("settingsDialog", u"IP \u0438\u043b\u0438 \u0434\u043e\u043c\u0435\u043d\u043d\u043e\u0435 \u0438\u043c\u044f \u0432\u0438\u0440\u0442\u0443\u0430\u043b\u044c\u043d\u043e\u0439 \u043c\u0430\u0448\u0438\u043d\u044b", None))
#if QT_CONFIG(tooltip)
        self.machineDomainInputBox.setToolTip(QCoreApplication.translate("settingsDialog", u"<html><head/><body><pre style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'monospace'; background-color:#ffffff;\"><br/></pre></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.machineDomainInputBox.setPlaceholderText(QCoreApplication.translate("settingsDialog", u"ya.hr-link.ru", None))
        self.machinePortInputBox.setPlaceholderText(QCoreApplication.translate("settingsDialog", u"10058", None))
#if QT_CONFIG(accessibility)
        self.saveButton.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
    # retranslateUi

