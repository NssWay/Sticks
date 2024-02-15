from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont
from qt_material import apply_stylesheet
import sys


class Ui_GameSticks(object):
    def __init__(self):
        self.vbox = None
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

        self.vbox = QVBoxLayout()
        self.vbox.addStretch(0)
        self.vbox.addWidget(self.label, alignment=QtCore.Qt.AlignCenter)
        self.vbox.addWidget(self.pushButton, alignment=QtCore.Qt.AlignCenter)
        self.vbox.addWidget(self.pushButton_2, alignment=QtCore.Qt.AlignCenter)
        self.vbox.addStretch()

        self.centralwidget = QWidget()
        self.centralwidget.setStyleSheet("background-color: rgb(214,244,172)")
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setLayout(self.vbox)

        GameSticks.setObjectName("GameSticks")
        GameSticks.resize(800, 600)
        GameSticks.setCentralWidget(self.centralwidget)

    def start_game(self):
        # self.second_window = QMainWindow()
        # self.second_window.show()
        # self.second_window.resize(800, 600)
        item = self.vbox.itemAt(0)
        self.vbox.removeItem(item)
        self.vbox.addWidget(self.label)
        #завернут в лэйаут и уничтожить виджеты

    def exit_game(self):
        QtWidgets.qApp.quit()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    GameSticks = QMainWindow()
    ui = Ui_GameSticks()
    ui.setupUi(GameSticks)
    apply_stylesheet(app, theme='light_red.xml')
    GameSticks.show()
    sys.exit(app.exec_())

# sticks = 15
# print(sticks)
# count = 1
#
#
# def sum_sticks():
#     global sticks
#     global count
#     if count % 2 == 1:  # подправить условие
#         print('Player 1 you need')
#     else:
#         print('Player 2 you need')
#     subtract = int(input('Enter the number from 1 to 3: '))
#     print(sticks - subtract)
#     sticks = sticks - subtract
#
#     count += 1
#
#
# game = True
# while game:
#     if sticks > 1:
#         sum_sticks()
#     else:
#         game = False
#         print('Game is over')
#         # print(count)
#         if count // 2 == 0:
#             print('!!!Player 1 win, player 2 lose!!!')
#         else:
#             print('!!!Player 2 win, player 1 lose!!!')