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

        self.pushButton = QPushButton()
        self.pushButton.setEnabled(True)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);"
                                      "min-height: 70px;"
                                      "max-width: 300px;"
                                      "min-width: 250px;"
                                      "margin-bottom: 20px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Начать игру")

#функция по очистке экрана
        def start_game():
            # Очищаем экран
            for child in GameSticks.centralWidget().children():
                child.deleteLater()
            GameSticks.centralWidget().deleteLater()

            # Создаем новое окно
            second_window = QWidget(GameSticks)
            second_window.setStyleSheet("background-color: rgb(214,244,172)")
            GameSticks.setCentralWidget(second_window)

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
        vbox.addStretch(0)  # вертикальное позиционирование
        vbox.addWidget(self.label, alignment=QtCore.Qt.AlignCenter)
        vbox.addWidget(self.pushButton, alignment=QtCore.Qt.AlignCenter)
        vbox.addWidget(self.pushButton_2, alignment=QtCore.Qt.AlignCenter)
        vbox.addStretch()  # вертикальное позиционирование

        self.centralwidget = QWidget()
        self.centralwidget.setStyleSheet("background-color: rgb(214,244,172)")
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setLayout(vbox)

        GameSticks.setObjectName("GameSticks")
        GameSticks.resize(800, 600)
        GameSticks.setCentralWidget(self.centralwidget)

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

    app = QtWidgets.QApplication(sys.argv)
    GameSticks = QtWidgets.QMainWindow()
    ui = Ui_GameSticks()
    ui.setupUi(GameSticks)
    GameSticks.show()
    sys.exit(app.exec_())


sticks = 15
print(sticks)
count = 1
def sum_sticks():
    global sticks
    global count
    if count % 2 == 1:   #подправить условие
        print('Player 1 you need')
    else:
        print('Player 2 you need')
    subtract = int(input('Enter the number from 1 to 3: '))
    print(sticks - subtract)
    sticks = sticks - subtract

    count += 1

game = True
while game:
    if sticks > 1:
        sum_sticks()
    else:
        game = False
        print('Game is over')
        #print(count)
        if count // 2 == 0:
            print('!!!Player 1 win, player 2 lose!!!')
        else:
            print('!!!Player 2 win, player 1 lose!!!')