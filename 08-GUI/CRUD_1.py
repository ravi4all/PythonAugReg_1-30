# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CRUD_1.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root',
                       passwd='', db='EmpData', autocommit=True)

cursor = connection.cursor()

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1137, 805)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1151, 781))
        self.frame.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(130, 180, 261, 71))
        self.label.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(130, 300, 261, 71))
        self.label_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(130, 430, 261, 71))
        self.label_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(400, 190, 421, 61))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
                                    "color: rgb(255, 255, 255);")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(400, 310, 421, 61))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
                                    "color: rgb(255, 255, 255);")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(400, 440, 421, 61))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
                                    "color: rgb(255, 255, 255);")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(210, 590, 281, 81))
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 590, 281, 81))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(-10, 0, 1151, 791))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(100, 140, 961, 531))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1137, 31))
        self.menubar.setObjectName("menubar")
        self.menuOperations = QtWidgets.QMenu(self.menubar)
        self.menuOperations.setObjectName("menuOperations")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCreate = QtWidgets.QAction(MainWindow)
        self.actionCreate.setObjectName("actionCreate")
        self.actionRead = QtWidgets.QAction(MainWindow)
        self.actionRead.setObjectName("actionRead")
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.menuOperations.addAction(self.actionCreate)
        self.menuOperations.addAction(self.actionRead)
        self.menuOperations.addAction(self.actionUpdate)
        self.menuOperations.addAction(self.actionDelete)
        self.menubar.addAction(self.menuOperations.menuAction())

        self.frame_2.hide()

        self.actionCreate.triggered.connect(self.showReadData)
        self.actionRead.triggered.connect(self.readEmp)
        self.pushButton.clicked.connect(self.addData)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enter Name"))
        self.label_2.setText(_translate("MainWindow", "Enter Age"))
        self.label_3.setText(_translate("MainWindow", "Enter Salary"))
        self.pushButton.setText(_translate("MainWindow", "Add"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit"))
        # item = self.tableWidget.horizontalHeaderItem(0)
        # item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Names"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Salary"))
        self.menuOperations.setTitle(_translate("MainWindow", "Operations"))
        self.actionCreate.setText(_translate("MainWindow", "Create"))
        self.actionRead.setText(_translate("MainWindow", "Read"))
        self.actionUpdate.setText(_translate("MainWindow", "Update"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))

    def addData(self):
        self.frame_2.hide()
        self.empName = self.lineEdit.text()
        self.empAge = self.lineEdit_2.text()
        self.empSalary = self.lineEdit_3.text()

        query = "INSERT INTO emp VALUES (%s, %s, %s)"

        cursor.execute(query, (self.empName, int(self.empAge), int(self.empSalary)))

        QtWidgets.QMessageBox.information(self,"Success","Data Inserted Successfully")

        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")

    def showReadData(self):
        self.frame_2.hide()

    def readEmp(self):
        self.frame_2.show()

        query = "SELECT * FROM emp"

        cursor.execute(query)

        self.tableWidget.setRowCount(cursor.rowcount)

        for row, form in enumerate(cursor):
            for col, item in enumerate(form):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(item)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

