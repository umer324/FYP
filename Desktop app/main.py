# Other Imports
import sys
import threading

import cv2
import numpy as np
import time
from threading import Thread


# Pyqt5 Imports
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QPropertyAnimation
from PyQt5.QtGui import QColor, QImage, QPixmap
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QApplication, QMessageBox, QFileDialog


# Architecture imports...
from graphs.pieChart import PieChartCanvas
from graphs.barChart import BarChartCanvas
from model.backendFunctions import *
from views import ui_login,ui_splashScreen, ui_forgetPassword ,ui_sendOtp, ui_changePassword, ui_adminHomeScreen , ui_addSupervisorScreen , ui_addInspectorScreen , ui_startInspectionScreen , ui_supervisorHomeScreen , ui_editSupervisorScreen , ui_editInspectorScreen
from controller.similarFunctionality import *



from SentOTP import *


counter = 0
userProfile = None

AllUsers = None

NoOfSupervisor = 0
NoOfInspector = 0
NoOfAdmin = 1

packetsClassIdFront = []
packetsClassIdBack = []

userObjectToEdit = None


class SplashScreenApp(QtWidgets.QMainWindow, ui_splashScreen.Ui_SplashScreen):
    def __init__(self, parent=None):
        super(SplashScreenApp, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.dropShadowFrame.setGraphicsEffect(self.shadow)

        # QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)

        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # Initial Text
        self.label_description.setText(
            "<strong>WELCOME</strong> TO MY APPLICATION")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.label_description.setText(
            "<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000, lambda: self.label_description.setText(
            "<strong>LOADING</strong> USER INTERFACE"))

        self.show()

    def progress(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        self.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = LoginApp()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1

class LoginApp(QtWidgets.QMainWindow, ui_login.Ui_MainWindow):
    def __init__(self, parent=None):
        super(LoginApp, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.pushButton.clicked.connect(self.loginButtonClick)
        self.commandLinkButton.clicked.connect(self.forgetPasswordButtonClick)

    def forgetPasswordButtonClick(self):
        self.main = ForgetPasswordApp()
        self.main.show()
        self.close()

    def loginButtonClick(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("LOGIN ERROR")

        if self.lineEdit.text() == "":
            msg.setText('Please fill the Username Field')
            msg.exec_()

        elif self.lineEdit_2.text() == "":
            msg.setText('Please fill the Password Field')
            msg.exec_()

        else:
            global userProfile
            loginUser = loginFunction(self.lineEdit.text(),self.lineEdit_2.text())
            userProfile = loginUser['user']
            if loginUser == 0:
                msg.setText('INCORRECT USERNAME OR PASSWORD')
                msg.exec_()
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
            else:
                user = loginUser['user']
                if user['role'] == "admin":
                    self.main = AdminHomeScreenApp()
                    self.main.show()
                    self.close()
                elif user['role'] == "spervisor":
                    self.main = SupervisorHomeScreenApp()
                    self.main.show()
                    self.close()
                elif user['role'] == "inspector;":
                    self.main = SupervisorHomeScreenApp()
                    self.main.show()
                    self.close()

class ForgetPasswordApp(QtWidgets.QMainWindow, ui_forgetPassword.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ForgetPasswordApp, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.sendOto.clicked.connect(self.sendOTP)
        self.loginAgain.clicked.connect(self.goBackToLoginScreen)

    def goBackToLoginScreen(self):
        self.main = LoginApp()
        self.main.show()
        self.close()

    def sendOTP(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("FORGET PASSWORD")

        if self.lineEdit.text() == "":
            msg.setText('Please fill the Email Field')
            msg.exec_()

        else:
            answer = sendOTP(self.lineEdit.text())
            if answer == 0:
                msg.setText('In-Valid Email Address')
                msg.exec_()

            elif answer == 1:
                msg.setText('Something went wrong')
                msg.exec_()
            else:
                global OTP
                global USEREMAIL
                                                      #Save the OTP and UserEmail Here....

                OTP = answer
                USEREMAIL = self.lineEdit.text()
                print(OTP)

                self.main = SendOtpApp()
                self.main.show()
                self.close()

class SendOtpApp(QtWidgets.QMainWindow, ui_sendOtp.Ui_MainWindow):
    def __init__(self, parent=None):
        super(SendOtpApp, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.sendOto.clicked.connect(self.verifyOTP)

    def verifyOTP(self):

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("OTP ERROR")

        if self.lineEdit.text() == "":
            msg.setText('Please enter the OTP')
            msg.exec_()

        else:
            if self.lineEdit.text() == OTP:

                self.main = ChangePasswordApp()
                self.main.show()
                self.close()
            else:
                msg.setText('You enter the wrong OTP')
                msg.exec_()

class ChangePasswordApp(QtWidgets.QMainWindow, ui_changePassword.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ChangePasswordApp, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.sendOto.clicked.connect(self.changePassword)
        self.loginAgain.clicked.connect(self.goBackToLoginScreen)

    def goBackToLoginScreen(self):
        self.main = LoginApp()
        self.main.show()
        self.close()

    def changePassword(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("FORGET PASSWORD")

        if self.lineEdit.text() == "":
            msg.setText('Please fill the New Password Field')
            msg.exec_()

        elif self.lineEdit_2.text() == "":
            msg.setText('Please fill the Re-enter Password Field')
            msg.exec_()
        else:
            if self.lineEdit.text() == self.lineEdit_2.text():
                changePassword(USEREMAIL,self.lineEdit.text())          #Change the user password whose email is this...
                self.main = LoginApp()
                self.main.show()
                self.close()
            else:
                msg.setText('New Password does not matach with re-enter password!')
                msg.exec_()


class SupervisorHomeScreenApp(QtWidgets.QMainWindow, ui_supervisorHomeScreen.Ui_MainWindow):
    def __init__(self, parent=None):
        super(SupervisorHomeScreenApp, self).__init__(parent)
        stat()
        global userProfile
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.profileButton.setText(userProfile['name'])
        self.topUserName.setText("Welcome, "+userProfile['name'])
        self.homeButton.setIcon(QtGui.QIcon("views/icons/house.png"))
        self.homeButton.setIconSize(QtCore.QSize(30, 44))
        self.logoutButton.setIcon(QtGui.QIcon("views/icons/log-out.png"))
        self.logoutButton.setIconSize(QtCore.QSize(33, 44))
        self.statisticsButton.setIcon(QtGui.QIcon("views/icons/statistics.png"))
        self.statisticsButton.setIconSize(QtCore.QSize(33, 44))
        self.profileButtonOrignal.setIcon(QtGui.QIcon("views/icons/profile.png"))
        self.profileButtonOrignal.setIconSize(QtCore.QSize(33, 44))
        self.startInspection.setIcon(QtGui.QIcon("views/icons/inspection.png"))
        self.startInspection.setIconSize(QtCore.QSize(50, 50))
        self.showStatistics.setIcon(QtGui.QIcon("views/icons/statistics.png"))
        self.showStatistics.setIconSize(QtCore.QSize(50, 50))
        self.label_15.setPixmap(QtGui.QPixmap("views/icons/profile.png"))
        self.label_15.setScaledContents(True)
        self.btn_close.setIcon(QtGui.QIcon("views/icons/16x16/cil-x.png"))
        self.btn_close.setIconSize(QtCore.QSize(16 , 16))
        self.btn_maximize_restore.setIcon(QtGui.QIcon("views/icons/16x16/cil-window-maximize.png"))
        self.btn_maximize_restore.setIconSize(QtCore.QSize(16, 16))
        self.btn_minimize.setIcon(QtGui.QIcon("views/icons/16x16/cil-window-minimize.png"))
        self.btn_minimize.setIconSize(QtCore.QSize(16, 16))
        self.btn_toggle_menu_2.setIcon(QtGui.QIcon("views/icons/24x24/cil - menu.png.png"))
        self.btn_toggle_menu_2.setIconSize(QtCore.QSize(24,24))



        # Top Functionality...
        self.btn_close.clicked.connect(self.closeButtonClick)
        self.btn_minimize.clicked.connect(self.minimizeButtonClick)



        # Home Screen Page Number 1:
        self.homeButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageHome))
        self.startInspection.clicked.connect(self.startInspectionScreen)
        self.showStatistics.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageStatistics))


        # Statistics Screen Page Number 3:
        self.statisticsButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageStatistics))
        canvas = PieChartCanvas(self.pieChartFrame, width=4, height=2)
        # canvas1 = BarChartCanvas(self.barChartFrame , width=2 , height=2)
        self.loadInformationTableData()


        # User Profile Screen Page Number 4:
        self.profileButton.setText("Wajid")
        self.UserName.setText("Welcome, "+userProfile['name'])
        self.EmailID.setText("Email : "+userProfile['email'])
        self.ROLEID.setText("ROLE : "+userProfile['role'])
        self.profileButtonOrignal.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageProfile))


        # Logout Screen Page Number 5:
        self.logoutButton.clicked.connect(self.onLogoutButtonClick)




