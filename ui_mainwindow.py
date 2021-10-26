# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 621, 81))
        self.labelInput = QLabel(self.groupBox)
        self.labelInput.setObjectName(u"labelInput")
        self.labelInput.setGeometry(QRect(30, 40, 53, 16))
        self.lineInput = QLineEdit(self.groupBox)
        self.lineInput.setObjectName(u"lineInput")
        self.lineInput.setGeometry(QRect(90, 40, 411, 20))
        self.btnExecute = QPushButton(self.groupBox)
        self.btnExecute.setObjectName(u"btnExecute")
        self.btnExecute.setGeometry(QRect(520, 40, 91, 24))
        self.btnExit = QPushButton(self.centralwidget)
        self.btnExit.setObjectName(u"btnExit")
        self.btnExit.setGeometry(QRect(530, 390, 91, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 22))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Group1", None))
        self.labelInput.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.btnExecute.setText(QCoreApplication.translate("MainWindow", u"Execute", None))
        self.btnExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

