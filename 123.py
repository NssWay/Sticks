from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont
from qt_material import apply_stylesheet
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer

import sys


class Ui_GameSticks(object):
    def init(self):
        self.centralwidget = None
        self.pushButton_2 = None
        self.pushButton = None
        self.label = None
        self.GameSticks = None
        self.second_window = None

    def setupUi(self, GameSticks):
        self.GameSticks = GameSticks
        self.label = QLabel()
        font = QFont()
        font.setFamily("Impact")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText("Добро пожаловать в игру Палочки!!!")
        self.label.setStyleSheet('font-size: 26px;'
                                 'font-weight: bold;'
                                 'margin-bottom: 50px;')

        self.pushButton = QPushButton()
        self.pushButton.setEnabled(True)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);"
                                      "min-height: 70px;"
                                      "max-width: 300px;"
                                      "min-width: 250px;"
                                      "margin-bottom: 20px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Начать игру")
        self.pushButton.clicked.connect(self.start_game)

        self.pushButton_2 = QPushButton()
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);"
                                        "min-height: 70px;"
                                        "max-width: 300px;"
                                        "min-width: 250px;"
                                        "margin-bottom: 20px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText("Выйти из игры")
        self.pushButton_2.clicked.connect(self.exit_game)

        vbox = QVBoxLayout()
        vbox.addStretch(0)
        vbox.addWidget(self.label, alignment=QtCore.Qt.AlignCenter)
        vbox.addWidget(self.pushButton, alignment=QtCore.Qt.AlignCenter)
        vbox.addWidget(self.pushButton_2, alignment=QtCore.Qt.AlignCenter)
        vbox.addStretch()

        self.centralwidget = QWidget()
        self.centralwidget.setStyleSheet("background-color: rgb(214,244,172)")
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setLayout(vbox)

        GameSticks.setWindowTitle("GameSticks")
        GameSticks.resize(800, 600)
        GameSticks.setCentralWidget(self.centralwidget)

    def start_game(self):
        self.second_window = EmptyWindow()
        self.second_window.setupUi()
        self.second_window.show()
        self.second_window.setStyleSheet("background-color: rgb(214,244,172)")
        self.second_window.move(self.GameSticks.pos())
        self.second_window.resize(800, 600)
        if self.GameSticks:
            self.GameSticks.close()

    def exit_game(self):
        QtWidgets.qApp.quit()
        self.close()

class EmptyWindow(QMainWindow):
    def setupUi(self):
        self.setWindowTitle("GameSticks")
        self.resize(400, 400)

        self.buttons = []
        for i in range(15):
            button = QPushButton("шмяк", self)
            button.setGeometry(40 + 120 * (i % 5), 40 + 80 * (i // 5), 100, 30)
            button.setStyleSheet("background-color: rgb(255, 0, 0)")
            self.buttons.append(button)

        label = QLabel('Выберите количество палочек', self)
        label.setObjectName('label')
        label.setGeometry(20, 300, 400, 30)
        label.setAlignment(Qt.AlignCenter)
        label.show()
        label.setStyleSheet('font-size: 26px; font-weight: bold;')

        play_button1 = QPushButton("1", self)
        play_button1.setGeometry(40, 350, 100, 30)
        play_button1.setStyleSheet("background-color: red; color: white;") #изменить цвет на белый красный
        play_button1.clicked.connect(lambda: self.hide_buttons(1))

        play_button2 = QPushButton("2", self)
        play_button2.setGeometry(160, 350, 100, 30)
        play_button2.setStyleSheet("background-color: blue; color: white;") #изменить цвет на белый красный
        play_button2.clicked.connect(lambda: self.hide_buttons(2))

        play_button3 = QPushButton("3", self)
        play_button3.setGeometry(280, 350, 100, 30)
        play_button3.setStyleSheet("background-color: green; color: white;") #изменить цвет на белый красный
        play_button3.clicked.connect(lambda: self.hide_buttons(3))

    def hide_buttons(self, num_to_hide):
        if len(self.buttons) >= num_to_hide:
            for _ in range(num_to_hide):
                button_to_hide = self.buttons.pop(0)
                button_to_hide.hide()

    def init(self):
        super().init()

        self.setWindowTitle("Empty Window")
        self.resize(400, 400)

        button = QPushButton(" ", self)
        button.setGeometry(150, 100, 100, 30)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    GameSticks = QMainWindow()
    ui = Ui_GameSticks()
    ui.setupUi(GameSticks)
    apply_stylesheet(app, theme='light_red.xml')
    GameSticks.show()
    sys.exit(app.exec_())
