# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminHomeScreen.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1069, 705)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1071, 71))
        self.frame.setStyleSheet("background-color: rgb(27, 29, 35);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_toggle_menu_2 = QtWidgets.QPushButton(self.frame)
        self.btn_toggle_menu_2.setGeometry(QtCore.QRect(0, 0, 70, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu_2.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu_2.setSizePolicy(sizePolicy)
        self.btn_toggle_menu_2.setStyleSheet("QPushButton {\n"
"    \n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    border: none;\n"
"    background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_toggle_menu_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../realTimeInspectionSystem/view/desktopAppIcons/24x24/cil-menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_toggle_menu_2.setIcon(icon)
        self.btn_toggle_menu_2.setIconSize(QtCore.QSize(24, 24))
        self.btn_toggle_menu_2.setObjectName("btn_toggle_menu_2")
        self.frame_label_top_btns = QtWidgets.QFrame(self.frame)
        self.frame_label_top_btns.setGeometry(QtCore.QRect(70, 0, 881, 42))
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
        self.btn_close.setGeometry(QtCore.QRect(1020, 0, 40, 42))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/24x24/cil-x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon1)
        self.btn_close.setObjectName("btn_close")
        self.btn_minimize = QtWidgets.QPushButton(self.frame)
        self.btn_minimize.setGeometry(QtCore.QRect(940, 0, 40, 42))
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/24x24/cil-window-minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_minimize.setIcon(icon2)
        self.btn_minimize.setObjectName("btn_minimize")
        self.btn_maximize_restore = QtWidgets.QPushButton(self.frame)
        self.btn_maximize_restore.setGeometry(QtCore.QRect(980, 0, 40, 42))
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/24x24/cil-window-maximize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_maximize_restore.setIcon(icon3)
        self.btn_maximize_restore.setObjectName("btn_maximize_restore")
        self.frame_top_info = QtWidgets.QFrame(self.frame)
        self.frame_top_info.setGeometry(QtCore.QRect(70, 50, 1001, 23))
        self.frame_top_info.setMaximumSize(QtCore.QSize(16777215, 65))
        self.frame_top_info.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_info.setObjectName("frame_top_info")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(-1, 69, 1071, 641))
        self.frame_2.setStyleSheet("background-color: rgb(40, 44, 52);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(-1, -1, 72, 641))
        self.frame_3.setStyleSheet("background-color: rgb(27, 29, 35);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.profileButton = QtWidgets.QLabel(self.frame_3)
        self.profileButton.setGeometry(QtCore.QRect(10, 530, 60, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profileButton.sizePolicy().hasHeightForWidth())
        self.profileButton.setSizePolicy(sizePolicy)
        self.profileButton.setMinimumSize(QtCore.QSize(60, 60))
        self.profileButton.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.profileButton.setFont(font)
        self.profileButton.setStyleSheet("QLabel {\n"
"    border-radius: 30px;\n"
"    background-color: rgb(44, 49, 60);\n"
"    border: 5px solid rgb(39, 44, 54);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}")
        self.profileButton.setAlignment(QtCore.Qt.AlignCenter)
        self.profileButton.setObjectName("profileButton")
        self.homeButton = QtWidgets.QPushButton(self.frame_3)
        self.homeButton.setGeometry(QtCore.QRect(0, 57, 71, 52))
        self.homeButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/views/icons/house.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeButton.setIcon(icon4)
        self.homeButton.setIconSize(QtCore.QSize(30, 44))
        self.homeButton.setObjectName("homeButton")
        self.logoutButton = QtWidgets.QPushButton(self.frame_3)
        self.logoutButton.setGeometry(QtCore.QRect(-1, 260, 81, 52))
        self.logoutButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/log-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logoutButton.setIcon(icon5)
        self.logoutButton.setIconSize(QtCore.QSize(33, 44))
        self.logoutButton.setObjectName("logoutButton")
        self.statisticsButton = QtWidgets.QPushButton(self.frame_3)
        self.statisticsButton.setGeometry(QtCore.QRect(-1, 163, 71, 52))
        self.statisticsButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/statistics.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.statisticsButton.setIcon(icon6)
        self.statisticsButton.setIconSize(QtCore.QSize(33, 44))
        self.statisticsButton.setObjectName("statisticsButton")
        self.adminPanelButton = QtWidgets.QPushButton(self.frame_3)
        self.adminPanelButton.setGeometry(QtCore.QRect(0, 110, 71, 52))
        self.adminPanelButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/adminPanel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.adminPanelButton.setIcon(icon7)
        self.adminPanelButton.setIconSize(QtCore.QSize(33, 44))
        self.adminPanelButton.setObjectName("adminPanelButton")
        self.profileButtonOrignal = QtWidgets.QPushButton(self.frame_3)
        self.profileButtonOrignal.setGeometry(QtCore.QRect(0, 210, 71, 52))
        self.profileButtonOrignal.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.profileButtonOrignal.setIcon(icon8)
        self.profileButtonOrignal.setIconSize(QtCore.QSize(33, 44))
        self.profileButtonOrignal.setObjectName("profileButtonOrignal")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(80, 0, 981, 611))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_4)
        self.stackedWidget.setGeometry(QtCore.QRect(-10, 0, 991, 606))
        self.stackedWidget.setStyleSheet("background: transparent;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageHome = QtWidgets.QWidget()
        self.pageHome.setObjectName("pageHome")
        self.label = QtWidgets.QLabel(self.pageHome)
        self.label.setGeometry(QtCore.QRect(10, 109, 973, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 15))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame_11 = QtWidgets.QFrame(self.pageHome)
        self.frame_11.setGeometry(QtCore.QRect(10, 140, 973, 448))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.startInspection = QtWidgets.QPushButton(self.frame_11)
        self.startInspection.setGeometry(QtCore.QRect(330, 112, 101, 101))
        self.startInspection.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"")
        self.startInspection.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/inspection.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startInspection.setIcon(icon9)
        self.startInspection.setIconSize(QtCore.QSize(50, 50))
        self.startInspection.setObjectName("startInspection")
        self.showStatistics = QtWidgets.QPushButton(self.frame_11)
        self.showStatistics.setGeometry(QtCore.QRect(520, 112, 101, 101))
        self.showStatistics.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"")
        self.showStatistics.setText("")
        self.showStatistics.setIcon(icon6)
        self.showStatistics.setIconSize(QtCore.QSize(50, 50))
        self.showStatistics.setObjectName("showStatistics")
        self.label_3 = QtWidgets.QLabel(self.frame_11)
        self.label_3.setGeometry(QtCore.QRect(330, 230, 111, 31))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_11)
        self.label_4.setGeometry(QtCore.QRect(520, 240, 101, 16))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.topUserName = QtWidgets.QLabel(self.pageHome)
        self.topUserName.setGeometry(QtCore.QRect(10, 0, 973, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topUserName.sizePolicy().hasHeightForWidth())
        self.topUserName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.topUserName.setFont(font)
        self.topUserName.setStyleSheet("color: rgb(255, 255, 255);")
        self.topUserName.setAlignment(QtCore.Qt.AlignCenter)
        self.topUserName.setObjectName("topUserName")
        self.stackedWidget.addWidget(self.pageHome)
        self.pageAdminPanel = QtWidgets.QWidget()
        self.pageAdminPanel.setObjectName("pageAdminPanel")
        self.label_9 = QtWidgets.QLabel(self.pageAdminPanel)
        self.label_9.setGeometry(QtCore.QRect(390, 20, 201, 61))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 28pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.supervisorTable = QtWidgets.QTableWidget(self.pageAdminPanel)
        self.supervisorTable.setGeometry(QtCore.QRect(90, 280, 351, 192))
        self.supervisorTable.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.supervisorTable.setObjectName("supervisorTable")
        self.supervisorTable.setColumnCount(3)
        self.supervisorTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.supervisorTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.supervisorTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.supervisorTable.setHorizontalHeaderItem(2, item)
        self.label_6 = QtWidgets.QLabel(self.pageAdminPanel)
        self.label_6.setGeometry(QtCore.QRect(700, 230, 81, 41))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.addSupervisor = QtWidgets.QPushButton(self.pageAdminPanel)
        self.addSupervisor.setGeometry(QtCore.QRect(240, 560, 141, 31))
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
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../../Desktop App/icons/24x24/cil-plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addSupervisor.setIcon(icon10)
        self.addSupervisor.setIconSize(QtCore.QSize(16, 16))
        self.addSupervisor.setObjectName("addSupervisor")
        self.searchButton = QtWidgets.QPushButton(self.pageAdminPanel)
        self.searchButton.setGeometry(QtCore.QRect(750, 150, 41, 41))
        self.searchButton.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchButton.setIcon(icon11)
        self.searchButton.setIconSize(QtCore.QSize(30, 30))
        self.searchButton.setObjectName("searchButton")
        self.addInspector = QtWidgets.QPushButton(self.pageAdminPanel)
        self.addInspector.setGeometry(QtCore.QRect(690, 560, 151, 31))
        self.addInspector.setStyleSheet("color: rgb(255, 255, 255);\n"
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
        self.addInspector.setIcon(icon10)
        self.addInspector.setIconSize(QtCore.QSize(16, 16))
        self.addInspector.setObjectName("addInspector")
        self.label_5 = QtWidgets.QLabel(self.pageAdminPanel)
        self.label_5.setGeometry(QtCore.QRect(210, 230, 91, 41))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.pageAdminPanel)
        self.label_8.setGeometry(QtCore.QRect(620, 510, 71, 81))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("icons/inspector.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.pageAdminPanel)
        self.label_7.setGeometry(QtCore.QRect(160, 510, 81, 81))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("icons/supervisor.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.inspectorTable = QtWidgets.QTableWidget(self.pageAdminPanel)
        self.inspectorTable.setGeometry(QtCore.QRect(570, 280, 341, 192))
        self.inspectorTable.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inspectorTable.setObjectName("inspectorTable")
        self.inspectorTable.setColumnCount(3)
        self.inspectorTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.inspectorTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.inspectorTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.inspectorTable.setHorizontalHeaderItem(2, item)
        self.label_12 = QtWidgets.QLabel(self.pageAdminPanel)
        self.label_12.setGeometry(QtCore.QRect(140, 140, 131, 61))
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 20pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.searchBar = QtWidgets.QLineEdit(self.pageAdminPanel)
        self.searchBar.setGeometry(QtCore.QRect(300, 150, 441, 41))
        self.searchBar.setStyleSheet("background-color: rgb(34, 34, 34);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius : 20px;\n"
"padding : 2px;\n"
"padding-left : 4px;")
        self.searchBar.setObjectName("searchBar")
        self.stackedWidget.addWidget(self.pageAdminPanel)
        self.pageStatistics = QtWidgets.QWidget()
        self.pageStatistics.setObjectName("pageStatistics")
        self.label_10 = QtWidgets.QLabel(self.pageStatistics)
        self.label_10.setGeometry(QtCore.QRect(420, 20, 141, 61))
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 28pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.informationTableWdget = QtWidgets.QTableWidget(self.pageStatistics)
        self.informationTableWdget.setGeometry(QtCore.QRect(755, 120, 201, 231))
        self.informationTableWdget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.informationTableWdget.setObjectName("informationTableWdget")
        self.informationTableWdget.setColumnCount(1)
        self.informationTableWdget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.informationTableWdget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.informationTableWdget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.informationTableWdget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.informationTableWdget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.informationTableWdget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.informationTableWdget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.informationTableWdget.setHorizontalHeaderItem(0, item)
        self.label_13 = QtWidgets.QLabel(self.pageStatistics)
        self.label_13.setGeometry(QtCore.QRect(756, 100, 201, 41))
        self.label_13.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.pieChartFrame = QtWidgets.QFrame(self.pageStatistics)
        self.pieChartFrame.setGeometry(QtCore.QRect(150, 200, 401, 201))
        self.pieChartFrame.setStyleSheet("border : 2px solid white;")
        self.pieChartFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pieChartFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pieChartFrame.setObjectName("pieChartFrame")
        self.barChartFrame = QtWidgets.QFrame(self.pageStatistics)
        self.barChartFrame.setGeometry(QtCore.QRect(10, 500, 211, 101))
        self.barChartFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barChartFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barChartFrame.setObjectName("barChartFrame")
        self.label_14 = QtWidgets.QLabel(self.pageStatistics)
        self.label_14.setGeometry(QtCore.QRect(40, 130, 251, 41))
        self.label_14.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")
        self.stackedWidget.addWidget(self.pageStatistics)
        self.pageProfile = QtWidgets.QWidget()
        self.pageProfile.setObjectName("pageProfile")
        self.label_11 = QtWidgets.QLabel(self.pageProfile)
        self.label_11.setGeometry(QtCore.QRect(410, 20, 191, 61))
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 28pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
        self.frame_5 = QtWidgets.QFrame(self.pageProfile)
        self.frame_5.setGeometry(QtCore.QRect(490, 110, 5, 500))
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.UserName = QtWidgets.QLabel(self.pageProfile)
        self.UserName.setGeometry(QtCore.QRect(590, 141, 311, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UserName.sizePolicy().hasHeightForWidth())
        self.UserName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.UserName.setFont(font)
        self.UserName.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 22pt \"MS Shell Dlg 2\";")
        self.UserName.setAlignment(QtCore.Qt.AlignCenter)
        self.UserName.setObjectName("UserName")
        self.EmailID = QtWidgets.QLabel(self.pageProfile)
        self.EmailID.setGeometry(QtCore.QRect(510, 250, 471, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EmailID.sizePolicy().hasHeightForWidth())
        self.EmailID.setSizePolicy(sizePolicy)
        self.EmailID.setMinimumSize(QtCore.QSize(0, 15))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.EmailID.setFont(font)
        self.EmailID.setStyleSheet("color: rgb(255, 255, 255);")
        self.EmailID.setAlignment(QtCore.Qt.AlignCenter)
        self.EmailID.setObjectName("EmailID")
        self.ROLEID = QtWidgets.QLabel(self.pageProfile)
        self.ROLEID.setGeometry(QtCore.QRect(510, 320, 471, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ROLEID.sizePolicy().hasHeightForWidth())
        self.ROLEID.setSizePolicy(sizePolicy)
        self.ROLEID.setMinimumSize(QtCore.QSize(0, 15))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.ROLEID.setFont(font)
        self.ROLEID.setStyleSheet("color: rgb(255, 255, 255);")
        self.ROLEID.setAlignment(QtCore.Qt.AlignCenter)
        self.ROLEID.setObjectName("ROLEID")
        self.label_15 = QtWidgets.QLabel(self.pageProfile)
        self.label_15.setGeometry(QtCore.QRect(50, 100, 371, 351))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("icons/profile.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.stackedWidget.addWidget(self.pageProfile)
        self.frame_label_bottom = QtWidgets.QFrame(self.frame_2)
        self.frame_label_bottom.setGeometry(QtCore.QRect(70, 610, 1001, 25))
        self.frame_label_bottom.setStyleSheet("background-color: rgb(27, 29, 35);")
        self.frame_label_bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_bottom.setObjectName("frame_label_bottom")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_credits = QtWidgets.QLabel(self.frame_label_bottom)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color: rgb(98, 103, 111);")
        self.label_credits.setObjectName("label_credits")
        self.horizontalLayout_7.addWidget(self.label_credits)
        self.label_version = QtWidgets.QLabel(self.frame_label_bottom)
        self.label_version.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_version.setFont(font)
        self.label_version.setStyleSheet("color: rgb(98, 103, 111);")
        self.label_version.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_version.setObjectName("label_version")
        self.horizontalLayout_7.addWidget(self.label_version)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title_bar_top.setText(_translate("MainWindow", "Main Window"))
        self.btn_close.setToolTip(_translate("MainWindow", "Close"))
        self.btn_minimize.setToolTip(_translate("MainWindow", "Minimize"))
        self.btn_maximize_restore.setToolTip(_translate("MainWindow", "Maximize"))
        self.profileButton.setText(_translate("MainWindow", "WM"))
        self.label.setText(_translate("MainWindow", "What would you like to do?"))
        self.label_3.setText(_translate("MainWindow", "Start Inspection"))
        self.label_4.setText(_translate("MainWindow", "Show Statistics"))
        self.topUserName.setText(_translate("MainWindow", "Welcome, User Name! "))
        self.label_9.setText(_translate("MainWindow", "Admin Panel"))
        item = self.supervisorTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.supervisorTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Edit"))
        item = self.supervisorTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Delete"))
        self.label_6.setText(_translate("MainWindow", "Inspector"))
        self.addSupervisor.setText(_translate("MainWindow", "Add Supervisor"))
        self.addInspector.setText(_translate("MainWindow", "Add Inspector"))
        self.label_5.setText(_translate("MainWindow", "Supervisor"))
        item = self.inspectorTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.inspectorTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Edit"))
        item = self.inspectorTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Delete"))
        self.label_12.setText(_translate("MainWindow", "Search Bar"))
        self.label_10.setText(_translate("MainWindow", "Statistics"))
        item = self.informationTableWdget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "No of Supervisor"))
        item = self.informationTableWdget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "No of Inspector"))
        item = self.informationTableWdget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "No of Admin"))
        item = self.informationTableWdget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Total batch Inspected"))
        item = self.informationTableWdget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Total strips accepted"))
        item = self.informationTableWdget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Total strips rejected"))
        self.label_13.setText(_translate("MainWindow", "Information"))
        self.label_14.setText(_translate("MainWindow", "Inspected Packets Chart"))
        self.label_11.setText(_translate("MainWindow", "User Profile"))
        self.UserName.setText(_translate("MainWindow", "Welcome, User Name! "))
        self.EmailID.setText(_translate("MainWindow", "Email : "))
        self.ROLEID.setText(_translate("MainWindow", "Role : "))
        self.label_credits.setText(_translate("MainWindow", "Made By : Abdul Wajid"))
        self.label_version.setText(_translate("MainWindow", "v1.0.0"))
