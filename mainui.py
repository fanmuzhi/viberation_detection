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
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.acc_tab = QtWidgets.QWidget()
        self.acc_tab.setObjectName("acc_tab")
        self.gridLayout = QtWidgets.QGridLayout(self.acc_tab)
        self.gridLayout.setObjectName("gridLayout")
        self.acc_data_tableView = QtWidgets.QTableView(self.acc_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acc_data_tableView.sizePolicy().hasHeightForWidth())
        self.acc_data_tableView.setSizePolicy(sizePolicy)
        self.acc_data_tableView.setObjectName("acc_data_tableView")
        self.gridLayout.addWidget(self.acc_data_tableView, 0, 0, 1, 1)
        self.tabWidget.addTab(self.acc_tab, "")
        self.gyr_tab = QtWidgets.QWidget()
        self.gyr_tab.setObjectName("gyr_tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gyr_tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gyr_data_tableView = QtWidgets.QTableView(self.gyr_tab)
        self.gyr_data_tableView.setObjectName("gyr_data_tableView")
        self.gridLayout_2.addWidget(self.gyr_data_tableView, 0, 0, 1, 1)
        self.tabWidget.addTab(self.gyr_tab, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
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
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Logic Decoder"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.acc_tab), _translate("MainWindow", "Acc"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gyr_tab), _translate("MainWindow", "Gyro"))
        self.tool_bar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_load_logfile.setText(_translate("MainWindow", "Load file"))

