# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtScreens/ui_changePassword.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1048, 618)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1051, 631))
        self.frame.setStyleSheet("*{\n"
"font-size:18px;}\n"
"#frame{\n"
"background:white;\n"
"\n"
"}\n"
"\n"
"#frame_2{\n"
"background: white;\n"
"border: 1px solid #01A794;\n"
"}\n"
"\n"
"#frame_3{\n"
"background:#01A794;\n"
"border: 1px solid #01A794;\n"
"border-radius:50px;\n"
"}\n"
"\n"
"#frame_4{\n"
"background:white;\n"
"border: 1px solid #01A794;\n"
"border-radius:50px;\n"
"}\n"
"\n"
"#label{\n"
"color:#01A794;\n"
"}\n"
"\n"
"#label_2{\n"
"color:#01A794;\n"
"}\n"
"\n"
"#label_3{\n"
"color:#01A794;\n"
"}\n"
"\n"
"#checkBox{\n"
"color:#01A794;\n"
"}\n"
"\n"
"\n"
"#commandLinkButton{\n"
"color:#01A794;\n"
"}\n"
"\n"
"\n"
"#pushButton{\n"
"background:#01A794;\n"
"border: 1px solid #01A794;\n"
"color:white;\n"
"}\n"
"\n"
"#lineEdit{\n"
"color:#01A794;\n"
"border: 1px solid #01A794;\n"
"}\n"
"\n"
"\n"
"#lineEdit_2{\n"
"color:#01A794;\n"
"border: 1px solid #01A794;\n"
"}\n"
"\n"
"#label_4{\n"
"color:white;\n"
"}\n"
"\n"
"#label_5{\n"
"color:white;\n"
"}\n"
" \n"
"#pushButton_2{\n"
"background:white;\n"
"border: 1px solid #01A794;\n"
"color:#01A794;\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(20, 20, 1011, 571))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(120, 90, 791, 411))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 391, 411))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setGeometry(QtCore.QRect(120, 40, 151, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 201, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit.setGeometry(QtCore.QRect(60, 130, 261, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 210, 261, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(50, 180, 221, 16))
        self.label_3.setObjectName("label_3")
        self.loginAgain = QtWidgets.QCommandLinkButton(self.frame_4)
        self.loginAgain.setGeometry(QtCore.QRect(50, 370, 291, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.loginAgain.setFont(font)
        self.loginAgain.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.loginAgain.setIconSize(QtCore.QSize(0, 0))
        self.loginAgain.setObjectName("loginAgain")
        self.sendOto = QtWidgets.QPushButton(self.frame_4)
        self.sendOto.setGeometry(QtCore.QRect(120, 260, 141, 31))
        self.sendOto.setStyleSheet("background-color: rgb(1, 167, 148);\n"
"color: rgb(255, 255, 255);")
        self.sendOto.setObjectName("sendOto")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(400, 140, 381, 51))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(400, 90, 381, 51))
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 141, 141))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("qtScreens\\../icons/leftTop.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(300, 0, 431, 71))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 170, 127);\n"
"font: 25pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(0, 430, 141, 141))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("qtScreens\\../icons/leftBottom.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(870, 0, 141, 141))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("qtScreens\\../icons/rightTop.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(870, 430, 141, 141))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("qtScreens\\../icons/rightBottom.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Change Password"))
        self.label_2.setText(_translate("MainWindow", "Enter the New Password"))
        self.label_3.setText(_translate("MainWindow", "Re-enter the New Password"))
        self.loginAgain.setText(_translate("MainWindow", "Remember The Password? Go To Login Screen"))
        self.sendOto.setText(_translate("MainWindow", "Send OTP"))
        self.label_4.setText(_translate("MainWindow", "Enter the same password in both text Fields."))
        self.label_5.setText(_translate("MainWindow", "Enter the New Password"))
        self.label_9.setText(_translate("MainWindow", "Real Time Inspection System"))
