# -*- coding: utf-8 -*-

# Dialog implementation generated from reading ui file 'affichagetouspersonne.ui'
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
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.label.setStyleSheet("background-image: url(:/newPrefix/mer800-600.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        """self.texttouspersonne = QtWidgets.QTextEdit(Dialog)
        self.texttouspersonne.setGeometry(QtCore.QRect(10, 80, 781, 511))
        self.texttouspersonne.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.texttouspersonne.setObjectName("texttouspersonne")"""
        #table
        self.table = QTableWidget(Dialog)
        self.table.setGeometry(10 , 65 , 780 , 530)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 20, 500, 31))
        self.label_2.setStyleSheet("font: 8pt \"Nirmala UI\";\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Contenu du dictionnaire personne"))
        self.label_2.setText(_translate("Dialog", "Contenu du dictionnaire personne :"))
   
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
