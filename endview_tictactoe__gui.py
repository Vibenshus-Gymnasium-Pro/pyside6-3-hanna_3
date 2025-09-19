# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'endview_tictactoe.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(467, 430)
        Form.setStyleSheet(u"background: 'black'")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 90, 81, 20))
        self.label.setStyleSheet(u"color:'white'")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(140, 120, 75, 24))
        self.pushButton.setStyleSheet(u"color:'white'")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(230, 120, 75, 24))
        self.pushButton_2.setStyleSheet(u"color:'white'")

        self.retranslateUi(Form)

        self.pushButton.setDefault(True)
        self.pushButton_2.setDefault(True)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Play Again?", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"yes", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"no", None))
    # retranslateUi

