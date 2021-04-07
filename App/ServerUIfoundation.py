# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ServerUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setMinimumSize(QtCore.QSize(900, 600))
        MainWindow.setMaximumSize(QtCore.QSize(900, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.users = QtWidgets.QWidget()
        self.users.setObjectName("users")
        self.usersTable = QtWidgets.QTableWidget(self.users)
        self.usersTable.setGeometry(QtCore.QRect(11, 11, 861, 431))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.usersTable.setFont(font)
        self.usersTable.setAutoScrollMargin(16)
        self.usersTable.setObjectName("usersTable")
        self.usersTable.setColumnCount(3)
        self.usersTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.usersTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.usersTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.usersTable.setHorizontalHeaderItem(2, item)
        self.usersTable.horizontalHeader().setDefaultSectionSize(267)
        self.usersTable.verticalHeader().setDefaultSectionSize(43)
        self.usersAddButton = QtWidgets.QPushButton(self.users)
        self.usersAddButton.setGeometry(QtCore.QRect(540, 460, 171, 41))
        self.usersAddButton.setObjectName("usersAddButton")
        self.usersDeleteButton = QtWidgets.QPushButton(self.users)
        self.usersDeleteButton.setGeometry(QtCore.QRect(730, 460, 131, 41))
        self.usersDeleteButton.setObjectName("usersDeleteButton")
        self.tabWidget.addTab(self.users, "")
        self.users_state = QtWidgets.QWidget()
        self.users_state.setObjectName("users_state")
        self.usersStateTable = QtWidgets.QTableWidget(self.users_state)
        self.usersStateTable.setGeometry(QtCore.QRect(11, 11, 861, 491))
        self.usersStateTable.setObjectName("usersStateTable")
        self.usersStateTable.setColumnCount(4)
        self.usersStateTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.usersStateTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.usersStateTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.usersStateTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.usersStateTable.setHorizontalHeaderItem(3, item)
        self.usersStateTable.horizontalHeader().setDefaultSectionSize(207)
        self.usersStateTable.verticalHeader().setDefaultSectionSize(43)
        self.tabWidget.addTab(self.users_state, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.usersTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.usersTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "login"))
        item = self.usersTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "password"))
        self.usersAddButton.setText(_translate("MainWindow", "Добавить"))
        self.usersDeleteButton.setText(_translate("MainWindow", "Удалить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.users), _translate("MainWindow", "Users"))
        item = self.usersStateTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "user_id"))
        item = self.usersStateTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ip"))
        item = self.usersStateTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "time"))
        item = self.usersStateTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "status"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.users_state), _translate("MainWindow", "UsersState"))
