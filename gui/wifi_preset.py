# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/qt/wifi_preset.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets



# Added by buildgui.py script to support pyinstaller
from src.helpers.pyinstaller_helper import PyInstallerHelper

class Ui_WiFiPresetDialog(object):
    def setupUi(self, WiFiPresetDialog):
        WiFiPresetDialog.setObjectName("WiFiPresetDialog")
        WiFiPresetDialog.resize(451, 420)
        self.verticalLayout = QtWidgets.QVBoxLayout(WiFiPresetDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.presetsListView = QtWidgets.QListView(WiFiPresetDialog)
        self.presetsListView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.presetsListView.setObjectName("presetsListView")
        self.verticalLayout.addWidget(self.presetsListView)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(WiFiPresetDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(70, 0))
        self.label_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.nameLineEdit = QtWidgets.QLineEdit(WiFiPresetDialog)
        self.nameLineEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.horizontalLayout.addWidget(self.nameLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(WiFiPresetDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(70, 0))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.ipLineEdit = QtWidgets.QLineEdit(WiFiPresetDialog)
        self.ipLineEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.ipLineEdit.setObjectName("ipLineEdit")
        self.horizontalLayout_3.addWidget(self.ipLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(WiFiPresetDialog)
        self.label_4.setMinimumSize(QtCore.QSize(70, 0))
        self.label_4.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.portSpinBox = QtWidgets.QSpinBox(WiFiPresetDialog)
        self.portSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.portSpinBox.setMaximum(65536)
        self.portSpinBox.setProperty("value", 0)
        self.portSpinBox.setObjectName("portSpinBox")
        self.horizontalLayout_4.addWidget(self.portSpinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(WiFiPresetDialog)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.passwordLineEdit = QtWidgets.QLineEdit(WiFiPresetDialog)
        self.passwordLineEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.horizontalLayout_6.addWidget(self.passwordLineEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.label_5 = QtWidgets.QLabel(WiFiPresetDialog)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.addButton = QtWidgets.QPushButton(WiFiPresetDialog)
        self.addButton.setObjectName("addButton")
        self.verticalLayout_3.addWidget(self.addButton)
        self.removeButton = QtWidgets.QPushButton(WiFiPresetDialog)
        self.removeButton.setObjectName("removeButton")
        self.verticalLayout_3.addWidget(self.removeButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(WiFiPresetDialog)
        QtCore.QMetaObject.connectSlotsByName(WiFiPresetDialog)

    def retranslateUi(self, WiFiPresetDialog):
        _translate = QtCore.QCoreApplication.translate
        WiFiPresetDialog.setWindowTitle(_translate("WiFiPresetDialog", "Presets"))
        self.label_2.setText(_translate("WiFiPresetDialog", "Name"))
        self.label_3.setText(_translate("WiFiPresetDialog", "IP adress"))
        self.label_4.setText(_translate("WiFiPresetDialog", "Port"))
        self.label.setText(_translate("WiFiPresetDialog", "Password"))
        self.label_5.setText(_translate("WiFiPresetDialog", "<html><head/><body><p><span style=\" color:#d50003;\">Warning: passwords are saved as plaintext</span></p></body></html>"))
        self.addButton.setText(_translate("WiFiPresetDialog", "Add"))
        self.removeButton.setText(_translate("WiFiPresetDialog", "Remove"))
