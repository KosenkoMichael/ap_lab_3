# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_V2.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Weather")
        MainWindow.setFixedSize(461, 218)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 121, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("""
        QPushButton {
            background-color: rgb(219, 219, 219); 
            color: black;
            border-radius: 5%;
        }
        QPushButton:hover {
            background-color:gray;
            color:white;
            border: 1px solid black;
        }
    """)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 10, 121, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("""
        QPushButton {
            background-color: rgb(219, 219, 219); 
            color: black;
            border-radius: 5%;
        }
        QPushButton:hover {
            background-color:gray;
            color:white;
            border: 1px solid black;
        }
    """)

        self.select_pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.select_pushButton_2.setGeometry(QtCore.QRect(230, 71, 60, 20))
        self.select_pushButton_2.setObjectName("select_pushButton_2")
        self.select_pushButton_2.setStyleSheet("""
        QPushButton {
            background-color: rgb(219, 219, 219); 
            color: black;
            border-radius: 5%;
        }
        QPushButton:hover {
            background-color:gray;
            color:white;
            border: 1px solid black;
        }
    """)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 10, 121, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("""
        QPushButton {
            background-color: rgb(219, 219, 219); 
            color: black;
            border-radius: 5%;
        }
        QPushButton:hover {
            background-color:gray;
            color:white;
            border: 1px solid black;
        }
    """)

        self.select_pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.select_pushButton_3.setGeometry(QtCore.QRect(390, 71, 60, 20))
        self.select_pushButton_3.setObjectName("select_pushButton_3")
        self.select_pushButton_3.setStyleSheet("""
        QPushButton {
            background-color: rgb(219, 219, 219); 
            color: black;
            border-radius: 5%;
        }
        QPushButton:hover {
            background-color:gray;
            color:white;
            border: 1px solid black;
        }
    """)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 100, 121, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet("""
        QPushButton {
            background-color: rgb(219, 219, 219); 
            color: black;
            border-radius: 5%;
        }
        QPushButton:hover {
            background-color:gray;
            color:white;
            border: 1px solid black;
        }
    """)

        self.select_pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.select_pushButton_4.setGeometry(QtCore.QRect(390, 160, 60, 20))
        self.select_pushButton_4.setObjectName("select_pushButton_4")
        self.select_pushButton_4.setStyleSheet("""
        QPushButton {
            background-color: rgb(219, 219, 219); 
            color: black;
            border-radius: 5%;
        }
        QPushButton:hover {
            background-color:gray;
            color:white;
            border: 1px solid black;
        }
    """)

        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 100, 121, 51))
        self.textEdit.setObjectName("textEdit")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 160, 71, 21))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet("""
        QPushButton {
            background-color: rgb(219, 219, 219); 
            color: black;
            border-radius: 5%;
        }
        QPushButton:hover {
            background-color:gray;
            color:white;
            border: 1px solid black;
        }
    """)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(133, 90, 190, 100))
        self.label.setObjectName("label")
        self.label.setWordWrap(True)

        self.get_next = QtWidgets.QPushButton(self.centralwidget)
        self.get_next.setGeometry(QtCore.QRect(200, 170, 71, 21))
        self.get_next.setObjectName("get_text")
        self.get_next.setStyleSheet("""
        QPushButton {
            background-color: rgb(219, 219, 219); 
            color: black;
            border-radius: 5%;
        }
        QPushButton:hover {
            background-color:gray;
            color:white;
            border: 1px solid black;
        }
    """)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 461, 21))
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
        self.pushButton.setText(_translate("MainWindow", "Select main file"))

        self.select_pushButton_2.setText(
            _translate("MainWindow", "add folder"))
        self.pushButton_2.setText(_translate("MainWindow", "Cut by data/date"))

        self.select_pushButton_3.setText(
            _translate("MainWindow", "add folder"))
        self.pushButton_3.setText(_translate("MainWindow", "Cut by years"))

        self.pushButton_4.setText(_translate("MainWindow", "cut by weaks"))
        self.select_pushButton_4.setText(
            _translate("MainWindow", "add folder"))

        self.pushButton_5.setText(_translate("MainWindow", "get data"))
        self.label.setText(_translate("MainWindow", ""))

        self.get_next.setText(_translate("MainWindow", "get_next"))
