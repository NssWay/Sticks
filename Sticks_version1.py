from PyQt5 import QtWidgets, QtCore, QtGui

class SecondWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GameSticks")

        # Добавляем виджеты на окно
        #label = QtWidgets.QLabel("This is the second window")
        #self.setCentralWidget(label)

# Создаем приложение
app = QtWidgets.QApplication([])

# Создаем и отображаем главное окно
main_window = QtWidgets.QMainWindow()
main_window.setWindowTitle("Main Window")
main_window.resize(800, 600)
main_window.show()

# Запускаем главный цикл приложения
app.exec_()