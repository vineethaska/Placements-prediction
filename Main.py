


from PyQt5 import QtCore, QtGui, QtWidgets
from Student import Ui_Student
from Admin import Ui_Admin
class Ui_Main(object):

    def adminlogin(self, event):
        try:
            self.admn = QtWidgets.QDialog()
            self.ui = Ui_Admin(self.admn)
            self.ui.setupUi(self.admn)
            self.admn.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        event.accept()

    def studentlogin(self, event):
        try:
            self.stdnt = QtWidgets.QDialog()
            self.ui = Ui_Student(self.stdnt)
            self.ui.setupUi(self.stdnt)
            self.stdnt.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        event.accept()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(778, 565)
        Dialog.setStyleSheet("background-color: rgb(176,196,222);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 20, 771, 81))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 20pt \"Vani\";")
        self.label.setObjectName("label")
        self.stdnt = QtWidgets.QLabel(Dialog)
        self.stdnt.setGeometry(QtCore.QRect(250, 330, 271, 131))
        self.stdnt.setStyleSheet("image: url(../StudentPlacement/images/student.png);")
        self.stdnt.setText("")
        self.stdnt.setObjectName("stdnt")
        self.stdnt.mousePressEvent = self.studentlogin
        self.admin = QtWidgets.QLabel(Dialog)
        self.admin.setGeometry(QtCore.QRect(240, 100, 271, 151))
        self.admin.setStyleSheet("image: url(../StudentPlacement/images/adminn.png);")
        self.admin.setText("")
        self.admin.setObjectName("admin")
        self.admin.mousePressEvent = self.adminlogin
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(340, 240, 131, 61))
        self.label_2.setStyleSheet("font: 16pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(340, 470, 141, 61))
        self.label_3.setStyleSheet("font: 16pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Main"))
        self.label.setText(_translate("Dialog", "A Review on Student Placement Chance Prediction"))
        self.label_2.setText(_translate("Dialog", "Admin"))
        self.label_3.setText(_translate("Dialog", "Student"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Main()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
