from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont
from qt_material import apply_stylesheet
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont, QPalette, QColor
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

        GameSticks.setObjectName("GameSticks")
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
        self.setWindowTitle("Empty Window")
        self.resize(400, 300)

        button = []
        for i in range(15):
            button = QPushButton("Click Me", self)
            button.setGeometry(120 + 60 * (i % 5), 40 + 70 * (i // 5), 41, 81)
            button.setStyleSheet("background-color: rgb(255, 0, 0)")

    def init(self):
        super().init()

        self.setWindowTitle("Empty Window")
        self.resize(400, 300)

        button = QPushButton("Click Me", self)
        button.setGeometry(150, 100, 100, 30)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    GameSticks = QMainWindow()
    ui = Ui_GameSticks()
    ui.setupUi(GameSticks)
    apply_stylesheet(app, theme='light_red.xml')
    GameSticks.show()
    sys.exit(app.exec_())
