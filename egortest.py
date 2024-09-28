import sys
import random

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout


class StartMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel()
        font = QFont()
        font.setFamily('Impact')
        self.label.setFont(font)
        self.label.setObjectName('label')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText('Добро пожаловать в игру\nПалочки!!!')
        self.label.setStyleSheet('font-size: 35px;'
                                 'background: #00000000;'
                                 'color: #000000;'
                                 'margin-bottom: 50px;')

        self.pushButton = QPushButton()
        self.pushButton.setEnabled(True)
        self.pushButton.setStyleSheet('background: #2f68c8ed;'
                                      'min-height: 70px;'
                                      'max-width: 300px;'
                                      'min-width: 250px;'
                                      'margin-bottom: 20px;'
                                      'font-size: 20px;'
                                      'color: #000000;'
                                      'border: 2px solid #000000 ')
        self.pushButton.setObjectName('pushButton')
        self.pushButton.setText('Начать игру')
        self.pushButton.clicked.connect(self.start_game)

        self.pushButton_2 = QPushButton()
        self.pushButton_2.setStyleSheet('background: #3e68afcc;'
                                        'min-height: 70px;'
                                        'max-width: 300px;'
                                        'min-width: 250px;'
                                        'margin-bottom: 20px;'
                                        'font-size: 20px;'
                                        'color: #000000;'
                                        'border: 2px solid #000000 ')
        self.pushButton_2.setObjectName('pushButton_2')
        self.pushButton_2.setText('Выйти из игры')
        self.pushButton_2.clicked.connect(self.exit_game)

        vbox = QVBoxLayout()
        vbox.addStretch(0)
        vbox.addWidget(self.label, alignment=QtCore.Qt.AlignCenter)
        vbox.addWidget(self.pushButton, alignment=QtCore.Qt.AlignCenter)
        vbox.addWidget(self.pushButton_2, alignment=QtCore.Qt.AlignCenter)
        vbox.addStretch()

        self.centralwidget = QWidget()
        self.centralwidget.setObjectName('centralwidget')
        self.centralwidget.setLayout(vbox)
        images = ["pictures/StartWindow1.jpg", "pictures/StartWindow2.jpg", "pictures/StartWindow3.jpg",
                  "pictures/StartWindow4.jpg", "pictures/StartWindow5.jpg"]
        random_image = random.choice(images)
        self.centralwidget.setStyleSheet('background-image: url("{}"); '
                                         'background-repeat: no-repeat; '
                                         'background-position: center;'.format(random_image))

        self.setWindowTitle('GameSticks')
        self.resize(800, 600)
        self.setCentralWidget(self.centralwidget)

    def start_game(self):
        self.second_window = GameZone()
        self.second_window.show()
        self.second_window.setStyleSheet('background-color: rgb(182,197,174)')
        self.second_window.move(self.pos())
        self.second_window.resize(800, 600)
        self.close()

    def exit_game(self):
        self.close()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

