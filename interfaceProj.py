# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceProj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(2176, 1123)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color:#3F3F41;")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sideMenuContainer = QFrame(self.centralwidget)
        self.sideMenuContainer.setObjectName(u"sideMenuContainer")
        self.sideMenuContainer.setMinimumSize(QSize(250, 0))
        self.sideMenuContainer.setMaximumSize(QSize(0, 16777215))
        self.sideMenuContainer.setStyleSheet(u"background:url(:/pages/images/bg.png)\n"
"/*background:rgb(0, 0, 0)")
        self.sideMenuContainer.setFrameShape(QFrame.StyledPanel)
        self.sideMenuContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.sideMenuContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.slideMenu = QFrame(self.sideMenuContainer)
        self.slideMenu.setObjectName(u"slideMenu")
        self.slideMenu.setMinimumSize(QSize(248, 0))
        self.slideMenu.setFrameShape(QFrame.StyledPanel)
        self.slideMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.slideMenu)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.slideMenu)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(220, 95))
        self.label_3.setMaximumSize(QSize(80, 80))
        self.label_3.setStyleSheet(u"background:transparent;")
        self.label_3.setPixmap(QPixmap(u":/pages/images/tempLogo.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setIndent(-1)

        self.horizontalLayout_5.addWidget(self.label_3)


        self.verticalLayout_5.addWidget(self.frame_5, 0, Qt.AlignTop)

        self.frame_6 = QFrame(self.slideMenu)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.toolBox = QToolBox(self.frame_6)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"background:transparent;\n"
"color:white;\n"
"\n"
"")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 226, 69))
        self.page_3.setStyleSheet(u"QToolBox::tab {\n"
"    color: #000000; /* Default color */\n"
"}\n"
"\n"
"QToolBox::tab:hover {\n"
"    color: #FF0000; /* Hover color */\n"
"}\n"
"")
        self.About = QPushButton(self.page_3)
        self.About.setObjectName(u"About")
        self.About.setGeometry(QRect(0, 0, 221, 23))
        self.About.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #FBF9CE;\n"
"    font-size: 15px;\n"
"    padding: 1px; \n"
"    background-color: rgba(255, 255, 255, 0.1); \n"
"}\n"
"")
        self.About.setFlat(False)
        self.Developers = QPushButton(self.page_3)
        self.Developers.setObjectName(u"Developers")
        self.Developers.setGeometry(QRect(0, 30, 221, 23))
        self.Developers.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #FBF9CE;\n"
"    font-size: 15px;\n"
"    padding: 1px; \n"
"    background-color: rgba(255, 255, 255, 0.1); \n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/home-7-256.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_3, icon, u"Home")
        self.Detection = QWidget()
        self.Detection.setObjectName(u"Detection")
        self.Detection.setGeometry(QRect(0, 0, 226, 69))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Detection.sizePolicy().hasHeightForWidth())
        self.Detection.setSizePolicy(sizePolicy1)
        self.Detection.setAutoFillBackground(False)
        self.New = QPushButton(self.Detection)
        self.New.setObjectName(u"New")
        self.New.setGeometry(QRect(0, 0, 221, 23))
        self.New.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #FBF9CE;\n"
"    font-size: 15px;\n"
"    padding: 1px; \n"
"    background-color: rgba(255, 255, 255, 0.1); \n"
"}\n"
"")
        self.History = QPushButton(self.Detection)
        self.History.setObjectName(u"History")
        self.History.setGeometry(QRect(0, 30, 221, 23))
        self.History.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #FBF9CE;\n"
