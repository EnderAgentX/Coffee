# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win3.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog3(object):
    Coffee_select = "icons/americano.png"

    def setupUi(self, Dialog3):
        Dialog3.setObjectName("Dialog3")
        Dialog3.resize(800, 600)
        Dialog3.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.label = QtWidgets.QLabel(Dialog3)
        self.label.setGeometry(QtCore.QRect(80, 160, 201, 201))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(self.Coffee_select))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.btn_make = QtWidgets.QPushButton(Dialog3)
        self.btn_make.setGeometry(QtCore.QRect(80, 400, 201, 61))
        self.btn_make.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_make.setObjectName("btn_make")
        self.spinBox1 = QtWidgets.QSpinBox(Dialog3)
        self.spinBox1.setGeometry(QtCore.QRect(560, 190, 91, 61))
        self.spinBox1.setMaximum(5)
        self.spinBox1.setObjectName("spinBox1")
        self.spinBox2 = QtWidgets.QSpinBox(Dialog3)
        self.spinBox2.setGeometry(QtCore.QRect(560, 280, 91, 61))
        self.spinBox2.setMinimum(1)
        self.spinBox2.setMaximum(5)
        self.spinBox2.setObjectName("spinBox2")
        self.label_2 = QtWidgets.QLabel(Dialog3)
        self.label_2.setGeometry(QtCore.QRect(390, 210, 141, 31))
        self.label_2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog3)
        self.label_3.setGeometry(QtCore.QRect(390, 290, 141, 31))
        self.label_3.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_syrop = QtWidgets.QLabel(Dialog3)
        self.label_syrop.setGeometry(QtCore.QRect(670, 280, 61, 51))
        self.label_syrop.setText("")
        self.label_syrop.setPixmap(QtGui.QPixmap("icons/caramel.png"))
        self.label_syrop.setScaledContents(True)
        self.label_syrop.setObjectName("label_syrop")

        self.retranslateUi(Dialog3)
        QtCore.QMetaObject.connectSlotsByName(Dialog3)

    def retranslateUi(self, Dialog3):
        _translate = QtCore.QCoreApplication.translate
        Dialog3.setWindowTitle(_translate("Dialog3", "Dialog"))
        self.btn_make.setText(_translate("Dialog3", "Make"))
        self.label_2.setText(_translate("Dialog3", "Сахар:"))
        self.label_3.setText(_translate("Dialog3", "Сироп:"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog3 = QtWidgets.QDialog()
    ui = Ui_Dialog3()
    ui.setupUi(Dialog3)
    Dialog3.show()
    sys.exit(app.exec_())
