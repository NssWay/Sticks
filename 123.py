from PyQt5 import QtCore, QtWidgets
from qt_material import apply_stylesheet
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

import sys


class Ui_GameSticks(object):
    def __init__(self):
        self.second_window = None
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
    def __init__(self):
        super().__init__()

        self.win_label = None
        self.turn_label = None
        self.turn_number = None
        self.buttons = None
        self.setWindowTitle("GameSticks")
        self.setupUi()

    def setupUi(self):
        self.buttons = []
        for i in range(15):
            button = QPushButton(" ", self)
            button.setGeometry(30 + 50 * (i % 15), 40 + 80 * (i // 15), 30, 170)
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
        play_button1.setStyleSheet("background-color: red; color: white;")
        play_button1.clicked.connect(lambda: self.hide_buttons(1))

        play_button2 = QPushButton("2", self)
        play_button2.setGeometry(160, 350, 100, 30)
        play_button2.setStyleSheet("background-color: blue; color: white;")
        play_button2.clicked.connect(lambda: self.hide_buttons(2))

        play_button3 = QPushButton("3", self)
        play_button3.setGeometry(280, 350, 100, 30)
        play_button3.setStyleSheet("background-color: green; color: white;")
        play_button3.clicked.connect(lambda: self.hide_buttons(3))

        restart_button = QPushButton("Restart", self)
        restart_button.setGeometry(600, 450, 120, 45)
        restart_button.setStyleSheet("background-color: red; color: white;")
        restart_button.clicked.connect(self.show_popup)

        self.turn_number = 1
        self.turn_label = QLabel(f'  Xод игрока: {self.turn_number}', self)
        self.turn_label.setGeometry(450, 300, 250, 30)
        self.turn_label.setAlignment(Qt.AlignRight)
        self.turn_label.setStyleSheet('font-size: 26px; font-weight: bold;')

    # при использовании данной функции перестает открываться второе окно
    def show_popup(self):
        print('hi')
        popup = QMessageBox()
        popup.setIcon(QMessageBox.Information)
        popup.setWindowTitle("Restart Confirmation")
        popup.setText("Вы уверены, что хотите начать игру заново?")
        popup.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # popup.setDefaultButton(QMessageBox.No)
        returnValue = popup.exec()
        if returnValue == QMessageBox.Yes:
            print('Yes clicked')

        else:
            self.close()
            print('No clicked')

    def hide_buttons(self, num_to_hide):
        if len(self.buttons) > num_to_hide:
            for _ in range(num_to_hide):
                button_to_hide = self.buttons.pop(0)
                button_to_hide.hide()

            if len(self.buttons) == 1:  # Проверяем, что осталась только одна кнопка
                winner_number = 2 if self.turn_number == 1 else 1
                self.win_label = QLabel(f"!!!Игрок {winner_number} выиграл!!!", self)
                self.win_label.setGeometry(250, 400, 300, 200)
                self.win_label.setAlignment(Qt.AlignCenter)
                self.win_label.setStyleSheet('font-size: 26px; font-weight: bold; color: red')
                self.win_label.show()
                self.turn_label.setText("Игра закончена")  # Изменяем текст в turn_label
            else:
                self.turn_number = 2 if self.turn_number == 1 else 1
                self.turn_label.setText(f'Ход игрока: {self.turn_number}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    GameSticks = QMainWindow()
    ui = Ui_GameSticks()
    ui.setupUi(GameSticks)
    apply_stylesheet(app, theme='light_red.xml')
    GameSticks.show()
    sys.exit(app.exec_())

    # добавить кнопку ESC для закрытия приложения
    # при нажатии кнопки ESС переспросить всплывающим окном, уверены что вы хотите выйти
    # Идея: играет музыка, когда убирается палочки из музыки на фоне убирается опр. политра звуков.
    # добавить кнопку перезапука, в сплывающем окне "хотите ли сиграть ещё"
    # если ответ да, то игра начианется заного, если ответ нет, то игра закрывается
    # сделать всё на одном окне
    # ПРИ ДОБАВЛЕНИИ КАКИХ-ЛИБО ДОПОЛНЕНИЙ В ПРОГРАММУ ИЗМЕНЕНИЯ ТАКЖЕ ОТСЛЕЖИВАТЬ В ТЗ.