"    font-size: 15px;\n"
"    padding: 1px; \n"
"    background-color: rgba(255, 255, 255, 0.1); \n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/detective-256.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.Detection, icon1, u"Generate Minutes of the Meeting")

        self.verticalLayout_6.addWidget(self.toolBox, 0, Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.slideMenu)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Settingsbtn = QPushButton(self.frame_7)
        self.Settingsbtn.setObjectName(u"Settingsbtn")
        self.Settingsbtn.setStyleSheet(u"color:rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/settings-24-256.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Settingsbtn.setIcon(icon2)
        self.Settingsbtn.setIconSize(QSize(0, 0))

        self.horizontalLayout_6.addWidget(self.Settingsbtn)


        self.verticalLayout_5.addWidget(self.frame_7)


        self.verticalLayout_2.addWidget(self.slideMenu)


        self.horizontalLayout.addWidget(self.sideMenuContainer)

        self.mainPage = QFrame(self.centralwidget)
        self.mainPage.setObjectName(u"mainPage")
        self.mainPage.setFrameShape(QFrame.StyledPanel)
        self.mainPage.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.mainPage)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.HeaderFrame = QFrame(self.mainPage)
        self.HeaderFrame.setObjectName(u"HeaderFrame")
        self.HeaderFrame.setStyleSheet(u"background-color:#A83547;")
        self.HeaderFrame.setFrameShape(QFrame.StyledPanel)
        self.HeaderFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.HeaderFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.HeaderFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menuList = QPushButton(self.frame_3)
        self.menuList.setObjectName(u"menuList")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/sideMenu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuList.setIcon(icon3)
        self.menuList.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.menuList)


        self.horizontalLayout_2.addWidget(self.frame_3, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_2 = QFrame(self.HeaderFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame = QFrame(self.HeaderFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.frame)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.minimizeBtn)

        self.Expand = QPushButton(self.frame)
        self.Expand.setObjectName(u"Expand")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/layer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Expand.setIcon(icon4)
        self.Expand.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.Expand)

        self.Exit = QPushButton(self.frame)
        self.Exit.setObjectName(u"Exit")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Exit.setIcon(icon5)
        self.Exit.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.Exit)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.HeaderFrame, 0, Qt.AlignTop)

        self.MainBody = QFrame(self.mainPage)
        self.MainBody.setObjectName(u"MainBody")
        sizePolicy.setHeightForWidth(self.MainBody.sizePolicy().hasHeightForWidth())
        self.MainBody.setSizePolicy(sizePolicy)
        self.MainBody.setStyleSheet(u"background:url(:/pages/images/bg.png)")
        self.MainBody.setFrameShape(QFrame.StyledPanel)
        self.MainBody.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.MainBody)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.MainBody)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.aboutPage = QWidget()
        self.aboutPage.setObjectName(u"aboutPage")
        self.verticalLayout_7 = QVBoxLayout(self.aboutPage)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.aboutPage)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setStyleSheet(u"/*background-image: url(:/image/images/about.jpg);\n"
"background-position: center; background-repeat: no-repeat;\n"
"*/")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFrameShadow(QFrame.Plain)
        self.label_4.setPixmap(QPixmap(u"images/FrontPage.png"))
        self.label_4.setScaledContents(True)

        self.verticalLayout_8.addWidget(self.label_4)


        self.verticalLayout_7.addWidget(self.frame_8)

        self.stackedWidget.addWidget(self.aboutPage)
        self.developersPage = QWidget()
        self.developersPage.setObjectName(u"developersPage")
        self.verticalLayout_10 = QVBoxLayout(self.developersPage)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.developersPage)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_9)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u":/pages/images/developerPage.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setWordWrap(False)

        self.verticalLayout_11.addWidget(self.label_5)


        self.verticalLayout_10.addWidget(self.frame_9)

        self.stackedWidget.addWidget(self.developersPage)
        self.newPage = QWidget()
        self.newPage.setObjectName(u"newPage")
        self.verticalLayout_9 = QVBoxLayout(self.newPage)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.newPage)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background:transparent;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_10)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_11 = QFrame(self.frame_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_11, 0, Qt.AlignTop)

        self.frame_14 = QFrame(self.frame_4)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy1.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy1)
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.frame_15, 0, Qt.AlignLeft)

        self.frame_18 = QFrame(self.frame_14)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy1.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy1)
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_18)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_19, 0, Qt.AlignTop)

        self.frame_21 = QFrame(self.frame_18)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_21)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.attachFileLabel = QLabel(self.frame_21)
        self.attachFileLabel.setObjectName(u"attachFileLabel")
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.attachFileLabel.setFont(font)
        self.attachFileLabel.setStyleSheet(u"QLabel{\n"
"color: white\n"
"};")
        self.attachFileLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.attachFileLabel)

        self.uploadBtn = QPushButton(self.frame_21)
        self.uploadBtn.setObjectName(u"uploadBtn")
        self.uploadBtn.setMinimumSize(QSize(200, 30))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.uploadBtn.setFont(font1)
        self.uploadBtn.setStyleSheet(u"  QPushButton {\n"
"                background-color: transparent;\n"
"                color: white;\n"
"                border: 2px solid white;\n"
"                padding: 5px;\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: white;\n"
"                color: black;\n"
"            }")

        self.verticalLayout_13.addWidget(self.uploadBtn)

        self.generateBtn = QPushButton(self.frame_21)
        self.generateBtn.setObjectName(u"generateBtn")
        self.generateBtn.setMinimumSize(QSize(200, 30))
        self.generateBtn.setFont(font1)
        self.generateBtn.setStyleSheet(u"  QPushButton {\n"
"                background-color: transparent;\n"
"                color: white;\n"
"                border: 2px solid white;\n"
"                padding: 5px;\n"
"            }\n"
"\n"
"            QPushButton:hover {\n"
"                background-color: white;\n"
"                color: black;\n"
"            }")

        self.verticalLayout_13.addWidget(self.generateBtn)

        self.exportPDF = QLabel(self.frame_21)
        self.exportPDF.setObjectName(u"exportPDF")
        font2 = QFont()
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(True)
        font2.setWeight(75)
        self.exportPDF.setFont(font2)
        self.exportPDF.setStyleSheet(u" QLabel {\n"
"\n"
"                color: white\n"
"            }\n"
"\n"
" QLabel:hover {\n"
"\n"
"                color: #FFFDD0\n"
"            }")
        self.exportPDF.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.exportPDF)


        self.verticalLayout_12.addWidget(self.frame_21, 0, Qt.AlignVCenter)

        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_20)


        self.horizontalLayout_9.addWidget(self.frame_18, 0, Qt.AlignRight)

        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.frame_16, 0, Qt.AlignRight)


        self.verticalLayout_3.addWidget(self.frame_14)

        self.frame_13 = QFrame(self.frame_4)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_13, 0, Qt.AlignBottom)


        self.horizontalLayout_3.addWidget(self.frame_4)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy1.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy1)
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_12)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_24 = QFrame(self.frame_12)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.verticalLayout_16.addWidget(self.frame_24, 0, Qt.AlignTop)

        self.frame_22 = QFrame(self.frame_12)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy)
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_22)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.fileName = QLabel(self.frame_22)
        self.fileName.setObjectName(u"fileName")
        self.fileName.setFont(font)
        self.fileName.setStyleSheet(u"QLabel{\n"
"color: white\n"
"};")
        self.fileName.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.fileName)

        self.showTxt = QTextEdit(self.frame_22)
        self.showTxt.setObjectName(u"showTxt")
        self.showTxt.setStyleSheet(u"background:white;\n"
"border-radius: 15px;\n"
"")

        self.verticalLayout_17.addWidget(self.showTxt)


        self.verticalLayout_16.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.frame_12)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)

        self.verticalLayout_16.addWidget(self.frame_23, 0, Qt.AlignBottom)


        self.horizontalLayout_3.addWidget(self.frame_12)


        self.verticalLayout_9.addWidget(self.frame_10)

        self.stackedWidget.addWidget(self.newPage)
        self.historyPage = QWidget()
        self.historyPage.setObjectName(u"historyPage")
        self.verticalLayout_14 = QVBoxLayout(self.historyPage)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.historyPage)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.verticalLayout_14.addWidget(self.frame_17)

        self.stackedWidget.addWidget(self.historyPage)
        self.setCoordinate = QWidget()
        self.setCoordinate.setObjectName(u"setCoordinate")
        self.verticalLayout_15 = QVBoxLayout(self.setCoordinate)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.setCoordinate)

        self.horizontalLayout_7.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.MainBody)


        self.horizontalLayout.addWidget(self.mainPage)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText("")
        self.About.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.Developers.setText(QCoreApplication.translate("MainWindow", u"Developers", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"Home", None))
        self.New.setText(QCoreApplication.translate("MainWindow", u"Generate New Minutes", None))
        self.History.setText(QCoreApplication.translate("MainWindow", u"Minutes History", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Detection), QCoreApplication.translate("MainWindow", u"Generate Minutes of the Meeting", None))
        self.Settingsbtn.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.menuList.setText("")
        self.minimizeBtn.setText("")
        self.Expand.setText("")
        self.Exit.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.attachFileLabel.setText(QCoreApplication.translate("MainWindow", u"ATTACH YOUR FILE", None))
        self.uploadBtn.setText(QCoreApplication.translate("MainWindow", u"UPLOAD MP3/MP4", None))
        self.generateBtn.setText(QCoreApplication.translate("MainWindow", u"GENERATE MINUTES", None))
        self.exportPDF.setText(QCoreApplication.translate("MainWindow", u"Export PDF?", None))
        self.fileName.setText("")
    # retranslateUi

