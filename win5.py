# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win5.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog5(object):
    def setupUi(self, Dialog5):
        Dialog5.setObjectName("Dialog5")
        Dialog5.resize(800, 600)
        Dialog5.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.btn_home = QtWidgets.QPushButton(Dialog5)
        self.btn_home.setGeometry(QtCore.QRect(330, 460, 111, 111))
        self.btn_home.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_home.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/home-btn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_home.setIcon(icon)
        self.btn_home.setIconSize(QtCore.QSize(100, 100))
        self.btn_home.setObjectName("btn_home")
        self.label = QtWidgets.QLabel(Dialog5)
        self.label.setGeometry(QtCore.QRect(160, 100, 451, 321))
        self.label.setStyleSheet("font: 15pt \"Stencil\";\n"
"background-color: rgba(255,255,255,40);\n"
"border: 5px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setIndent(-1)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog5)
        QtCore.QMetaObject.connectSlotsByName(Dialog5)

    def retranslateUi(self, Dialog5):
        _translate = QtCore.QCoreApplication.translate
        Dialog5.setWindowTitle(_translate("Dialog5", "Dialog"))
        self.label.setText(_translate("Dialog5", "take your coffee"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog5 = QtWidgets.QDialog()
    ui = Ui_Dialog5()
    ui.setupUi(Dialog5)
    Dialog5.show()
    sys.exit(app.exec_())