# Home Screen Button Functionality...

    def startInspectionScreen(self):
        self.main = StartInspectionApp()
        self.main.show()
        self.close()



# Statistics Button Functionality...

    def loadInformationTableData(self):
        global NoOfSupervisor
        global NoOfInspector
        global NoOfAdmin
        NofBatches , total_packets ,valid , invalid = stat(user_id=1)

        self.informationTableWdget.setColumnWidth(1, 20)
        self.informationTableWdget.setRowCount(6)
        self.informationTableWdget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(NoOfSupervisor)))
        self.informationTableWdget.setItem(1, 0, QtWidgets.QTableWidgetItem(str(NoOfInspector)))
        self.informationTableWdget.setItem(2, 0, QtWidgets.QTableWidgetItem(str(NoOfAdmin)))
        self.informationTableWdget.setItem(3, 0, QtWidgets.QTableWidgetItem(str(total_packets)))
        self.informationTableWdget.setItem(4, 0, QtWidgets.QTableWidgetItem(str(valid)))
        self.informationTableWdget.setItem(5, 0, QtWidgets.QTableWidgetItem(str(invalid)))


# logut Button Functionality...

    def onLogoutButtonClick(self):
        msg = QMessageBox()
        msg.setWindowTitle("Logout Button Click")
        msg.setText("Are you sure you want to Logout.")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)  # seperate buttons with "|"
        msg.setDefaultButton(QMessageBox.No)  # setting default button to Cancel
        x = msg.exec_()  # this will show our messagebox
        if x == 16384:
            self.main = LoginApp()
            self.main.show()
            self.close()

# Top functionality App
    def toggleMenu(self):
        maxWidth = 220
        enable = True
        if enable:
            # GET WIDTH
            width = self.frame_left_menu_2.width()
            maxExtend = maxWidth
            standard = 70
            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard
            # ANIMATION
            self.animation = QPropertyAnimation(self.frame_left_menu_2, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def maximizeButtonClick(self):
        print("Maximize Button Click")

    def minimizeButtonClick(self):
        self.showMinimized()

    def closeButtonClick(self):
        msg = QMessageBox()
        msg.setWindowTitle("Close Button")
        msg.setText("Are you sure you want to quit.")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)  # seperate buttons with "|"
        msg.setDefaultButton(QMessageBox.No)  # setting default button to Cancel
        x = msg.exec_()  # this will show our messagebox
        if x == 16384:
            self.close()


