# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win4.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog4(object):
    def setupUi(self, Dialog4):
        Dialog4.setObjectName("Dialog4")
        Dialog4.resize(800, 600)
        Dialog4.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.progressBar = QtWidgets.QProgressBar(Dialog4)
        self.progressBar.setGeometry(QtCore.QRect(200, 210, 441, 131))
        self.progressBar.setStyleSheet("font: 15pt \"Stencil\";")
        self.progressBar.setProperty("value", 50)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Dialog4)
        QtCore.QMetaObject.connectSlotsByName(Dialog4)

    def retranslateUi(self, Dialog4):
        _translate = QtCore.QCoreApplication.translate
        Dialog4.setWindowTitle(_translate("Dialog4", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog4 = QtWidgets.QDialog()
    ui = Ui_Dialog4()
    ui.setupUi(Dialog4)
    Dialog4.show()
    sys.exit(app.exec_())
