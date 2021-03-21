
from PyQt5 import QtCore, QtGui, QtWidgets
from DBConnection import DBConnection
class ViewDataSet(object):

    def viewdata(self):
        database = DBConnection.getConnection()
        cursor = database.cursor()
        cursor.execute("select *from dataset")
        row = cursor.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(row):
            self.tableWidget.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(582, 240)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 581, 241))
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(12)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "View DataSet"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "CodingSkills"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "AptitudeSkills"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "TechnicalSkills"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "CommunicationSkills"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "PresentationSkills"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "AcademicPerformance"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "EnglishProficiency"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "ProgrammingSkills"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "ManagementSkills"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Dialog", "Projects"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Dialog", "Internships"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("Dialog", "Placed"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = ViewDataSet()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

