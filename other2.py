from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QSplitter, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication
from qt_material import apply_stylesheet

import sys


class Ui_GameSticks(object):
    def setupUi(self, GameSticks):

        self.label = QLabel()
        font = QFont()
        font.setFamily("Impact")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText("Добро пожаловать в игру Палочки!!!")
        self.label.setStyleSheet('font-size: 26px;'
                                 'font-weight: bold;'
                                 'margin-bottom: 50px;')
