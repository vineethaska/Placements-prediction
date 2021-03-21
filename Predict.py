from PyQt5 import QtCore, QtGui, QtWidgets
from DBConnection import DBConnection
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import pandas as pd
from SalPKG import Ui_SalPKG
import sys
import time
class Ui_Predict(object):
    def browse_file(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File")
        print(fileName)
        self.lineEdit.setText(fileName)

    def predict(self):
        try:
            trainset = []
            fname = self.lineEdit.text()
            database = DBConnection.getConnection()
            cursor = database.cursor()
            cursor.execute(
                "select CodingSkills,AptitudeSkills,TechnicalSkills,CommunicationSkills,PresentationSkills,AcademicPerformance,EnglishProficiency,ProgrammingSkills,ManagementSkills,Projects,Internships,Placed from dataset")
            row = cursor.fetchall()
            y_train = []
            trainset.clear()
            y_train.clear()
            for r in row:
                x_train = []
                x_train.clear()
                x_train.append(float(r[0]))
                x_train.append(float(r[1]))
                x_train.append(float(r[2]))
                x_train.append(float(r[3]))
                x_train.append(float(r[4]))
                x_train.append(float(r[5]))
                x_train.append(float(r[6]))
                x_train.append(float(r[7]))
                x_train.append(float(r[8]))
                x_train.append(float(r[9]))
                x_train.append(float(r[10]))
                y_train.append(r[11])
                trainset.append(x_train)
            print("y=", y_train)
            print("trd=", trainset)
            trainset = np.array(trainset)
            print("trd=", trainset)

            # Train the model
            y_train = np.array(y_train)

            tf = pd.read_csv(fname)
            print(tf)
            testdata = np.array(tf)
            print("td=", testdata)
            testdata = testdata.reshape(len(testdata), -1)

            rf = DecisionTreeClassifier()
            rf.fit(trainset, y_train)
            s = time.clock()
            result = rf.predict(testdata)
            e = time.clock()
            t = round(e - s, 5)
            print("Time:", t, "seconds")
            print("pre=", result)


            if (result[0]=='1'):
                ts=tf.get("TechnicalSkills")[0]
                print("ts=",ts)
                self.label_3.setText('YES')
                self.user = QtWidgets.QDialog()
                self.ui = Ui_SalPKG()
                self.ui.setupUi(self.user)
                self.ui.salinfo(ts)
                self.user.show()


            else:
                self.label_3.setText('NO\n'+"Better Luck Next Time")

            return result

        except Exception as e:
            print("Error=",e)
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(610, 461)

        Dialog.setStyleSheet("background-color: rgb(169,169,169);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 130, 191, 41))
        self.label.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 180, 241, 41))
        self.lineEdit.setStyleSheet("font: 11pt \"Times New Roman\";")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(410, 180, 101, 31))
        self.pushButton.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.browse_file)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 260, 121, 41))
        self.pushButton_2.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.predict)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(120, 360, 131, 51))
        self.label_2.setStyleSheet("font: 14pt \"Franklin Gothic Demi\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(240, 360, 161, 51))
        self.label_3.setStyleSheet("font: 12pt \"Franklin Gothic Demi\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(210, 60, 261, 31))
        self.label_4.setStyleSheet("font: 14pt \"Franklin Gothic Demi\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Placement Prediction"))
        self.label.setText(_translate("Dialog", "Select Testing dataset"))
        self.pushButton.setText(_translate("Dialog", "Browse"))
        self.pushButton_2.setText(_translate("Dialog", "Prediction"))
        self.label_2.setText(_translate("Dialog", "Result  : "))
        self.label_4.setText(_translate("Dialog", "Placement Prediction"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())