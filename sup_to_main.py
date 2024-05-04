import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from qt_material import apply_stylesheet


class Ui_GameSticks(object):
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
                                 'margin-bottom: 50px;'
                                 'color: rgb(76,76,76)')

        self.pushButton = QPushButton()
        self.pushButton.setEnabled(True)
        self.pushButton.setStyleSheet("background-color: rgb(149,163,146);"
                                      "min-height: 70px;"
                                      "max-width: 300px;"
                                      "min-width: 250px;"
                                      "margin-bottom: 20px;"
                                      'color: rgb(76,76,76)')
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Начать игру")
        self.pushButton.clicked.connect(self.remove_elements)

        self.pushButton_2 = QPushButton()
        self.pushButton_2.setStyleSheet("background-color: rgb(149,163,146);"
                                        "min-height: 70px;"
                                        "max-width: 300px;"
                                        "min-width: 250px;"
                                        "margin-bottom: 20px;"
                                        "color: rgb(76,76,76)")
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
        self.centralwidget.setStyleSheet("background-color: rgb(182,197,174)")
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setLayout(vbox)

        GameSticks.setWindowTitle("GameSticks")
        GameSticks.resize(800, 600)
        GameSticks.setCentralWidget(self.centralwidget)

        self.select_label = QLabel()
        self.select_label.setText('Выберите количество палочек')
        self.select_label.setObjectName('select_label')
        self.select_label.setGeometry(20, 300, 400, 30)
        self.select_label.setAlignment(Qt.AlignCenter)
        self.select_label.setStyleSheet('font-size: 24px; font-weight: bold; color: rgb(76,76,76)')
        self.select_label.hide()

    def exit_game(self):
        QtWidgets.qApp.quit()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def remove_elements(self):
        self.label.hide()
        self.pushButton.hide()
        self.pushButton_2.hide()
        self.select_label.show()



class EmptyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def clearWindow(self):
        for widget in self.findChildren(QLabel):
            widget.deleteLater()

        label = QLabel('Выберите количество палочек', self)
        label.setObjectName('label')
        label.setGeometry(20, 300, 400, 30)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet('font-size: 24px; font-weight: bold; color: rgb(76,76,76)')
        label.show()

        button_layout = QVBoxLayout()
        for i in range(1, 16):  # Создаем 15 кнопок
            button = QPushButton(f'Button {i}', self)
            button.setStyleSheet("background-color: rgb(149,163,146);"
                                 "min-height: 50px;"
                                 "max-width: 200px;"
                                 "min-width: 150px;"
                                 "margin-bottom: 10px;"
                                 "color: rgb(76,76,76)")
            button.setObjectName(f"button_{i}")
            button.clicked.connect(lambda checked, i=i: print(f'Button {i} was clicked'))
            button_layout.addWidget(button)

        central_widget = QWidget()
        central_widget.setStyleSheet("background-color: rgb(182,197,174)")
        central_widget.setObjectName("centralwidget")
        central_widget.setLayout(button_layout)

        self.setCentralWidget(central_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GameSticks = QMainWindow()
    ui = Ui_GameSticks()
    ui.setupUi(GameSticks)
    apply_stylesheet(app, theme='rgb(152,160,164)')
    GameSticks.show()

    window = EmptyWindow()
    window.clearWindow()

    sys.exit(app.exec_())
