# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(825, 681)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/resource/img/Black_spider.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.vertical_main = QtWidgets.QVBoxLayout()
        self.vertical_main.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.vertical_main.setObjectName("vertical_main")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.acc_data_tableView = QtWidgets.QTableView(self.centralwidget)
        self.acc_data_tableView.setObjectName("acc_data_tableView")
        self.gridLayout.addWidget(self.acc_data_tableView, 0, 0, 1, 1)
        self.vertical_main.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.vertical_main)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 825, 26))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.tool_bar = QtWidgets.QToolBar(MainWindow)
        self.tool_bar.setObjectName("tool_bar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.tool_bar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_load_logfile = QtWidgets.QAction(MainWindow)
        self.action_load_logfile.setEnabled(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/resources/img/decode.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_load_logfile.setIcon(icon1)
        self.action_load_logfile.setObjectName("action_load_logfile")
        self.tool_bar.addAction(self.action_load_logfile)
        self.tool_bar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Logic Decoder"))
        self.tool_bar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_load_logfile.setText(_translate("MainWindow", "Load file"))