class AdminHomeScreenApp(QtWidgets.QMainWindow, ui_adminHomeScreen.Ui_MainWindow):
    def __init__(self, parent=None):
        super(AdminHomeScreenApp, self).__init__(parent)
        stat()
        global userProfile
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.profileButton.setText(userProfile['name'])
        self.topUserName.setText("Welcome, "+userProfile['name'])
        self.homeButton.setIcon(QtGui.QIcon("views/icons/house.png"))
        self.homeButton.setIconSize(QtCore.QSize(30, 44))
        self.logoutButton.setIcon(QtGui.QIcon("views/icons/log-out.png"))
        self.logoutButton.setIconSize(QtCore.QSize(33, 44))
        self.adminPanelButton.setIcon(QtGui.QIcon("views/icons/adminPanel.png"))
        self.adminPanelButton.setIconSize(QtCore.QSize(33, 44))
        self.statisticsButton.setIcon(QtGui.QIcon("views/icons/statistics.png"))
        self.statisticsButton.setIconSize(QtCore.QSize(33, 44))
        self.profileButtonOrignal.setIcon(QtGui.QIcon("views/icons/profile.png"))
        self.profileButtonOrignal.setIconSize(QtCore.QSize(33, 44))
        self.startInspection.setIcon(QtGui.QIcon("views/icons/inspection.png"))
        self.startInspection.setIconSize(QtCore.QSize(50, 50))
        self.showStatistics.setIcon(QtGui.QIcon("views/icons/statistics.png"))
        self.showStatistics.setIconSize(QtCore.QSize(50, 50))
        self.searchButton.setIcon(QtGui.QIcon("views/icons/search.png"))
        self.searchButton.setIconSize(QtCore.QSize(30, 30))
        self.label_7.setPixmap(QtGui.QPixmap("views/icons/supervisor.png"))
        self.label_7.setScaledContents(True)
        self.label_8.setPixmap(QtGui.QPixmap("views/icons/inspector.png"))
        self.label_8.setScaledContents(True)
        self.label_15.setPixmap(QtGui.QPixmap("views/icons/profile.png"))
        self.label_15.setScaledContents(True)
        self.btn_close.setIcon(QtGui.QIcon("views/icons/16x16/cil-x.png"))
        self.btn_close.setIconSize(QtCore.QSize(16 , 16))
        self.btn_maximize_restore.setIcon(QtGui.QIcon("views/icons/16x16/cil-window-maximize.png"))
        self.btn_maximize_restore.setIconSize(QtCore.QSize(16, 16))
        self.btn_minimize.setIcon(QtGui.QIcon("views/icons/16x16/cil-window-minimize.png"))
        self.btn_minimize.setIconSize(QtCore.QSize(16, 16))
        self.btn_toggle_menu_2.setIcon(QtGui.QIcon("views/icons/24x24/cil - menu.png.png"))
        self.btn_toggle_menu_2.setIconSize(QtCore.QSize(24,24))



        # Top Functionality...
        self.btn_close.clicked.connect(self.closeButtonClick)
        self.btn_minimize.clicked.connect(self.minimizeButtonClick)



        # Home Screen Page Number 1:
        self.homeButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageHome))
        self.startInspection.clicked.connect(self.startInspectionScreen)
        self.showStatistics.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageStatistics))

        # Admin Panel Screen Page Number 2:
        self.adminPanelButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageAdminPanel))
        self.addSupervisor.clicked.connect(self.addSupervisorButtonClick)
        self.addInspector.clicked.connect(self.addInspectorButtonClick)
        self.loadAllDataInTable()


        # Statistics Screen Page Number 3:
        self.statisticsButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageStatistics))
        canvas = PieChartCanvas(self.pieChartFrame, width=4, height=2)
        # canvas1 = BarChartCanvas(self.barChartFrame , width=2 , height=2)
        self.loadInformationTableData()


        # User Profile Screen Page Number 4:
        self.profileButton.setText("Wajid")
        self.UserName.setText("Welcome, "+userProfile['name'])
        self.EmailID.setText("Email : "+userProfile['email'])
        self.ROLEID.setText("ROLE : "+userProfile['role'])
        self.profileButtonOrignal.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageProfile))


        # Logout Screen Page Number 5:
        self.logoutButton.clicked.connect(self.onLogoutButtonClick)




# Home Screen Button Functionality...

    def startInspectionScreen(self):
        self.main = StartInspectionApp()
        self.main.show()
        self.close()


