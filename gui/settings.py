# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/qt\settings.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

# Added by buildgui.py script to support pyinstaller
from src.pyinstaller_helper import PyInstallerHelper

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(706, 479)
        self.verticalLayout = QtWidgets.QVBoxLayout(SettingsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.editorGroupBox = QtWidgets.QGroupBox(SettingsDialog)
        self.editorGroupBox.setObjectName("editorGroupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.editorGroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.editorFormLayout = QtWidgets.QFormLayout()
        self.editorFormLayout.setObjectName("editorFormLayout")
        self.label_4 = QtWidgets.QLabel(self.editorGroupBox)
        self.label_4.setObjectName("label_4")
        self.editorFormLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.editorGroupBox)
        self.label_5.setObjectName("label_5")
        self.editorFormLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.externalCommandLineEdit = QtWidgets.QLineEdit(self.editorGroupBox)
        self.externalCommandLineEdit.setObjectName("externalCommandLineEdit")
        self.editorFormLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.externalCommandLineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.externalPathLineEdit = QtWidgets.QLineEdit(self.editorGroupBox)
        self.externalPathLineEdit.setObjectName("externalPathLineEdit")
        self.horizontalLayout.addWidget(self.externalPathLineEdit)
        self.externalPathBrowseButton = QtWidgets.QPushButton(self.editorGroupBox)
        self.externalPathBrowseButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.externalPathBrowseButton.setObjectName("externalPathBrowseButton")
        self.horizontalLayout.addWidget(self.externalPathBrowseButton)
        self.editorFormLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.editorFormLayout)
        self.verticalLayout.addWidget(self.editorGroupBox)
        self.terminalGroupBox = QtWidgets.QGroupBox(SettingsDialog)
        self.terminalGroupBox.setObjectName("terminalGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.terminalGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.terminalFormLayout = QtWidgets.QFormLayout()
        self.terminalFormLayout.setObjectName("terminalFormLayout")
        self.label = QtWidgets.QLabel(self.terminalGroupBox)
        self.label.setObjectName("label")
        self.terminalFormLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.newLineKeyEdit = QtWidgets.QLineEdit(self.terminalGroupBox)
        self.newLineKeyEdit.setObjectName("newLineKeyEdit")
        self.terminalFormLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.newLineKeyEdit)
        self.label_2 = QtWidgets.QLabel(self.terminalGroupBox)
        self.label_2.setObjectName("label_2")
        self.terminalFormLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.sendKeyEdit = QtWidgets.QLineEdit(self.terminalGroupBox)
        self.sendKeyEdit.setObjectName("sendKeyEdit")
        self.terminalFormLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sendKeyEdit)
        self.label_6 = QtWidgets.QLabel(self.terminalGroupBox)
        self.label_6.setObjectName("label_6")
        self.terminalFormLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabSpacesSpinBox = QtWidgets.QSpinBox(self.terminalGroupBox)
        self.tabSpacesSpinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.tabSpacesSpinBox.setMinimum(1)
        self.tabSpacesSpinBox.setMaximum(8)
        self.tabSpacesSpinBox.setObjectName("tabSpacesSpinBox")
        self.horizontalLayout_2.addWidget(self.tabSpacesSpinBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.terminalFormLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.terminalFormLayout)
        self.verticalLayout.addWidget(self.terminalGroupBox)
        self.groupBox = QtWidgets.QGroupBox(SettingsDialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.mpyCrossPathLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.mpyCrossPathLineEdit.setObjectName("mpyCrossPathLineEdit")
        self.horizontalLayout_3.addWidget(self.mpyCrossPathLineEdit)
        self.mpyPathBrowseButton = QtWidgets.QPushButton(self.groupBox)
        self.mpyPathBrowseButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.mpyPathBrowseButton.setObjectName("mpyPathBrowseButton")
        self.horizontalLayout_3.addWidget(self.mpyPathBrowseButton)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.formLayout)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(SettingsDialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.preferredPortLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.preferredPortLineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.preferredPortLineEdit.setObjectName("preferredPortLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.preferredPortLineEdit)
        self.verticalLayout_5.addLayout(self.formLayout_2)
        self.verticalLayout.addWidget(self.groupBox_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(SettingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SettingsDialog)
        self.buttonBox.accepted.connect(SettingsDialog.accept)
        self.buttonBox.rejected.connect(SettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "Settings"))
        self.editorGroupBox.setTitle(_translate("SettingsDialog", "Editor"))
        self.label_4.setText(_translate("SettingsDialog", "Path to external editor"))
        self.label_5.setText(_translate("SettingsDialog", "External editor arguments"))
        self.externalPathBrowseButton.setText(_translate("SettingsDialog", "..."))
        self.terminalGroupBox.setTitle(_translate("SettingsDialog", "Terminal"))
        self.label.setText(_translate("SettingsDialog", "New line key"))
        self.label_2.setText(_translate("SettingsDialog", "Send key"))
        self.label_6.setText(_translate("SettingsDialog", "Tab spaces"))
        self.groupBox.setTitle(_translate("SettingsDialog", "Compiler"))
        self.label_3.setText(_translate("SettingsDialog", "mpy-cross path"))
        self.mpyPathBrowseButton.setText(_translate("SettingsDialog", "..."))
        self.groupBox_2.setTitle(_translate("SettingsDialog", "Connection"))
        self.label_7.setText(_translate("SettingsDialog", "Preferred port"))

