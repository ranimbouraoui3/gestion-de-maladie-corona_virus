# -*- coding: utf-8 -*-

# Dialog implementation generated from reading ui file 'affichageparnationalite.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QTableWidget, QTableWidgetItem 


class Ui_Form(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        Dialog.setMinimumSize(QtCore.QSize(800, 600))
        Dialog.setMaximumSize(QtCore.QSize(800, 600))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-4, 0, 811, 601))
        self.label.setStyleSheet("background-image: url(:/newPrefix/mer800-600.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        """self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(40, 340, 721, 231))
        self.textEdit.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.textEdit.setObjectName("textEdit")"""
        #table
        self.table = QTableWidget(Dialog)
        self.table.setGeometry(10 , 335 , 780, 255)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 20, 500, 31))
        self.label_2.setStyleSheet("font: 8pt \"Nirmala UI\";\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(230, 40, 550, 71))
        self.label_2.setStyleSheet("font: 8pt \"Nirmala UI\";\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(380, 180, 311, 31))
        self.lineEdit.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(190, 170, 131, 31))
        self.label_3.setStyleSheet("font: 8pt \"Nirmala UI\";\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(310, 270, 241, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Recherche par nationalité"))
        self.label_2.setText(_translate("Dialog", "Recherche par nationalité"))
        self.label_3.setText(_translate("Dialog", "Nationalité :"))
        self.pushButton.setText(_translate("Dialog", "recherche et affichage"))
    def getbouttonrechaffnat(self):
        return self.pushButton
    def getTable(self):
        return self.table

from photo import photos2


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
