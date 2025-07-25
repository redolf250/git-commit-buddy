# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QStackedWidget, QTextEdit,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1468, 872)
        MainWindow.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1468, 872))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topBar = QFrame(self.centralwidget)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setMaximumSize(QSize(16777215, 50))
        self.topBar.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.topBar.setFrameShape(QFrame.NoFrame)
        self.topBar.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.topBar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.leftTopBar = QFrame(self.topBar)
        self.leftTopBar.setObjectName(u"leftTopBar")
        self.leftTopBar.setMinimumSize(QSize(0, 0))
        self.leftTopBar.setMaximumSize(QSize(16777215, 16777215))
        self.leftTopBar.setFrameShape(QFrame.NoFrame)
        self.leftTopBar.setFrameShadow(QFrame.Plain)
        self.label = QLabel(self.leftTopBar)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(14, 10, 31, 31))
        self.label.setPixmap(QPixmap(u"../resources/assert/github.svg"))
        self.label_2 = QLabel(self.leftTopBar)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 0, 211, 41))
        font = QFont()
        font.setFamilies([u"Baskerville Old Face"])
        font.setPointSize(14)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.leftTopBar)

        self.rightTopBar = QFrame(self.topBar)
        self.rightTopBar.setObjectName(u"rightTopBar")
        self.rightTopBar.setMinimumSize(QSize(120, 0))
        self.rightTopBar.setMaximumSize(QSize(100, 16777215))
        self.rightTopBar.setFrameShape(QFrame.NoFrame)
        self.rightTopBar.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.rightTopBar)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnMinimize = QPushButton(self.rightTopBar)
        self.btnMinimize.setObjectName(u"btnMinimize")
        self.btnMinimize.setMinimumSize(QSize(0, 50))
        self.btnMinimize.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(66, 66, 66);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"../resources/assert/minimize.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnMinimize.setIcon(icon)
        self.btnMinimize.setIconSize(QSize(30, 30))
        self.btnMinimize.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btnMinimize)

        self.btnClose = QPushButton(self.rightTopBar)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setMinimumSize(QSize(0, 50))
        self.btnClose.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../resources/assert/x.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnClose.setIcon(icon1)
        self.btnClose.setIconSize(QSize(30, 30))
        self.btnClose.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btnClose)


        self.horizontalLayout_2.addWidget(self.rightTopBar)


        self.verticalLayout.addWidget(self.topBar)

        self.mainContent = QFrame(self.centralwidget)
        self.mainContent.setObjectName(u"mainContent")
        self.mainContent.setFrameShape(QFrame.NoFrame)
        self.mainContent.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.mainContent)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QFrame(self.mainContent)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(55, 0))
        self.leftMenu.setMaximumSize(QSize(55, 16777215))
        self.leftMenu.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.leftMenu.setFrameShape(QFrame.NoFrame)
        self.leftMenu.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.bottomMenu = QFrame(self.leftMenu)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Plain)
        self.btnSettings = QPushButton(self.bottomMenu)
        self.btnSettings.setObjectName(u"btnSettings")
        self.btnSettings.setGeometry(QRect(0, 760, 55, 60))
        self.btnSettings.setMinimumSize(QSize(0, 60))
        self.btnSettings.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border:none;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"../resources/assert/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSettings.setIcon(icon2)
        self.btnSettings.setIconSize(QSize(30, 30))
        self.btnSettings.setFlat(True)
        self.topMenu = QFrame(self.bottomMenu)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setGeometry(QRect(0, 0, 55, 160))
        self.topMenu.setMinimumSize(QSize(0, 160))
        self.topMenu.setMaximumSize(QSize(16777215, 80))
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.topMenu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btnCommit = QPushButton(self.topMenu)
        self.btnCommit.setObjectName(u"btnCommit")
        self.btnCommit.setMinimumSize(QSize(0, 60))
        self.btnCommit.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid rgb(255,255,255);\n"