# Admin Panel Button Functionality...

    def addSupervisorButtonClick(self):
        self.main = AddSupervisorScreenApp()
        self.main.show()
        self.close()

    def addInspectorButtonClick(self):
        self.main = AddInspectorScreenApp()
        self.main.show()
        self.close()

    def loadAllDataInTable(self):
        global NoOfSupervisor
        global NoOfInspector
        global AllUsers
        self.supervisorTable.setColumnWidth(0, 220)
        self.supervisorTable.setColumnWidth(1, 50)
        self.supervisorTable.setColumnWidth(2, 50)
        self.inspectorTable.setColumnWidth(0, 220)
        self.inspectorTable.setColumnWidth(1, 50)
        self.inspectorTable.setColumnWidth(2, 50)

        result = getAllUsersDetail()
        AllUsers = result
        supervisorList = []
        inspectorList = []
        for data in result:
            if data['role'] == "inspector":
                inspectorList.append({"Name" : data['name']})

            elif data['role'] == "spervisor":
                supervisorList.append({"Name" : data['name']})


        row = 0
        NoOfSupervisor = len(supervisorList)
        NoOfInspector = len(inspectorList)
        self.supervisorTable.setRowCount(len(supervisorList))
        self.inspectorTable.setRowCount(len(inspectorList))

        for person in supervisorList:
            self.editButtonForSupervisor = QtWidgets.QPushButton("")
            self.editButtonForSupervisor.clicked.connect(self.editButtonForSupervisorClick)
            self.editButtonForSupervisor.setIcon(QtGui.QIcon("views/icons/edit.png"))
            self.deleteButtonForSupervisor = QtWidgets.QPushButton("")
            self.deleteButtonForSupervisor.clicked.connect(self.deleteButtonForSupervisorClick)
            self.deleteButtonForSupervisor.setIcon(QtGui.QIcon("views/icons/delete.png"))
            self.supervisorTable.setItem(row, 0, QtWidgets.QTableWidgetItem(person["Name"]))
            self.supervisorTable.setCellWidget(row, 1, self.editButtonForSupervisor)
            self.supervisorTable.setCellWidget(row, 2, self.deleteButtonForSupervisor)
            row = row + 1

        row = 0

        for person in inspectorList:
            self.editButtonForInspector = QtWidgets.QPushButton("")
            self.editButtonForInspector.clicked.connect(self.editButtonForInspectorClick)
            self.editButtonForInspector.setIcon(QtGui.QIcon("views/icons/edit.png"))
            self.deleteButtonForInspector = QtWidgets.QPushButton("")
            self.deleteButtonForInspector.clicked.connect(self.deleteButtonForInspectorClick)
            self.deleteButtonForInspector.setIcon(QtGui.QIcon("views/icons/delete.png"))
            self.inspectorTable.setItem(row, 0, QtWidgets.QTableWidgetItem(person["Name"]))
            self.inspectorTable.setCellWidget(row, 1, self.editButtonForInspector)
            self.inspectorTable.setCellWidget(row, 2, self.deleteButtonForInspector)

            row = row + 1

    def editButtonForSupervisorClick(self):
        global AllUsers
        global userObjectToEdit
        button = self.sender()
        index = self.supervisorTable.indexAt(button.pos())
        if index.isValid():
            objectToEdit = None
            for data in AllUsers:
                if data['role'] == 'spervisor':
                    if data['name'] == self.supervisorTable.item(index.row(), 0).text():
                        objectToEdit = data

            userObjectToEdit = objectToEdit
            self.main = EditSupervisorScreenApp()
            self.main.show()
            self.close()

    def deleteButtonForSupervisorClick(self):
        global AllUsers
        button = self.sender()
        index = self.supervisorTable.indexAt(button.pos())
        if index.isValid():
            msg = QMessageBox()
            msg.setWindowTitle("Delete Supervisor")
            msg.setText("Are you sure you want to delete "+self.supervisorTable.item(index.row(),0).text()+" Supervisor.")
            msg.setIcon(QMessageBox.Question)
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)  # seperate buttons with "|"
            msg.setDefaultButton(QMessageBox.No)  # setting default button to Cancel
            x = msg.exec_()  # this will show our messagebox
            if x == 16384:
                objectToDelete = None
                for data in AllUsers:
                    if data['role'] == 'spervisor':
                        if data['name'] == self.supervisorTable.item(index.row(),0).text():
                            objectToDelete = data

                deleteSuperVisor(objectToDelete['id'])
                self.main = AdminHomeScreenApp()
                self.main.show()
                self.close()


    def editButtonForInspectorClick(self):
        global AllUsers
        global userObjectToEdit
        button = self.sender()
        index = self.inspectorTable.indexAt(button.pos())
        if index.isValid():
            objectToEdit = None
            for data in AllUsers:
                if data['role'] == 'inspector':
                    if data['name'] == self.inspectorTable.item(index.row(), 0).text():
                        objectToEdit = data

            userObjectToEdit = objectToEdit
            self.main = EditInspectorScreenApp()
            self.main.show()
            self.close()

    def deleteButtonForInspectorClick(self):
        global AllUsers

        button = self.sender()
        index = self.inspectorTable.indexAt(button.pos())
        if index.isValid():
            msg = QMessageBox()
            msg.setWindowTitle("Delete Inspector")
            msg.setText(
                "Are you sure you want to delete " + self.inspectorTable.item(index.row(), 0).text() + " Inspector.")
            msg.setIcon(QMessageBox.Question)
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)  # seperate buttons with "|"
            msg.setDefaultButton(QMessageBox.No)  # setting default button to Cancel
            x = msg.exec_()  # this will show our messagebox
            if x == 16384:
                objectToDelete = None
                for data in AllUsers:
                    if data['role'] == 'inspector':
                        if data['name'] == self.inspectorTable.item(index.row(), 0).text():
                            objectToDelete = data

                deleteSuperVisor(objectToDelete['id'])
                self.main = AdminHomeScreenApp()
                self.main.show()
                self.close()

# Statistics Button Functionality...

    def loadInformationTableData(self):
        global NoOfSupervisor
        global NoOfInspector
        global NoOfAdmin
        NofBatches , total_packets ,valid , invalid = stat(user_id=1)

        self.informationTableWdget.setColumnWidth(1, 20)
        self.informationTableWdget.setRowCount(6)
        self.informationTableWdget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(NoOfSupervisor)))
        self.informationTableWdget.setItem(1, 0, QtWidgets.QTableWidgetItem(str(NoOfInspector)))
        self.informationTableWdget.setItem(2, 0, QtWidgets.QTableWidgetItem(str(NoOfAdmin)))
        self.informationTableWdget.setItem(3, 0, QtWidgets.QTableWidgetItem(str(total_packets)))
        self.informationTableWdget.setItem(4, 0, QtWidgets.QTableWidgetItem(str(valid)))
        self.informationTableWdget.setItem(5, 0, QtWidgets.QTableWidgetItem(str(invalid)))


# logut Button Functionality...

    def onLogoutButtonClick(self):
        msg = QMessageBox()
        msg.setWindowTitle("Logout Button Click")
        msg.setText("Are you sure you want to Logout.")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)  # seperate buttons with "|"
        msg.setDefaultButton(QMessageBox.No)  # setting default button to Cancel
        x = msg.exec_()  # this will show our messagebox
        if x == 16384:
            self.main = LoginApp()
            self.main.show()
            self.close()

