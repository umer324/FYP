# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1057, 603)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1061, 601))
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
        self.frame_2.setGeometry(QtCore.QRect(20, 20, 1011, 561))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(120, 90, 771, 401))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(10, 10, 381, 381))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setGeometry(QtCore.QRect(150, 40, 151, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(50, 180, 111, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setGeometry(QtCore.QRect(110, 270, 151, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit.setGeometry(QtCore.QRect(50, 130, 261, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 210, 261, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.frame_4)
        self.commandLinkButton.setGeometry(QtCore.QRect(90, 340, 201, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.commandLinkButton.setIconSize(QtCore.QSize(0, 0))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(400, 140, 381, 51))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(400, 190, 261, 41))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(300, 20, 431, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 170, 127);\n"
"font: 25pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(870, 0, 141, 141))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../../Desktop App/icons/rightTop.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 141, 141))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("../../Desktop App/icons/leftTop.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(0, 420, 141, 141))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("../../Desktop App/icons/leftBottom.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(870, 420, 141, 141))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("../../Desktop App/icons/rightBottom.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SIGN IN"))
        self.label_2.setText(_translate("MainWindow", "User Name"))
        self.label_3.setText(_translate("MainWindow", "Password:"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.commandLinkButton.setText(_translate("MainWindow", "Forgot Password? Click Here."))
        self.label_4.setText(_translate("MainWindow", "Fill the \"User Name\" and \"Password\" to login"))
        self.label_5.setText(_translate("MainWindow", "as Admin/Supervisor/Inspector."))
        self.label_7.setText(_translate("MainWindow", "Real Time Inspection System"))
