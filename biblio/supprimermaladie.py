# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'supprimermaladie.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QLineEdit, QTextEdit

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        Dialog.setMinimumSize(QtCore.QSize(800, 600))
        Dialog.setMaximumSize(QtCore.QSize(800, 600))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 611))
        self.label.setStyleSheet("background-image: url(:/newPrefix/mer800-600.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 180, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(310, 380, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(310, 180, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Supprimer une maladie"))
        self.label_2.setText(_translate("Dialog", "Nom Maladie :"))
        self.pushButton.setText(_translate("Dialog", "supprimer"))
        self.comboBox.setItemText(0, _translate("Dialog", " "))
        self.comboBox.setItemText(1, _translate("Dialog", "ASTHME"))
        self.comboBox.setItemText(2, _translate("Dialog", "DIABETE"))
        self.comboBox.setItemText(3, _translate("Dialog", "HYPERTENSION"))
        
    def getbouttonsupprimermaladie(self):
        return self.pushButton        
    def reset_fields(self):
        for widget in   QApplication.activeWindow().findChildren((QLineEdit, QTextEdit)):
            if isinstance(widget, QLineEdit) or isinstance(widget, QTextEdit):
                widget.setText("")      
from photo import photos2



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
