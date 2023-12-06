import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer

from coffee import Ui_MainWindow
from win2 import Ui_Dialog
from win3 import Ui_Dialog3
from win4 import Ui_Dialog4
from win5 import Ui_Dialog5




class Coffee(QMainWindow):
    def __init__(self):

        super(Coffee, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.timer = QTimer(self)
        self.timer.setInterval(25)
        self.timer.timeout.connect(self.plus)
        self.progress = 0





        self.ui.btn_start.clicked.connect(self.openWindow2)


    def plus(self):
        if self.progress == 0:
            self.new_window = QtWidgets.QDialog()
            self.ui_window = Ui_Dialog4()
            self.ui_window.setupUi(self.new_window)
            self.new_window.show()

        self.progress += 1
        self.ui_window.progressBar.setValue(self.progress)
        if self.progress == 100:
            self.timer.stop()
            self.openWindow5()
            self.progress = 0

    def openWindow2(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        self.close()
        self.ui_window.btn_end.clicked.connect(self.openWindow1)
        self.ui_window.btn_coffee_1.clicked.connect(self.openWindow3_1)
        self.ui_window.btn_coffee_2.clicked.connect(self.openWindow3_2)
        self.ui_window.btn_coffee_3.clicked.connect(self.openWindow3_3)
        self.ui_window.btn_coffee_4.clicked.connect(self.openWindow3_4)
        self.ui_window.btn_coffee_5.clicked.connect(self.openWindow3_5)
        self.ui_window.btn_coffee_6.clicked.connect(self.openWindow3_6)
        self.ui_window.btn_coffee_7.clicked.connect(self.openWindow3_7)
        self.ui_window.btn_coffee_8.clicked.connect(self.openWindow3_8)
        self.ui_window.btn_coffee_9.clicked.connect(self.openWindow3_9)
        self.ui_window.btn_coffee_10.clicked.connect(self.openWindow3_10)
        self.ui_window.btn_coffee_11.clicked.connect(self.openWindow3_11)
        self.ui_window.btn_coffee_12.clicked.connect(self.openWindow3_12)


    def openWindow5(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog5()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        self.ui_window.btn_home.clicked.connect(self.openWindow1)

    def openWindow4(self):
        self.timer.start()



    def openWindow3_1(self):
        self.new_window.close()
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog3()
        self.ui_window.Coffee_select = "icons/espresso.png"
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        self.ui_window.btn_make.clicked.connect(self.openWindow4)
        print(self.ui_window.spinBox1.text())
        self.ui_window.Syrop_select = "icons/espresso.png"
        #self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/espresso.png"))


        def change():
            print(self.ui_window.spinBox2.text())
            if self.ui_window.spinBox2.text() == "0":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/espresso.png"))
            elif  self.ui_window.spinBox2.text() == "1":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/americano.png"))
            elif  self.ui_window.spinBox2.text() == "2":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/raf.png"))
            elif  self.ui_window.spinBox2.text() == "3":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/viennese_coffee.png"))
            elif  self.ui_window.spinBox2.text() == "4":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/cocoa.png"))



        self.ui_window.spinBox2.valueChanged.connect(change)







    def openWindow3_2(self):
        self.new_window.close()
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog3()
        self.ui_window.Coffee_select = "icons/espresso.png"
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        self.ui_window.btn_make.clicked.connect(self.openWindow4)

    def openWindow3_3(self):
        self.new_window.close()
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog3()
        self.ui_window.Coffee_select = "icons/americano.png"
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        self.ui_window.btn_make.clicked.connect(self.openWindow4)

    def openWindow3_4(self):
        self.new_window.close()
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog3()
        self.ui_window.Coffee_select = "icons/macchiato.png"
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        self.ui_window.btn_make.clicked.connect(self.openWindow4)

    def openWindow3_5(self):
        self.new_window.close()
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog3()
        self.ui_window.Coffee_select = "icons/latte.png"
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        self.ui_window.btn_make.clicked.connect(self.openWindow4)

    def openWindow3_6(self):
        self.new_window.close()
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog3()
        self.ui_window.Coffee_select = "icons/moccachino.png"
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        self.ui_window.btn_make.clicked.connect(self.openWindow4)

    def openWindow3_7(self):
        self.new_window.close()
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog3()
        self.ui_window.Coffee_select = "icons/raf.png"
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        self.ui_window.btn_make.clicked.connect(self.openWindow4)

    def openWindow3_8(self):
        self.new_window.close()
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog3()
        self.ui_window.Coffee_select = "icons/cappuccino.png"
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        self.ui_window.btn_make.clicked.connect(self.openWindow4)

    def openWindow3_9(self):
        self.new_window.close()
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog3()
        self.ui_window.Coffee_select = "icons/glasse.png"
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        self.ui_window.btn_make.clicked.connect(self.openWindow4)

    def openWindow3_10(self):
        self.new_window.close()
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog3()
        self.ui_window.Coffee_select = "icons/viennese_coffee.png"
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        self.ui_window.btn_make.clicked.connect(self.openWindow4)

    def openWindow3_11(self):
        self.new_window.close()
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog3()
        self.ui_window.Coffee_select = "icons/hot_chocolate.png"
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        self.ui_window.btn_make.clicked.connect(self.openWindow4)

    def openWindow3_12(self):
        self.new_window.close()
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog3()
        self.ui_window.Coffee_select = "icons/cocoa.png"
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        self.ui_window.btn_make.clicked.connect(self.openWindow4)

    def openWindow1(self):
        self.show()
        self.new_window.close()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Coffee()
    window.show()
    sys.exit(app.exec())

