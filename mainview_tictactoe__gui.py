# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainview_tictactoe.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(463, 0)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(150, 110, 181, 141))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"\n"
"background: \"black\";")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 10, 181, 124))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.twoplayer_button = QPushButton(self.gridLayoutWidget)
        self.twoplayer_button.setObjectName(u"twoplayer_button")
        self.twoplayer_button.setStyleSheet(u"color:\"white\";\n"
"font: 700 8pt \"Segoe UI\";\n"
"background: \"black\";")
        self.twoplayer_button.setAutoDefault(False)


        self.gridLayout.addWidget(self.twoplayer_button, 5, 0, 1, 1)

        self.singleplayer_button = QPushButton(self.gridLayoutWidget)
        self.singleplayer_button.setObjectName(u"singleplayer_button")
        self.singleplayer_button.setStyleSheet(u"color:\"white\";\n"
"font: 700 8pt \"Segoe UI\";\n"
"background: \"black\";")

        self.gridLayout.addWidget(self.singleplayer_button, 1, 0, 1, 1)

        self.title1 = QLabel(self.gridLayoutWidget)
        self.title1.setObjectName(u"title1")
        self.title1.setAutoFillBackground(False)
        self.title1.setStyleSheet(u"color:\"white\";\n"
"font: 700 12pt \"Segoe UI\";\n"
"background: \"black\";\n"
"")
        self.title1.setFrameShape(QFrame.Shape.StyledPanel)
        self.title1.setFrameShadow(QFrame.Shadow.Raised)
        self.title1.setLineWidth(2)
        self.title1.setTextFormat(Qt.TextFormat.PlainText)
        self.title1.setScaledContents(False)
        self.title1.setMargin(18)

        self.gridLayout.addWidget(self.title1, 2, 0, 1, 1)

        self.background = QLabel(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(0, 0, 471, 391))
        self.background.setPixmap(QPixmap(u"tictactoemade.png"))
        self.background.setScaledContents(True)
        self.background.setMargin(1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.background.raise_()
        self.frame.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 463, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)

        self.twoplayer_button.setDefault(True)
        self.singleplayer_button.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.twoplayer_button.setText(QCoreApplication.translate("MainWindow", u"Twoplayers", None))
        self.singleplayer_button.setText(QCoreApplication.translate("MainWindow", u"Singleplayer", None))
        self.title1.setText(QCoreApplication.translate("MainWindow", u"Select gamemode", None))
        self.background.setText("")

    # retranslateUi

   