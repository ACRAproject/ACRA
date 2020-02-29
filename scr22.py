# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acra2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(300, 370, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.nextbut = QtWidgets.QPushButton(self.centralwidget)
        self.nextbut.setGeometry(QtCore.QRect(609, 190, 111, 31))
        self.nextbut.setObjectName("nextbut")
        self.backbut = QtWidgets.QPushButton(self.centralwidget)
        self.backbut.setGeometry(QtCore.QRect(80, 190, 111, 31))
        self.backbut.setObjectName("backbut")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 410, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.imgdisp = QtWidgets.QLabel(self.centralwidget)
        self.imgdisp.setGeometry(QtCore.QRect(272, 80, 256, 256))
        self.imgdisp.setFrameShape(QtWidgets.QFrame.Box)
        self.imgdisp.setText("")
        self.imgdisp.setObjectName("imgdisp")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_1.setText(_translate("MainWindow", "Pneumonia Negetive"))
        self.nextbut.setText(_translate("MainWindow", "New Patient"))
        self.backbut.setText(_translate("MainWindow", "Change Image"))
        self.label_2.setText(_translate("MainWindow", "(Pneumonia Not Found)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