"}\n"
"\n"
"\n"
" QPushButton:focus{\n"
"    color: rgb(255, 255, 255);\n"
"    border-left: 2px solid rgb(255,255,255);	\n"
"  }")
        icon3 = QIcon()
        icon3.addFile(u"../resources/assert/git-commit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCommit.setIcon(icon3)
        self.btnCommit.setIconSize(QSize(30, 30))
        self.btnCommit.setFlat(True)

        self.verticalLayout_4.addWidget(self.btnCommit)

        self.btnPullRequest = QPushButton(self.topMenu)
        self.btnPullRequest.setObjectName(u"btnPullRequest")
        self.btnPullRequest.setMinimumSize(QSize(0, 60))
        self.btnPullRequest.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid rgb(255,255,255);\n"
"}\n"
"\n"
"\n"
" QPushButton:focus{\n"
"    color: rgb(255, 255, 255);\n"
"    border-left: 2px solid rgb(255,255,255);	\n"
"  }")
        icon4 = QIcon()
        icon4.addFile(u"../resources/assert/git-pull-request.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPullRequest.setIcon(icon4)
        self.btnPullRequest.setIconSize(QSize(30, 30))
        self.btnPullRequest.setFlat(True)

        self.verticalLayout_4.addWidget(self.btnPullRequest)


        self.verticalLayout_3.addWidget(self.bottomMenu)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.rightContent = QFrame(self.mainContent)
        self.rightContent.setObjectName(u"rightContent")
        self.rightContent.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.rightContent.setFrameShape(QFrame.NoFrame)
        self.rightContent.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.rightContent)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.rightContent)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 800))
        self.stackedWidget.setMaximumSize(QSize(16777215, 800))
        font1 = QFont()
        font1.setFamilies([u"Baskerville Old Face"])
        font1.setPointSize(11)
        self.stackedWidget.setFont(font1)
        self.commitPage = QWidget()
        self.commitPage.setObjectName(u"commitPage")
        self.horizontalLayout_4 = QHBoxLayout(self.commitPage)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.commitPage)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(320, 0))
        self.frame_3.setMaximumSize(QSize(260, 16777215))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.issueKeyLineEdit = QLineEdit(self.frame_3)
        self.issueKeyLineEdit.setObjectName(u"issueKeyLineEdit")
        self.issueKeyLineEdit.setGeometry(QRect(10, 150, 171, 51))
        self.issueKeyLineEdit.setFont(font1)
        self.issueKeyLineEdit.setStyleSheet(u"QLineEdit{\n"
"color: rgb(255, 255, 255);\n"
"padding-left: 5px;\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(255,255,255);	\n"
"}\n"
"")
        self.issueKeyLineEdit.setClearButtonEnabled(True)
        self.projectsComboBox = QComboBox(self.frame_3)
        self.projectsComboBox.setObjectName(u"projectsComboBox")
        self.projectsComboBox.setGeometry(QRect(10, 80, 301, 51))
        self.projectsComboBox.setFont(font)
        self.projectsComboBox.setStyleSheet(u"QComboBox{\n"
"color: rgb(255, 255, 255);\n"
"padding-left: 5px;\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(255,255,255);	\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"        color: white;       /* Dropdown text color */\n"
"        background-color: #333;\n"
"    }")
        self.projectsComboBox.setEditable(False)
        self.projectsComboBox.setPlaceholderText(u"Select Project")
        self.projectsComboBox.setFrame(True)
        self.commitMessageLenghtEdit = QLineEdit(self.frame_3)
        self.commitMessageLenghtEdit.setObjectName(u"commitMessageLenghtEdit")
        self.commitMessageLenghtEdit.setGeometry(QRect(10, 220, 171, 51))
        self.commitMessageLenghtEdit.setFont(font1)
        self.commitMessageLenghtEdit.setToolTipDuration(6)
        self.commitMessageLenghtEdit.setStyleSheet(u"QLineEdit{\n"
"color: rgb(255, 255, 255);\n"
"padding-left: 5px;\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(255,255,255);	\n"
"}\n"
"")
        self.commitMessageLenghtEdit.setClearButtonEnabled(True)
        self.btnBrowse = QPushButton(self.frame_3)
        self.btnBrowse.setObjectName(u"btnBrowse")
        self.btnBrowse.setGeometry(QRect(10, 450, 181, 51))
        font2 = QFont()
        font2.setFamilies([u"Baskerville Old Face"])
        font2.setPointSize(12)
        self.btnBrowse.setFont(font2)
        self.btnBrowse.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border:none;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"../resources/assert/git-branch.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnBrowse.setIcon(icon5)
        self.btnBrowse.setFlat(True)
        self.fileExtentionsTextEdit = QTextEdit(self.frame_3)
        self.fileExtentionsTextEdit.setObjectName(u"fileExtentionsTextEdit")
        self.fileExtentionsTextEdit.setGeometry(QRect(10, 520, 301, 261))
        font3 = QFont()
        font3.setFamilies([u"Baskerville Old Face"])
        font3.setPointSize(15)
        self.fileExtentionsTextEdit.setFont(font3)
        self.fileExtentionsTextEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(255,255,255);	")
        self.fileExtentionsTextEdit.setFrameShape(QFrame.NoFrame)
        self.fileExtentionsTextEdit.setFrameShadow(QFrame.Plain)
        self.btnSaveProjectConfiguration = QPushButton(self.frame_3)
        self.btnSaveProjectConfiguration.setObjectName(u"btnSaveProjectConfiguration")
        self.btnSaveProjectConfiguration.setGeometry(QRect(200, 450, 111, 51))
        self.btnSaveProjectConfiguration.setFont(font2)
        self.btnSaveProjectConfiguration.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border:none;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"../resources/assert/save.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSaveProjectConfiguration.setIcon(icon6)
        self.btnSaveProjectConfiguration.setIconSize(QSize(20, 20))
        self.btnSaveProjectConfiguration.setFlat(True)
        self.projectKey = QLineEdit(self.frame_3)
        self.projectKey.setObjectName(u"projectKey")
        self.projectKey.setGeometry(QRect(10, 380, 301, 51))
        self.projectKey.setFont(font1)
        self.projectKey.setToolTipDuration(6)
        self.projectKey.setStyleSheet(u"QLineEdit{\n"
"color: rgb(255, 255, 255);\n"
"padding-left: 5px;\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(255,255,255);	\n"
"}\n"
"")
        self.projectKey.setClearButtonEnabled(True)
        self.btnGenerateCommit = QPushButton(self.frame_3)
        self.btnGenerateCommit.setObjectName(u"btnGenerateCommit")
        self.btnGenerateCommit.setGeometry(QRect(190, 290, 121, 51))
        self.btnGenerateCommit.setFont(font2)
        self.btnGenerateCommit.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border:none;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"../resources/assert/sliders.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnGenerateCommit.setIcon(icon7)
        self.btnGenerateCommit.setIconSize(QSize(16, 16))
        self.btnGenerateCommit.setFlat(True)
        self.btnRemoveProject = QPushButton(self.frame_3)
        self.btnRemoveProject.setObjectName(u"btnRemoveProject")
        self.btnRemoveProject.setGeometry(QRect(190, 150, 121, 51))
        self.btnRemoveProject.setFont(font2)
        self.btnRemoveProject.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border:none;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"../resources/assert/minus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnRemoveProject.setIcon(icon8)
        self.btnRemoveProject.setFlat(True)
        self.btnResetTextEdit = QPushButton(self.frame_3)
        self.btnResetTextEdit.setObjectName(u"btnResetTextEdit")
        self.btnResetTextEdit.setGeometry(QRect(190, 220, 121, 51))
        self.btnResetTextEdit.setFont(font2)
        self.btnResetTextEdit.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border:none;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"../resources/assert/refresh-ccw.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnResetTextEdit.setIcon(icon9)
        self.btnResetTextEdit.setFlat(True)
        self.llmModels = QComboBox(self.frame_3)
        self.llmModels.setObjectName(u"llmModels")
        self.llmModels.setGeometry(QRect(10, 10, 301, 51))
        self.llmModels.setFont(font)
        self.llmModels.setStyleSheet(u"QComboBox{\n"
"color: rgb(255, 255, 255);\n"
"padding-left: 5px;\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(255,255,255);	\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"        color: white;       /* Dropdown text color */\n"
"        background-color: #333;\n"
"    }")
        self.llmModels.setEditable(False)
        self.llmModels.setPlaceholderText(u"Select Project")
        self.llmModels.setFrame(True)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 290, 171, 51))
        self.label_3.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border:none;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLabel:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.toggleTracking = QRadioButton(self.frame_3)
        self.toggleTracking.setObjectName(u"toggleTracking")
        self.toggleTracking.setGeometry(QRect(20, 290, 151, 51))
        self.toggleTracking.setFont(font2)
        self.toggleTracking.setStyleSheet(u"QRadioButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border:none;\n"
"	border-radius: 5px;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"../resources/assert/file.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toggleTracking.setIcon(icon10)
        self.label_3.raise_()
        self.issueKeyLineEdit.raise_()
        self.projectsComboBox.raise_()
        self.commitMessageLenghtEdit.raise_()
        self.btnBrowse.raise_()
        self.fileExtentionsTextEdit.raise_()
        self.btnSaveProjectConfiguration.raise_()
        self.projectKey.raise_()
        self.btnGenerateCommit.raise_()
        self.btnRemoveProject.raise_()
        self.btnResetTextEdit.raise_()
        self.llmModels.raise_()
        self.toggleTracking.raise_()

        self.horizontalLayout_4.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.commitPage)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.projectPath = QLabel(self.frame_4)
        self.projectPath.setObjectName(u"projectPath")
        self.projectPath.setMinimumSize(QSize(0, 50))
        self.projectPath.setFont(font1)
        self.projectPath.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(66, 66, 66);\n"
