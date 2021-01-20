# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editSupervisorScreen.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(487, 553)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 491, 71))
        self.frame.setStyleSheet("background-color: rgb(27, 29, 35);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_label_top_btns = QtWidgets.QFrame(self.frame)
        self.frame_label_top_btns.setGeometry(QtCore.QRect(0, 0, 641, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy)
        self.frame_label_top_btns.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_top_btns.setObjectName("frame_label_top_btns")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_icon_top_bar_2 = QtWidgets.QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar_2.setMaximumSize(QtCore.QSize(30, 30))
        self.frame_icon_top_bar_2.setStyleSheet("background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/cil-terminal.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_icon_top_bar_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_icon_top_bar_2.setObjectName("frame_icon_top_bar_2")
        self.label_2 = QtWidgets.QLabel(self.frame_icon_top_bar_2)
        self.label_2.setGeometry(QtCore.QRect(6, 5, 20, 21))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../Desktop App/icons/16x16/cil-home.png"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar_2)
        self.label_title_bar_top = QtWidgets.QLabel(self.frame_label_top_btns)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_title_bar_top.setFont(font)
        self.label_title_bar_top.setStyleSheet("background: transparent;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_title_bar_top.setObjectName("label_title_bar_top")
        self.horizontalLayout_10.addWidget(self.label_title_bar_top)
        self.btn_close = QtWidgets.QPushButton(self.frame)
        self.btn_close.setGeometry(QtCore.QRect(450, 0, 40, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setMinimumSize(QtCore.QSize(40, 0))
        self.btn_close.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_close.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_close.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/24x24/cil-x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon)
        self.btn_close.setObjectName("btn_close")
        self.btn_minimize = QtWidgets.QPushButton(self.frame)
        self.btn_minimize.setGeometry(QtCore.QRect(370, 0, 40, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy)
        self.btn_minimize.setMinimumSize(QtCore.QSize(40, 0))
        self.btn_minimize.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_minimize.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_minimize.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/24x24/cil-window-minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_minimize.setIcon(icon1)
        self.btn_minimize.setObjectName("btn_minimize")
        self.btn_maximize_restore = QtWidgets.QPushButton(self.frame)
        self.btn_maximize_restore.setGeometry(QtCore.QRect(410, 0, 40, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy)
        self.btn_maximize_restore.setMinimumSize(QtCore.QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet("QPushButton {    \n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_maximize_restore.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/24x24/cil-window-maximize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_maximize_restore.setIcon(icon2)
        self.btn_maximize_restore.setObjectName("btn_maximize_restore")
        self.frame_top_info = QtWidgets.QFrame(self.frame)
        self.frame_top_info.setGeometry(QtCore.QRect(-10, 50, 501, 23))
        self.frame_top_info.setMaximumSize(QtCore.QSize(16777215, 65))
        self.frame_top_info.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_info.setObjectName("frame_top_info")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_credits = QtWidgets.QLabel(self.centralwidget)
        self.label_credits.setGeometry(QtCore.QRect(0, 530, 491, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("background-color: rgb(39, 44, 54);\n"
"color: rgb(255, 255, 255);")
        self.label_credits.setObjectName("label_credits")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 70, 491, 461))
        self.frame_2.setStyleSheet("background-color: rgb(27, 29, 35);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.addSupervisor = QtWidgets.QPushButton(self.frame_2)
        self.addSupervisor.setGeometry(QtCore.QRect(100, 380, 161, 31))
        self.addSupervisor.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(255, 0, 0);\n"
"\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"\n"
"border-width: 2px;\n"
"\n"
"border-radius: 15px;\n"
"\n"
"padding: 4px;\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../Desktop App/icons/24x24/cil-plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addSupervisor.setIcon(icon3)
        self.addSupervisor.setIconSize(QtCore.QSize(16, 16))
        self.addSupervisor.setObjectName("addSupervisor")
        self.cancle = QtWidgets.QPushButton(self.frame_2)
        self.cancle.setGeometry(QtCore.QRect(290, 380, 81, 31))
        self.cancle.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(0, 170, 255);\n"
"\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"\n"
"border-width: 2px;\n"
"\n"
"border-radius: 15px;\n"
"\n"
"padding: 4px;\n"
"")
        self.cancle.setIcon(icon3)
        self.cancle.setIconSize(QtCore.QSize(16, 16))
        self.cancle.setObjectName("cancle")
        self.nameLineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.nameLineEdit.setGeometry(QtCore.QRect(210, 80, 181, 41))
        self.nameLineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.emailLineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.emailLineEdit.setGeometry(QtCore.QRect(210, 160, 181, 41))
        self.emailLineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.passwordLineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.passwordLineEdit.setGeometry(QtCore.QRect(210, 240, 181, 41))
        self.passwordLineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(90, 80, 51, 41))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(90, 160, 51, 41))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(90, 240, 81, 41))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(90, 310, 41, 41))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(250, 310, 91, 41))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(90, 20, 51, 41))
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.userID = QtWidgets.QLabel(self.frame_2)
        self.userID.setGeometry(QtCore.QRect(210, 20, 51, 41))
        self.userID.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.userID.setText("")
        self.userID.setObjectName("userID")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title_bar_top.setText(_translate("MainWindow", "Edit Supervisor Detail"))
        self.btn_close.setToolTip(_translate("MainWindow", "Close"))
        self.btn_minimize.setToolTip(_translate("MainWindow", "Minimize"))
        self.btn_maximize_restore.setToolTip(_translate("MainWindow", "Maximize"))
        self.label_credits.setText(_translate("MainWindow", "   Made By : Abdul Wajid"))
        self.addSupervisor.setText(_translate("MainWindow", "Edit Supervisor"))
        self.cancle.setText(_translate("MainWindow", "Cancle"))
        self.label_5.setText(_translate("MainWindow", "Name"))
        self.label_6.setText(_translate("MainWindow", "Email"))
        self.label_7.setText(_translate("MainWindow", "Password"))
        self.label_8.setText(_translate("MainWindow", "Role"))
        self.label_9.setText(_translate("MainWindow", "Supervisor"))
        self.label_10.setText(_translate("MainWindow", "ID"))
