import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Window1(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Окно 1')
        self.setGeometry(100, 100, 280, 80)

        self.button = QPushButton('Перейти к окну 2', self)
        self.button.clicked.connect(self.open_window2)

    def open_window2(self):
        self.window2 = Window2()
        self.window2.show()
        self.hide()


class Window2(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Окно 2')
        self.setGeometry(100, 100, 280, 80)

        self.button = QPushButton('Вернуться к окну 1', self)
        self.button.clicked.connect(self.open_window1)

    def open_window1(self):
        self.window1 = Window1()
        self.window1.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window1 = Window1()
    window1.show()
    sys.exit(app.exec_())
