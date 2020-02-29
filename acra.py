# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acra.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import cv2
import os
import pydicom
import glob

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 50, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 61, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 240, 51, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 330, 51, 21))
        self.label_4.setObjectName("label_4")
        self.name = QtWidgets.QTextEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(30, 80, 141, 31))
        self.name.setObjectName("name")
        self.age = QtWidgets.QTextEdit(self.centralwidget)
        self.age.setGeometry(QtCore.QRect(30, 170, 141, 31))
        self.age.setObjectName("age")
        self.xid = QtWidgets.QTextEdit(self.centralwidget)
        self.xid.setGeometry(QtCore.QRect(30, 360, 141, 31))
        self.xid.setObjectName("xid")
        self.submitbut = QtWidgets.QPushButton(self.centralwidget)
        self.submitbut.setGeometry(QtCore.QRect(520, 460, 93, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.submitbut.setFont(font)
        self.submitbut.setObjectName("submitbut")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(480, 40, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.uploadbut = QtWidgets.QPushButton(self.centralwidget)
        self.uploadbut.setGeometry(QtCore.QRect(520, 130, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.uploadbut.setFont(font)
        self.uploadbut.setObjectName("uploadbut")
        self.imgdisp = QtWidgets.QLabel(self.centralwidget)
        self.imgdisp.setGeometry(QtCore.QRect(440, 180, 256, 256))
        self.imgdisp.setFrameShape(QtWidgets.QFrame.Box)
        self.imgdisp.setText("")
        self.imgdisp.setObjectName("imgdisp")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(500, 80, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gender = QtWidgets.QComboBox(self.centralwidget)
        self.gender.setGeometry(QtCore.QRect(30, 270, 141, 31))
        self.gender.setObjectName("gender")
        self.gender.addItem("")
        self.gender.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.mw = MainWindow

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Name:"))
        self.label_2.setText(_translate("MainWindow", "Age:"))
        self.label_3.setText(_translate("MainWindow", "Gender:"))
        self.label_4.setText(_translate("MainWindow", "X-id:"))
        self.submitbut.setText(_translate("MainWindow", "submit"))
        self.label_5.setText(_translate("MainWindow", "Upload Radiograph"))
        self.uploadbut.setText(_translate("MainWindow", "upload "))
        self.label_7.setText(_translate("MainWindow", "(JPEG or DICOM)"))
        self.gender.setItemText(0, _translate("MainWindow", "Male"))
        self.gender.setItemText(1, _translate("MainWindow", "Female"))
        self.submitbut.clicked.connect(self.submit)
        self.uploadbut.clicked.connect(self.upload)
        self.classifier = load_model('classifier3.h5')
        
    def upload(self):
        self.fname = QFileDialog.getOpenFileName(self.centralwidget, 'Open file', '',"Radiograph files (*.jpg *.jpeg *.dcm)")
        if self.fname:
            if(self.fname[0][-3:]=='jpg' or self.fname[0][-4:]=='jpeg'):
                self.imgdisp.setPixmap(QPixmap(self.fname[0]).scaled(256, 256, QtCore.Qt.KeepAspectRatio))
                img = image.load_img(self.fname[0], target_size=(64, 64))
            else:
                ds = pydicom.read_file(self.fname[0])
                img = ds.pixel_array
                cv2.imwrite(self.fname[0].replace('.dcm','.jpg'),img)
                self.imgdisp.setPixmap(QPixmap(self.fname[0].replace('.dcm','.jpg')).scaled(256, 256, QtCore.Qt.KeepAspectRatio))
                img = image.load_img(self.fname[0].replace('.dcm','.jpg'), target_size=(64, 64))
                
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            self.result = self.classifier.predict(x)
                
        
    def submit(self):
        self.window2 = QtWidgets.QMainWindow()
        ui = Ui_MainWindow2()
        ui.setupUi(self.window2, self)
        self.window2.show()
        self.mw.hide()
        

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow, parent):
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
        self.mw = MainWindow
        self.parent = parent

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
        if(self.parent.fname[0][-3:]=='jpg' or self.parent.fname[0][-4:]=='jpeg'):
                self.imgdisp.setPixmap(QPixmap(self.parent.fname[0]).scaled(256, 256, QtCore.Qt.KeepAspectRatio))
        else:
            ds = pydicom.read_file(self.parent.fname[0])
            img = ds.pixel_array
            cv2.imwrite(self.parent.fname[0].replace('.dcm','.jpg'),img)
            self.imgdisp.setPixmap(QPixmap(self.parent.fname[0].replace('.dcm','.jpg')).scaled(256, 256, QtCore.Qt.KeepAspectRatio))
    
        self.nextbut.setText(_translate("MainWindow", "New Patient"))
        self.backbut.setText(_translate("MainWindow", "Change Image"))
        
        def backscr():
            self.parent.mw.show()
            self.mw.hide()
        self.backbut.clicked.connect(backscr)
        
        def nextscr():
            self.parent.setupUi(self.parent.mw)
            self.parent.mw.show()
            self.mw.hide()
        self.nextbut.clicked.connect(nextscr)
        
        
        if(self.parent.result[0][0] == 0):
            self.label_1.setText(_translate("MainWindow", "Pneumonia Negetive"))
            self.label_2.setText(_translate("MainWindow", "(Pneumonia Not Found)"))
            self.label_1.setStyleSheet('color: green')
        else:
            self.label_1.setText(_translate("MainWindow", "Pneumonia Positive"))
            self.label_2.setText(_translate("MainWindow", "(Pneumonia Found)"))
            self.label_1.setStyleSheet('color: red')
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