"padding-left: 2px;\n"
"border-radius: 5px;")
        self.projectPath.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.projectPath)

        self.textEdit = QTextEdit(self.frame_4)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFont(font1)
        self.textEdit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setFrameShadow(QFrame.Plain)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.textEdit)


        self.horizontalLayout_4.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.commitPage)
        self.pullRequestPage = QWidget()
        self.pullRequestPage.setObjectName(u"pullRequestPage")
        self.verticalLayout_7 = QVBoxLayout(self.pullRequestPage)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.pullRequestPage)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 60))
        self.frame_5.setMaximumSize(QSize(16777215, 65))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.projectPathPullRequest = QLabel(self.frame_5)
        self.projectPathPullRequest.setObjectName(u"projectPathPullRequest")
        self.projectPathPullRequest.setGeometry(QRect(230, 10, 1171, 50))
        self.projectPathPullRequest.setMinimumSize(QSize(0, 50))
        self.projectPathPullRequest.setFont(font1)
        self.projectPathPullRequest.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(66, 66, 66);\n"
"padding-left: 2px;\n"
"border-radius: 5px;")
        self.projectPathPullRequest.setAlignment(Qt.AlignCenter)
        self.btnGeneratePullRequest = QPushButton(self.frame_5)
        self.btnGeneratePullRequest.setObjectName(u"btnGeneratePullRequest")
        self.btnGeneratePullRequest.setGeometry(QRect(20, 10, 201, 51))
        self.btnGeneratePullRequest.setFont(font2)
        self.btnGeneratePullRequest.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border:none;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u"../resources/assert/send.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnGeneratePullRequest.setIcon(icon11)
        self.btnGeneratePullRequest.setIconSize(QSize(16, 16))
        self.btnGeneratePullRequest.setFlat(True)

        self.verticalLayout_7.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.pullRequestPage)
        self.frame_6.setObjectName(u"frame_6")
        font4 = QFont()
        font4.setFamilies([u"Baskerville Old Face"])
        font4.setPointSize(10)
        self.frame_6.setFont(font4)
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Plain)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pullTextEdit = QTextEdit(self.frame_6)
        self.pullTextEdit.setObjectName(u"pullTextEdit")
        font5 = QFont()
        font5.setFamilies([u"Baskerville Old Face"])
        font5.setPointSize(14)
        self.pullTextEdit.setFont(font5)
        self.pullTextEdit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pullTextEdit.setFrameShape(QFrame.NoFrame)
        self.pullTextEdit.setFrameShadow(QFrame.Plain)
        self.pullTextEdit.setReadOnly(True)

        self.verticalLayout_8.addWidget(self.pullTextEdit)


        self.verticalLayout_7.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.pullRequestPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.stackedWidget.addWidget(self.settingsPage)
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.stackedWidget.addWidget(self.homePage)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.rightContent)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 40))
        self.frame_2.setMaximumSize(QSize(16777215, 25))
        self.frame_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.gitVersion = QLabel(self.frame_2)
        self.gitVersion.setObjectName(u"gitVersion")
        self.gitVersion.setGeometry(QRect(330, 10, 381, 31))
        font6 = QFont()
        font6.setFamilies([u"Bahnschrift SemiBold"])
        font6.setPointSize(8)
        font6.setBold(True)
        self.gitVersion.setFont(font6)
        self.gitVersion.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.gitVersion.setAlignment(Qt.AlignCenter)
        self.ollamaVersion = QLabel(self.frame_2)
        self.ollamaVersion.setObjectName(u"ollamaVersion")
        self.ollamaVersion.setGeometry(QRect(750, 10, 381, 31))
        self.ollamaVersion.setFont(font6)
        self.ollamaVersion.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.ollamaVersion.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.rightContent)


        self.verticalLayout.addWidget(self.mainContent)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"GitCommitBuddy", None))
