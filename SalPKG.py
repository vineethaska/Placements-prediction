
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SalPKG(object):

    def salinfo(self,ts):

        if(int(ts)<=60):

            self.salpkg.setText(" 3 to 6 package")
            cmpny="Inforsis\n\n"+"Wipro\n\n"+"CT\n"
            self.cmlist.setText(cmpny)

        elif (int(ts) > 60 and int(ts) <= 75 ):
            self.salpkg.setText(" 6 to 9 package")
            cmpny = "ValueLab\n\n"+ "Oracle"
            self.cmlist.setText(cmpny)

        elif (int(ts) > 76 and int(ts) <= 90):
            self.salpkg.setText(" 9 to 12 package")
            cmpny = "TCS\n\n" + "Dell\n\n" + "CS"
            self.cmlist.setText(cmpny)
        else:

            self.salpkg.setText("12+ package")
            cmpny = "Capgemini\n\n" + "HCL\n\n" +"IBM"
            self.cmlist.setText(cmpny)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(543, 597)
        Dialog.setStyleSheet("background-color: rgb(220,220,220);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 50, 341, 41))
        self.label.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 140, 181, 41))
        self.label_2.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"color: rgb(85, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.salpkg = QtWidgets.QLabel(Dialog)
        self.salpkg.setGeometry(QtCore.QRect(150, 180, 291, 51))
        self.salpkg.setStyleSheet("font: 75 12pt \"Georgia\";")
        self.salpkg.setObjectName("salpkg")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(70, 260, 181, 41))
        self.label_4.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"color: rgb(85, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.cmlist = QtWidgets.QLabel(Dialog)
        self.cmlist.setGeometry(QtCore.QRect(110, 310, 381, 141))
        self.cmlist.setStyleSheet("font: 75 12pt \"Georgia\";")
        self.cmlist.setObjectName("cmlist")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Placement Prediction"))
        self.label.setText(_translate("Dialog", "Placement Prediction"))
        self.label_2.setText(_translate("Dialog", "Salary Package :"))
        self.salpkg.setText(_translate("Dialog", " "))
        self.label_4.setText(_translate("Dialog", "Company List  :"))
        self.cmlist.setText(_translate("Dialog", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
