# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'twoplayerview_tictactoe.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox,QDialog, QFrame,
    QLabel, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(473, 423)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"background: 'black'")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 30, 190, 21))
        self.label.setStyleSheet(u"color:\"white\";\n"
"font: 700 12pt \"Segoe UI\";\n"
"background: \"black\";\n"
"")
        self.felt1 = QPushButton(Form)
        self.felt1.setObjectName(u"felt1")
        self.felt1.setGeometry(QRect(80, 90, 91, 81))
        self.felt1.setStyleSheet(u"color:\"white\";\n"
"font: 700 32pt \"Segoe UI\";\n"
"background: \"black\";")
        self.felt2 = QPushButton(Form)
        self.felt2.setObjectName(u"felt2")
        self.felt2.setGeometry(QRect(180, 90, 91, 81))
        self.felt2.setStyleSheet(u"color:\"white\";\n"
"font: 700 32pt \"Segoe UI\";\n"
"background: \"black\";")
        self.felt3 = QPushButton(Form)
        self.felt3.setObjectName(u"felt3")
        self.felt3.setGeometry(QRect(280, 90, 91, 81))
        self.felt3.setStyleSheet(u"color:\"white\";\n"
"font: 700 32pt \"Segoe UI\";\n"
"background: \"black\";")
        self.felt4 = QPushButton(Form)
        self.felt4.setObjectName(u"felt4")
        self.felt4.setGeometry(QRect(80, 180, 91, 81))
        self.felt4.setStyleSheet(u"color:\"white\";\n"
"font: 700 32pt \"Segoe UI\";\n"
"background: \"black\";")
        self.felt5 = QPushButton(Form)
        self.felt5.setObjectName(u"felt5")
        self.felt5.setGeometry(QRect(180, 180, 91, 81))
        self.felt5.setStyleSheet(u"color:\"white\";\n"
"font: 700 32pt \"Segoe UI\";\n"
"background: \"black\";")
        self.felt6 = QPushButton(Form)
        self.felt6.setObjectName(u"felt6")
        self.felt6.setGeometry(QRect(280, 180, 91, 81))
        self.felt6.setStyleSheet(u"color:\"white\";\n"
"font: 700 32pt \"Segoe UI\";\n"
"background: \"black\";")
        self.felt7 = QPushButton(Form)
        self.felt7.setObjectName(u"felt7")
        self.felt7.setGeometry(QRect(80, 270, 91, 91))
        self.felt7.setStyleSheet(u"color:\"white\";\n"
"font: 700 32pt \"Segoe UI\";\n"
"background: \"black\";")
        self.felt8 = QPushButton(Form)
        self.felt8.setObjectName(u"felt8")
        self.felt8.setGeometry(QRect(180, 270, 91, 91))
        self.felt8.setStyleSheet(u"color:\"white\";\n"
"font: 700 32pt \"Segoe UI\";\n"
"background: \"black\";")
        self.felt9 = QPushButton(Form)
        self.felt9.setObjectName(u"felt9")
        self.felt9.setGeometry(QRect(280, 270, 91, 91))
        self.felt9.setStyleSheet(u"color:\"white\";\n"
"font: 700 32pt \"Segoe UI\";\n"
"background: \"black\";")
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(70, 260, 311, 16))
        self.line.setStyleSheet(u"color:\"white\";")
        self.line.setFrameShadow(QFrame.Shadow.Plain)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(70, 170, 301, 16))
        self.line_2.setStyleSheet(u"color:'white'")
        self.line_2.setFrameShadow(QFrame.Shadow.Plain)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(170, 90, 16, 281))
        self.line_3.setStyleSheet(u"color:'white'")
        self.line_3.setFrameShadow(QFrame.Shadow.Plain)
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_4 = QFrame(Form)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(260, 90, 31, 281))
        self.line_4.setStyleSheet(u"color:'white'")
        self.line_4.setFrameShadow(QFrame.Shadow.Plain)
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(210, 380, 210, 16))
        self.label_2.setStyleSheet(u"color:'white'")
        self.dialog_label = QLabel(Form)
        self.dialog_label.setObjectName(u"dialog_label")
        self.dialog_label.setGeometry(QRect(190, 10, 81, 21))
        self.dialog_label.setStyleSheet(u"color:\"white\";\n"
"font: 700 12pt \"Segoe UI\";")
        self.dialog = QDialog()
        self.dialog.setObjectName(u"dialog")
        self.dialog_buttons = QDialogButtonBox(Form)
        self.dialog_buttons.setObjectName(u"dialogbox")
        self.dialog_buttons.setGeometry(QRect(150, 0, 161, 141))
        self.dialog_buttons.setAutoFillBackground(False)
        self.dialog_buttons.hide()
        self.dialog_buttons.setStyleSheet(u"color: 'white'; \n"
"background: 'grey'\n"
"")
        self.dialog_label.setText("Play again?")
        self.dialog_label.hide()

        self.dialog_buttons.setStandardButtons(QDialogButtonBox.StandardButton.No|QDialogButtonBox.StandardButton.Yes)
        self.dialog_buttons.setCenterButtons(True)

        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.label.raise_()
        self.felt1.raise_()
        self.felt2.raise_()
        self.felt3.raise_()
        self.felt4.raise_()
        self.felt5.raise_()
        self.felt6.raise_()
        self.felt7.raise_()
        self.felt8.raise_()
        self.felt9.raise_()
        self.label_2.raise_()
        self.dialog.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Player Begins", None))
        self.felt1.setText("")
        self.felt2.setText("")
        self.felt3.setText("")
        self.felt4.setText("")
        self.felt5.setText("")
        self.felt6.setText("")
        self.felt7.setText("")
        self.felt8.setText("")
        self.felt9.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"score: ", None))
    # retranslateUi