#if QT_CONFIG(tooltip)
        self.btnMinimize.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btnMinimize.setText("")
#if QT_CONFIG(tooltip)
        self.btnClose.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btnClose.setText("")
        self.btnSettings.setText("")
        self.btnCommit.setText("")
        self.btnPullRequest.setText("")
        self.issueKeyLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Issue Key (Optional)", None))
#if QT_CONFIG(tooltip)
        self.commitMessageLenghtEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.commitMessageLenghtEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Message Length ", None))
        self.btnBrowse.setText(QCoreApplication.translate("MainWindow", u"New Repository", None))
        self.fileExtentionsTextEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Baskerville Old Face'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>", None))
        self.fileExtentionsTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter file extentions here, should be comma seperated. eg c,cpp and etc", None))
        self.btnSaveProjectConfiguration.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(tooltip)
        self.projectKey.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.projectKey.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Project Key (Unique)", None))
        self.btnGenerateCommit.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.btnRemoveProject.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.btnResetTextEdit.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label_3.setText("")
        self.toggleTracking.setText(QCoreApplication.translate("MainWindow", u"Track Files", None))
        self.projectPath.setText(QCoreApplication.translate("MainWindow", u"Project Path", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Baskerville Old Face'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>", None))
        self.projectPathPullRequest.setText(QCoreApplication.translate("MainWindow", u"Project Path", None))
        self.btnGeneratePullRequest.setText(QCoreApplication.translate("MainWindow", u"Generate ", None))
        self.gitVersion.setText("")
        self.ollamaVersion.setText("")
    # retranslateUi

