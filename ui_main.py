# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\barankrky\CodingWorkspace\fakeNameGenerator\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(396, 124)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 71, 31))
        self.label.setObjectName("label")
        self.fakeNameOutput = QtWidgets.QLineEdit(self.centralwidget)
        self.fakeNameOutput.setGeometry(QtCore.QRect(110, 20, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.fakeNameOutput.setFont(font)
        self.fakeNameOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.fakeNameOutput.setReadOnly(True)
        self.fakeNameOutput.setObjectName("fakeNameOutput")
        self.generateButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.generateButton.setGeometry(QtCore.QRect(150, 60, 111, 41))
        self.generateButton.setObjectName("generateButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Fake  Name :"))
        self.fakeNameOutput.setText(_translate("MainWindow", "Generated Fake Name"))
        self.generateButton.setText(_translate("MainWindow", "Generate"))
