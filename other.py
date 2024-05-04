import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from qt_material import apply_stylesheet


class Ui_GameSticks(object):
    def setupUi(self, GameSticks):
        self.GameSticks = GameSticks

        self.label = QtWidgets.QLabel()
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

        vbox = QtWidgets.QVBoxLayout()
        vbox.addStretch(0)
        vbox.addWidget(self.label, alignment=QtCore.Qt.AlignCenter)
        vbox.addWidget(self.pushButton, alignment=QtCore.Qt.AlignCenter)
        vbox.addWidget(self.pushButton_2, alignment=QtCore.Qt.AlignCenter)
        vbox.addStretch()

        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setStyleSheet("background-color: rgb(182,197,174)")
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setLayout(vbox)

        GameSticks.setWindowTitle("GameSticks")
        GameSticks.resize(800, 600)
        GameSticks.setCentralWidget(self.centralwidget)

    def exit_game(self):
        QtWidgets.qApp.quit()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def remove_elements(self):
        self.label.deleteLater()
        self.pushButton.deleteLater()
        self.pushButton_2.deleteLater()
        print('clear')  # удалить потом
        self.init_empty_window()

    def init_empty_window(self):
        empty_window = EmptyWindow()
        empty_window.show()


class EmptyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: rgb(182,197,174)")
        self.setFixedSize(800, 600)

        self.buttons = []
        for i in range(15):
            button = QPushButton(" ", self)
            button.setGeometry(30 + 50 * (i % 15), 40 + 80 * (i // 15), 30, 170)
        print('инициализация')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    GameSticks = QMainWindow()
    ui = Ui_GameSticks()
    ui.setupUi(GameSticks)
    apply_stylesheet(app, theme='rgb(152,160,164)')
    GameSticks.show()
    sys.exit(app.exec_())