# Top functionality App
    def toggleMenu(self):
        maxWidth = 220
        enable = True
        if enable:
            # GET WIDTH
            width = self.frame_left_menu_2.width()
            maxExtend = maxWidth
            standard = 70
            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard
            # ANIMATION
            self.animation = QPropertyAnimation(self.frame_left_menu_2, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def maximizeButtonClick(self):
        print("Maximize Button Click")

    def minimizeButtonClick(self):
        self.showMinimized()

    def closeButtonClick(self):
        msg = QMessageBox()
        msg.setWindowTitle("Close Button")
        msg.setText("Are you sure you want to quit.")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)  # seperate buttons with "|"
        msg.setDefaultButton(QMessageBox.No)  # setting default button to Cancel
        x = msg.exec_()  # this will show our messagebox
        if x == 16384:
            self.close()

# Use in Home Screen...
class StartInspectionApp(QtWidgets.QMainWindow, ui_startInspectionScreen.Ui_MainWindow):
    def __init__(self, parent=None):
        super(StartInspectionApp, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.btn_close.setIcon(QtGui.QIcon("views/icons/16x16/cil-x.png"))
        self.btn_close.setIconSize(QtCore.QSize(16 , 16))
        self.btn_maximize_restore.setIcon(QtGui.QIcon("views/icons/16x16/cil-window-maximize.png"))
        self.btn_maximize_restore.setIconSize(QtCore.QSize(16, 16))
        self.btn_minimize.setIcon(QtGui.QIcon("views/icons/16x16/cil-window-minimize.png"))
        self.btn_minimize.setIconSize(QtCore.QSize(16, 16))
        self.goBack.setIcon(QtGui.QIcon("views/icons/previous.png"))
        self.goBack.setIconSize(QtCore.QSize(25, 25))

        self.logic = 0

        self.frontFileName = " "
        self.backFileName = " "

        self.startBackInspection.clicked.connect(self.bothVideoStarterFunction)
        self.stopBackInspection.clicked.connect(self.stopInspectionClick)

        self.goBack.clicked.connect(self.backScreenButtonClick)
        self.openFrontVideo.clicked.connect(self.open_front_file)
        self.openBackVideo.clicked.connect(self.open_back_file)

        # Top Functionality...
        self.btn_close.clicked.connect(self.closeButtonClick)
        self.btn_minimize.clicked.connect(self.minimizeButtonClick)

    def maximizeButtonClick(self):
        print("Maximize Button Click")

    def minimizeButtonClick(self):
        self.showMinimized()

    def closeButtonClick(self):
        msg = QMessageBox()
        msg.setWindowTitle("Close Button")
        msg.setText("Are you sure you want to quit.")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)  # seperate buttons with "|"
        msg.setDefaultButton(QMessageBox.No)  # setting default button to Cancel
        x = msg.exec_()  # this will show our messagebox
        if x == 16384:
            self.close()

    def backScreenButtonClick(self):
        self.main = AdminHomeScreenApp()
        self.main.show()
        self.close()

    # Back Inspection Algo...
    def startInspectionClick(self):
        counter = 0
        self.logic = 1
        net = cv2.dnn.readNet("yolov3-tiny6_custom_8000.weights", "yolov3-tiny6_custom.cfg")

        classes = []
        global packetsClassIdBack

        classes = ["barcode", "Template Matched", "uanble to find", "Invalid Printing"]
        layer_names = net.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        colors = np.random.uniform(0, 255, size=(len(classes), 3))
        cap = cv2.VideoCapture(self.backFileName)

        while (cap.isOpened()):
            ret, img = cap.read()

            if ret == True:

                height, width, channels = img.shape
                (H, W) = img.shape[:2]

                # determine only the output layer names that we need from YOLO

                ln = net.getLayerNames()
                ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

                    # construct a blob from the input image and then perform a forward
                    # pass of the YOLO object detector, giving us our bounding boxes and
                    # associated probabilities

                blob = cv2.dnn.blobFromImage(img, 1 / 255.0, (416, 416), swapRB=True, crop=False)
                net.setInput(blob)
                start = time.time()
                layerOutputs = net.forward(ln)
                end = time.time()

                # initialize our lists of detected bounding boxes, confidences, and
                # class IDs, respectively

                boxes = []
                confidences = []
                classIDs = []
                # loop over each of the layer outputs

                for output in layerOutputs:
                    # loop over each of the detections
                    for detection in output:
                        # extract the class ID and confidence (i.e., probability) of
                            # the current object detection
                        scores = detection[5:]
                        classID = np.argmax(scores)
                        confidence = scores[classID]
                        # filter out weak predictions by ensuring the detected
                        # probability is greater than the minimum probability
                        if confidence > 0.5:
                                # scale the bounding box coordinates back relative to the
                                # size of the image, keeping in mind that YOLO actually
                                # returns the center (x, y)-coordinates of the bounding
                                # box followed by the boxes' width and height
                            box = detection[0:4] * np.array([W, H, W, H])
                            (centerX, centerY, width, height) = box.astype("int")
                            # use the center (x, y)-coordinates to derive the top and
                            # and left corner of the bounding box
                            x = int(centerX - (width / 2))
                            y = int(centerY - (height / 2))
                            # update our list of bounding box coordinates, confidences,
                            # and class IDs
                            boxes.append([x, y, int(width), int(height)])
                            confidences.append(float(confidence))
                            classIDs.append(classID)

                # apply non-maxima suppression to suppress weak, overlapping bounding
                # boxes
                indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

                COLORS = np.random.randint(0, 255, size=(len(classes), 3), dtype="uint8")

                # ensure at least one detection exists
                if len(indexes) > 0:
                    for i in indexes.flatten():
                        # extract the bounding box coordinatesz
                        (x, y) = (boxes[i][0], boxes[i][1])
                        (w, h) = (boxes[i][2], boxes[i][3])
                        # draw a bounding box rectangle and label on the image
                        packetsClassIdBack.append(classIDs[i])
                        color = [int(c) for c in COLORS[classIDs[i]]]
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
                        text = "{}: {:.4f}".format(classes[classIDs[i]], confidences[i])
                        cv2.putText(img, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
                        Label = classIDs[i]
                    # show the output image

                dim = (770, 501)
                counter = counter + 1
                print(counter)
                if counter == 45:
                    print("Counter value is ",counter,"this when we call database function.")
                    self.sendResultToDataBase()
                if counter == 90:
                    print("Counter value is ", counter, "this when we call database function.")
                    self.sendResultToDataBase()

                self.displayImage(img, 1)
                time.sleep(0.03)
                cv2.waitKey()

                if (self.logic == 0):
                    break

            else:
                s = None


        cap.release()
        cv2.destroyAllWindows()

    def stopInspectionClick(self):
        self.logic = 0

    def displayImage(self , img , window = 1):
        qFormat = QImage.Format_Indexed8

        if len(img.shape) == 3:
            if (img.shape[2]) == 4:
                qFormat = QImage.Format_RGBA8888
            else:
                qFormat = QImage.Format_RGB888

        img = QImage(img , img.shape[1] , img.shape[0] , qFormat)
        img = img.rgbSwapped()
        self.backLabel.setPixmap(QPixmap.fromImage(img))
        self.backLabel.setScaledContents(True)


    # Front Inspection Algo...
    @pyqtSlot()
    def startFrontInspectionClick(self):
        self.logic = 1
        global packetsClassIdFront
        net = cv2.dnn.readNet("yolov3-tiny6_custom_6000.weights", "yolov3-tiny6_front_custom.cfg")
        classes = []

        classes = ["Template Matched", "Invalid Printing", "dirt spot"]
        layer_names = net.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        colors = np.random.uniform(0, 255, size=(len(classes), 3))

        cap = cv2.VideoCapture(self.frontFileName)

        while (cap.isOpened()):
            ret, img = cap.read()

            if ret == True:

                height, width, channels = img.shape
                (H, W) = img.shape[:2]

                    # determine only the output layer names that we need from YOLO

                ln = net.getLayerNames()
                ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

                    # construct a blob from the input image and then perform a forward
                    # pass of the YOLO object detector, giving us our bounding boxes and
                    # associated probabilities

                blob = cv2.dnn.blobFromImage(img, 1 / 255.0, (416, 416), swapRB=True, crop=False)
                net.setInput(blob)
                start = time.time()
                layerOutputs = net.forward(ln)
                end = time.time()


                    # initialize our lists of detected bounding boxes, confidences, and
                    # class IDs, respectively

                boxes = []
                confidences = []
                classIDs = []
                # loop over each of the layer outputs

                for output in layerOutputs:
                    # loop over each of the detections
                    for detection in output:
                        # extract the class ID and confidence (i.e., probability) of
                        # the current object detection
                        scores = detection[5:]
                        classID = np.argmax(scores)
                        confidence = scores[classID]
                        # filter out weak predictions by ensuring the detected
                        # probability is greater than the minimum probability
                        if confidence > 0.5:
                        # scale the bounding box coordinates back relative to the
                            # size of the image, keeping in mind that YOLO actually
                            # returns the center (x, y)-coordinates of the bounding
                            # box followed by the boxes' width and height
                            box = detection[0:4] * np.array([W, H, W, H])
                            (centerX, centerY, width, height) = box.astype("int")
                            # use the center (x, y)-coordinates to derive the top and
                            # and left corner of the bounding box
                            x = int(centerX - (width / 2))
                            y = int(centerY - (height / 2))
                            # update our list of bounding box coordinates, confidences,
                            # and class IDs
                            boxes.append([x, y, int(width), int(height)])
                            confidences.append(float(confidence))
                            classIDs.append(classID)

                # apply non-maxima suppression to suppress weak, overlapping bounding
                # boxes
                indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

                COLORS = np.random.randint(0, 255, size=(len(classes), 3), dtype="uint8")

                # ensure at least one detection exists
                if len(indexes) > 0:
                    # loop over the indexes we are keeping
                    for i in indexes.flatten():
                        # extract the bounding box coordinatesz
                        (x, y) = (boxes[i][0], boxes[i][1])
                        (w, h) = (boxes[i][2], boxes[i][3])
                        packetsClassIdFront.append(classIDs[i])
                        # draw a bounding box rectangle and label on the image
                        color = [int(c) for c in COLORS[classIDs[i]]]
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
                        text = "{}: {:.4f}".format(classes[classIDs[i]], confidences[i])
                        cv2.putText(img, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
                        Label = classIDs[i]
                # show the output image

                dim = (770, 501)


                self.displayFrontImage(img, 1)
                cv2.waitKey()
                time.sleep(0.03)

                if (self.logic == 0):
                    break

            else:
                self.main = AdminHomeScreenApp()
                self.main.show()
                self.close()

        cap.release()
        cv2.destroyAllWindows()

    def stopFrontInspectionClick(self):
        self.logic = 0

    def displayFrontImage(self , img , window = 1):
        qFormat = QImage.Format_Indexed8

        if len(img.shape) == 3:
            if (img.shape[2]) == 4:
                qFormat = QImage.Format_RGBA8888
            else:
                qFormat = QImage.Format_RGB888

        img = QImage(img , img.shape[1] , img.shape[0] , qFormat)
        img = img.rgbSwapped()
        self.frontLabel.setPixmap(QPixmap.fromImage(img))
        self.frontLabel.setScaledContents(True)


    @pyqtSlot()
    def bothVideoStarterFunction(self):
        if self.backFileName == " ":
            msg = QMessageBox()
            msg.setWindowTitle("File Error")
            msg.setText("Please select a video file for Back View")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
        elif self.frontFileName == " ":
            msg = QMessageBox()
            msg.setWindowTitle("File Error")
            msg.setText("Please select a video file for Front View")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()

        else:
            Thread(target=self.startInspectionClick).start()
            Thread(target=self.startFrontInspectionClick).start()


    def sendResultToDataBase(self):
        global packetsClassIdFront
        global packetsClassIdBack

        print("Front Packets ID")
        print(packetsClassIdFront)
        print("Back Packets ID")
        print(packetsClassIdBack)


        result = "valid"

        for number in packetsClassIdBack:
            if int(number) == 2 or int(number) == 3:
                result = "invalid"

        for number in packetsClassIdFront:
            if int(number) == 1 or int(number) == 2:
                result = "invalid"

        saveInspectionResult(result)

        packetsClassIdFront = []
        packetsClassIdBack = []

    def open_front_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Front Video")
        self.frontFileName = filename

    def open_back_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Back Video")
        self.backFileName = filename


# Use in Admin Panel...
class AddSupervisorScreenApp(QtWidgets.QMainWindow, ui_addSupervisorScreen.Ui_MainWindow):
    def __init__(self, parent=None):
        super(AddSupervisorScreenApp, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.btn_close.setIcon(QtGui.QIcon("views/icons/16x16/cil-x.png"))
        self.btn_close.setIconSize(QtCore.QSize(16 , 16))
        self.btn_maximize_restore.setIcon(QtGui.QIcon("views/icons/16x16/cil-window-maximize.png"))
        self.btn_maximize_restore.setIconSize(QtCore.QSize(16, 16))
        self.btn_minimize.setIcon(QtGui.QIcon("views/icons/16x16/cil-window-minimize.png"))
        self.btn_minimize.setIconSize(QtCore.QSize(16, 16))
        self.addSupervisor.clicked.connect(self.addNewSupervisorButtonClick)
        self.cancle.clicked.connect(self.cancleButtonClick)

        # Top Functionality...
        self.btn_close.clicked.connect(self.closeButtonClick)
        self.btn_minimize.clicked.connect(self.minimizeButtonClick)

    def maximizeButtonClick(self):
        print("Maximize Button Click")

    def minimizeButtonClick(self):
        self.showMinimized()

    def closeButtonClick(self):
        msg = QMessageBox()
        msg.setWindowTitle("Close Button")
        msg.setText("Are you sure you want to quit.")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)  # seperate buttons with "|"
        msg.setDefaultButton(QMessageBox.No)  # setting default button to Cancel
        x = msg.exec_()  # this will show our messagebox
        if x == 16384:
            self.close()

    def addNewSupervisorButtonClick(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Add User")

        if self.nameLineEdit.text() == "":
            msg.setText('Please fill the Username Field')
            msg.exec_()
        elif self.emailLineEdit.text() == "":
            msg.setText('Please fill the Email Field')
            msg.exec_()
        elif self.passwordLineEdit.text() == "":
            msg.setText('Please fill the Password Field')
            msg.exec_()
        else:
            result = addNewSupervisor(self.nameLineEdit.text(),self.emailLineEdit.text(),self.passwordLineEdit.text())
            msg.setText('Add New Supervisor')
            msg.exec_()


    def cancleButtonClick(self):
        self.main = AdminHomeScreenApp()
        self.main.show()
        self.close()

class AddInspectorScreenApp(QtWidgets.QMainWindow, ui_addInspectorScreen.Ui_MainWindow):
    def __init__(self, parent=None):
        super(AddInspectorScreenApp, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.addInspector.clicked.connect(self.addNewInspectorButtonClick)
        self.cancle.clicked.connect(self.cancleButtonClick)
        self.btn_close.setIcon(QtGui.QIcon("views/icons/16x16/cil-x.png"))
        self.btn_close.setIconSize(QtCore.QSize(16 , 16))
        self.btn_maximize_restore.setIcon(QtGui.QIcon("views/icons/16x16/cil-window-maximize.png"))
        self.btn_maximize_restore.setIconSize(QtCore.QSize(16, 16))
        self.btn_minimize.setIcon(QtGui.QIcon("views/icons/16x16/cil-window-minimize.png"))
        self.btn_minimize.setIconSize(QtCore.QSize(16, 16))

        # Top Functionality...
        self.btn_close.clicked.connect(self.closeButtonClick)
        self.btn_minimize.clicked.connect(self.minimizeButtonClick)

    def maximizeButtonClick(self):
        print("Maximize Button Click")

    def minimizeButtonClick(self):
        self.showMinimized()

    def closeButtonClick(self):
        msg = QMessageBox()
        msg.setWindowTitle("Close Button")
        msg.setText("Are you sure you want to quit.")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)  # seperate buttons with "|"
        msg.setDefaultButton(QMessageBox.No)  # setting default button to Cancel
        x = msg.exec_()  # this will show our messagebox
        if x == 16384:
            self.close()

    def addNewInspectorButtonClick(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Add User")

        if self.nameLineEdit.text() == "":
            msg.setText('Please fill the Username Field')
            msg.exec_()
        elif self.emailLineEdit.text() == "":
            msg.setText('Please fill the Email Field')
            msg.exec_()
        elif self.passwordLineEdit.text() == "":
            msg.setText('Please fill the Password Field')
            msg.exec_()
        else:
            result = addNewInspector(self.nameLineEdit.text(),self.emailLineEdit.text(),self.passwordLineEdit.text())
            msg.setText('Add New Inspector')
            msg.exec_()


    def cancleButtonClick(self):
        self.main = AdminHomeScreenApp()
        self.main.show()
        self.close()

class EditSupervisorScreenApp(QtWidgets.QMainWindow, ui_editSupervisorScreen.Ui_MainWindow):
    def __init__(self, parent=None):
        super(EditSupervisorScreenApp, self).__init__(parent)
        self.setupUi(self)
        global userObjectToEdit
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.btn_close.setIcon(QtGui.QIcon("views/icons/16x16/cil-x.png"))
        self.btn_close.setIconSize(QtCore.QSize(16 , 16))
        self.btn_maximize_restore.setIcon(QtGui.QIcon("views/icons/16x16/cil-window-maximize.png"))
        self.btn_maximize_restore.setIconSize(QtCore.QSize(16, 16))
        self.btn_minimize.setIcon(QtGui.QIcon("views/icons/16x16/cil-window-minimize.png"))
        self.btn_minimize.setIconSize(QtCore.QSize(16, 16))


        self.userID.setText(str(userObjectToEdit['id']))
        self.nameLineEdit.setText(str(userObjectToEdit['name']))
        self.emailLineEdit.setText(str(userObjectToEdit['email']))
        self.passwordLineEdit.setText("")

        self.addSupervisor.clicked.connect(self.editSupervisorButtonClick)
        self.cancle.clicked.connect(self.cancleButtonClick)

        # Top Functionality...
        self.btn_close.clicked.connect(self.closeButtonClick)
        self.btn_minimize.clicked.connect(self.minimizeButtonClick)

    def editSupervisorButtonClick(self):
        editSupervisor(str(userObjectToEdit['id']),self.nameLineEdit.text(),self.emailLineEdit.text(),self.passwordLineEdit.text())
        self.main = AdminHomeScreenApp()
        self.main.show()
        self.close()

    def cancleButtonClick(self):
        self.main = AdminHomeScreenApp()
        self.main.show()
        self.close()
    def maximizeButtonClick(self):
        print("Maximize Button Click")

    def minimizeButtonClick(self):
        self.showMinimized()

    def closeButtonClick(self):
        msg = QMessageBox()
        msg.setWindowTitle("Close Button")
        msg.setText("Are you sure you want to quit.")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)  # seperate buttons with "|"
        msg.setDefaultButton(QMessageBox.No)  # setting default button to Cancel
        x = msg.exec_()  # this will show our messagebox
        if x == 16384:
            self.close()

    def addNewSupervisorButtonClick(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("LOGIN ERROR")

        if self.nameLineEdit.text() == "":
            msg.setText('Please fill the Username Field')
            msg.exec_()
        elif self.emailLineEdit.text() == "":
            msg.setText('Please fill the Email Field')
            msg.exec_()
        elif self.passwordLineEdit.text() == "":
            msg.setText('Please fill the Password Field')
            msg.exec_()
        else:
            result = addNewSupervisor(self.nameLineEdit.text(),self.emailLineEdit.text(),self.passwordLineEdit.text())
            msg.setText('Add New Supervisor')
            msg.exec_()


    def cancleButtonClick(self):
        self.main = AdminHomeScreenApp()
        self.main.show()
        self.close()


class EditInspectorScreenApp(QtWidgets.QMainWindow, ui_editInspectorScreen.Ui_MainWindow):
    def __init__(self, parent=None):
        super(EditInspectorScreenApp, self).__init__(parent)
        self.setupUi(self)
        global userObjectToEdit
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.btn_close.setIcon(QtGui.QIcon("views/icons/16x16/cil-x.png"))
        self.btn_close.setIconSize(QtCore.QSize(16 , 16))
        self.btn_maximize_restore.setIcon(QtGui.QIcon("views/icons/16x16/cil-window-maximize.png"))
        self.btn_maximize_restore.setIconSize(QtCore.QSize(16, 16))
        self.btn_minimize.setIcon(QtGui.QIcon("views/icons/16x16/cil-window-minimize.png"))
        self.btn_minimize.setIconSize(QtCore.QSize(16, 16))

        # print(userObjectToEdit['id'])
        self.userID.setText(str(userObjectToEdit['id']))
        self.nameLineEdit.setText(str(userObjectToEdit['name']))
        self.emailLineEdit.setText(str(userObjectToEdit['email']))
        self.passwordLineEdit.setText("")
        #
        self.addInspector.clicked.connect(self.editSupervisorButtonClick)
        self.cancle.clicked.connect(self.cancleButtonClick)

        # Top Functionality...
        self.btn_close.clicked.connect(self.closeButtonClick)
        self.btn_minimize.clicked.connect(self.minimizeButtonClick)

    def editSupervisorButtonClick(self):
        editInspector(str(userObjectToEdit['id']),self.nameLineEdit.text(),self.emailLineEdit.text(),self.passwordLineEdit.text())
        self.main = AdminHomeScreenApp()
        self.main.show()
        self.close()

    def cancleButtonClick(self):
        self.main = AdminHomeScreenApp()
        self.main.show()
        self.close()

    def maximizeButtonClick(self):
        print("Maximize Button Click")

    def minimizeButtonClick(self):
        self.showMinimized()

    def closeButtonClick(self):
        msg = QMessageBox()
        msg.setWindowTitle("Close Button")
        msg.setText("Are you sure you want to quit.")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)  # seperate buttons with "|"
        msg.setDefaultButton(QMessageBox.No)  # setting default button to Cancel
        x = msg.exec_()  # this will show our messagebox
        if x == 16384:
            self.close()

    def addNewSupervisorButtonClick(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("LOGIN ERROR")

        if self.nameLineEdit.text() == "":
            msg.setText('Please fill the Username Field')
            msg.exec_()
        elif self.emailLineEdit.text() == "":
            msg.setText('Please fill the Email Field')
            msg.exec_()
        elif self.passwordLineEdit.text() == "":
            msg.setText('Please fill the Password Field')
            msg.exec_()
        else:
            result = addNewSupervisor(self.nameLineEdit.text(),self.emailLineEdit.text(),self.passwordLineEdit.text())
            msg.setText('Add New Supervisor')
            msg.exec_()


    def cancleButtonClick(self):
        self.main = AdminHomeScreenApp()
        self.main.show()
        self.close()


def main():
    app = QApplication(sys.argv)
    form = SplashScreenApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()