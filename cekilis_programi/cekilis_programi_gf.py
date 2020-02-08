import random
import sys
import os
from PyQt5.QtWidgets import QWidget, QTextEdit, QLineEdit, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(590, 512)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 0, 151, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(190, 36, 381, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(190, 136, 381, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 180, 151, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(190, 220, 381, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 270, 151, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.textEdit_5 = QtWidgets.QTextEdit(Form)
        self.textEdit_5.setGeometry(QtCore.QRect(190, 270, 381, 111))
        self.textEdit_5.setObjectName("textEdit_5")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 400, 381, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 450, 379, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton_2.clicked.connect(self.yaziyi_temizle)
        self.pushButton_3.clicked.connect(self.cekilis_yap)		

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Çekiliş Programı"))
        self.label.setText(_translate("Form", "Talihli Sayısı:"))
        self.label_2.setText(_translate("Form", "Katılımcıların\n"
"başlangıç değeri:"))
        self.label_3.setText(_translate("Form", "Katılımcıların\n"
"bitiş değeri:"))
        self.label_5.setText(_translate("Form", "Sonuç:"))
        self.pushButton_2.setText(_translate("Form", "Temizle"))
        self.pushButton_3.setText(_translate("Form", "Çekiliş Yap"))

    def yaziyi_temizle(self):
        self.textEdit_5.clear()

    def cekilis_yap(self):
        random_de = set(())
        a = int(self.textEdit.toPlainText())
        b = int(self.textEdit_2.toPlainText())
        c = int(self.textEdit_3.toPlainText())
		
        while (len(random_de) < a):
            random_de.add(random.randrange(b, c))
			
        self.textEdit_5.setText(str(random_de))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

