from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


def showDialog():
    msg_box = Q
    msg_box.setWindowTitle('Диалоговое окно')
    msg_box.setText('Это пример диалогового окна')
    msg_box.exec_()


if __name__ == '__main__':
    app = QApplication([])

    window = QWidget()
    window.setGeometry(100, 100, 300, 200)
    window.setWindowTitle('Пример окна с кнопкой')

    button = QPushButton('Показать диалог', window)
    button.clicked.connect(showDialog)

    window.show()

    app.exec_()