class GameZone(QMainWindow):

    def __init__(self):
        super().__init__()
        self.wind = None
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName('centralwidget')
        self.setCentralWidget(self.centralwidget)
        vbox = QVBoxLayout()
        self.centralwidget.setLayout(vbox)
        self.setFixedSize(800, 600)


        images = ["pictures/StartWindow1.jpg", "pictures/StartWindow2.jpg", "pictures/StartWindow3.jpg",
                  "pictures/StartWindow4.jpg", "pictures/StartWindow5.jpg"]
        random_image = random.choice(images)

        self.centralwidget.setStyleSheet('background-image: url("{}"); '
                                         'background-repeat: no-repeat; '
                                         'background-position: center;'.format(random_image))

        self.win_label = None
        self.turn_label = None
        self.turn_number = None
        self.buttons = None
        self.setWindowTitle('GameSticks')

        self.buttons = []
        for i in range(15):
            button = QPushButton(' ', self)
            button.setGeometry(30 + 50 * (i % 15), 40 + 80 * (i // 15), 30, 170)
            button.setStyleSheet("QPushButton {border: none; margin : 0px; padding: 0px; border-image: url(pictures/stick.png);}")
            button.show()
            self.buttons.append(button)

        label = QLabel('Выберите количество палочек', self)
        label.setObjectName('label')
        label.setGeometry(20, 300, 400, 30)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet('background: transparent;'
                            'font-size: 26px;'
                            'font-weight: bold;'
                            'font-size: 24px;'
                            'color: #000000;'
                            'font-weight: bold;')
        label.show()

        play_button1 = QPushButton('1', self)
        play_button1.setGeometry(40, 350, 100, 30)
        play_button1.setStyleSheet('background: #3e68afcc;'
                                   'min-height: 30px;'
                                   'max-width: 100px;'
                                   'min-width: 100px;'
                                   'margin-bottom: 20px;'
                                   'font-size: 20px;'
                                   'color: #000000;'
                                   'border: 2px solid #000000 ')
        play_button1.clicked.connect(lambda: self.hide_buttons(1))

        play_button2 = QPushButton('2', self)
        play_button2.setGeometry(160, 350, 100, 30)
        play_button2.setStyleSheet('background: #3e68afcc;'
                                   'min-height: 30px;'
                                   'max-width: 100px;'
                                   'min-width: 100px;'
                                   'margin-bottom: 20px;'
                                   'font-size: 20px;'
                                   'color: #000000;'
                                   'border: 2px solid #000000 ')
        play_button2.clicked.connect(lambda: self.hide_buttons(2))

        play_button3 = QPushButton('3', self)
        play_button3.setGeometry(280, 350, 100, 30)
        play_button3.setStyleSheet('background: #3e68afcc;'
                                   'min-height: 30px;'
                                   'max-width: 100px;'
                                   'min-width: 100px;'
                                   'margin-bottom: 20px;'
                                   'font-size: 20px;'
                                   'color: #000000;'
                                   'border: 2px solid #000000 ')
        play_button3.clicked.connect(lambda: self.hide_buttons(3))

        restart_button = QPushButton('Restart', self)
        restart_button.setGeometry(600, 450, 120, 45)
        restart_button.setStyleSheet('background: #3e68afcc;'
                                     'min-height: 30px;'
                                     'max-width: 100px;'
                                     'min-width: 100px;'
                                     'margin-bottom: 20px;'
                                     'font-size: 20px;'
                                     'color: #000000;'
                                     'border: 2px solid #000000 ')
        restart_button.clicked.connect(self.restart_game)

        self.turn_number = 1
        self.turn_label = QLabel(f'  Xод игрока: {self.turn_number}', self)
        self.turn_label.setGeometry(450, 300, 250, 30)
        self.turn_label.setAlignment(Qt.AlignRight)
        self.turn_label.setStyleSheet('background: transparent;'
                                      'min-height: 30px;'
                                      'margin-bottom: 20px;'
                                      'font-size: 26px;'
                                      'font-weight: bold;'
                                      'font-size: 20px;'
                                      'color: #000000;')

    def restart_game(self):
        self.wind = GameZone()
        self.wind.show()
        self.close()



    def hide_buttons(self, num_to_hide):
        if len(self.buttons) > num_to_hide:
            for _ in range(num_to_hide):
                button_to_hide = self.buttons.pop(0)
                button_to_hide.hide()

            if len(self.buttons) == 1:
                winner_number = 2 if self.turn_number == 1 else 1
                self.win_label = QLabel(f'!!!Игрок {winner_number} выиграл!!!', self)
                self.win_label.setGeometry(250, 400, 300, 200)
                self.win_label.setAlignment(Qt.AlignCenter)
                self.win_label.setStyleSheet('background-color: rgba(0, 0, 0, 0);' 
                                             'font-size: 26px; font-weight: bold; color: rgb(0,0,0)')
                self.win_label.show()
                self.turn_label.setText('Игра закончена')
            else:
                self.turn_number = 2 if self.turn_number == 1 else 1
                self.turn_label.setText(f'Ход игрока: {self.turn_number}')

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GameSticks = StartMenu()
    #apply_stylesheet(app, theme='default')
    GameSticks.show()
    sys.exit(app.exec_())
