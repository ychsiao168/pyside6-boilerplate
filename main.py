#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PySide6 import QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QWidget,
    QMessageBox,
)
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.initTitle(title)
        self.initIcon()
        self.initMenuBar()
        self.initStatusBar()
        self.initGroup1()
        self.ui.btnExit.clicked.connect(self.onExit)


    def initTitle(self, title):
        self.setWindowTitle(title)


    def initIcon(self):
        self.setWindowIcon(QIcon('assets/images/happy.png'))


    def initMenuBar(self):
        self.ui.actionAbout.triggered.connect(self.onHelpAbout)


    def initGroup1(self):
        self.ui.btnExecute.clicked.connect(self.onExecute)


    def initStatusBar(self):
        w = QWidget()
        w.setLayout(QHBoxLayout())

        statusLabel = QLabel('Status Bar Messages')
        statusLabel.setAlignment(QtCore.Qt.AlignHCenter)

        w.layout().addWidget(statusLabel)
        self.ui.statusbar.addWidget(w, 1)


    def onHelpAbout(self):
        QMessageBox.information(self, 'About', f'Hello PySide6')


    def onExecute(self):
        input = self.ui.lineInput.text()
        QMessageBox.information(self, 'Input', f'input:{input}')


    def onExit(self):
        self.close()


if __name__ == "__main__":
    app = QApplication([])

    with open('assets/style/style.qss', 'r') as f:
        _style = f.read()
        app.setStyleSheet(_style)

    window = MainWindow('Hello PySIde6')
    window.show()

    sys.exit(app.exec())
