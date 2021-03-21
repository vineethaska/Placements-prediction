


from PyQt5 import QtCore, QtGui, QtWidgets

import xlrd
from DBConnection import DBConnection
import xlrd
class Ui_UploadDataset(object):

    def browse_file(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File", "*.xlsx")
        print(fileName)
        self.lineEdit.setText(fileName)

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def saveToDB(self):
        try:
            fname = self.lineEdit.text()
            book = xlrd.open_workbook(fname)
            sheet = book.sheet_by_index(0)
            database = DBConnection.getConnection()
            cursor = database.cursor()
            cursor.execute("delete from dataset")
            database.commit()
            query = "insert into dataset values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            for r in range(1, sheet.nrows):
                cs = sheet.cell(r, 0).value
                askl = sheet.cell(r, 1).value
                ts = sheet.cell(r, 2).value
                cms = sheet.cell(r, 3).value
                ps = sheet.cell(r, 4).value
                ap = sheet.cell(r, 5).value
                ep = sheet.cell(r, 6).value
                prsk = sheet.cell(r, 7).value
                ms = sheet.cell(r, 8).value
                prjt = sheet.cell(r, 9).value
                intrnsp = sheet.cell(r, 10).value
                placed = sheet.cell(r, 11).value
                values = (int(cs), int(askl), int(ts), int(cms),int(ps), int(ap), int(ep), int(prsk),
                          int(ms), int(prjt),int(intrnsp),int(placed))
                cursor.execute(query, values)
                database.commit()
                columns = str(sheet.ncols)
                # rows=str(sheet.nrows)
                print("inserted")
            self.showMessageBox("Information", "DataSet Loaded Successfully")
            self.lineEdit.setText("")
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(544, 388)
        Dialog.setStyleSheet("background-color: rgb(176,196,222);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 39, 201, 71))
        self.label.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 120, 131, 41))
        self.label_2.setStyleSheet("font: 75 12pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 160, 251, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(380, 160, 75, 31))
        self.pushButton.setStyleSheet("font: 75 12pt \"Times New Roman\";\n"
"background-color: rgb(0, 85, 127);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.browse_file)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 220, 121, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Times New Roman\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.saveToDB)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Upload DataSet"))
        self.label_2.setText(_translate("Dialog", "Select File"))
        self.pushButton.setText(_translate("Dialog", "Browse"))
        self.pushButton_2.setText(_translate("Dialog", "Upload"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
