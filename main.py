#!/usr/bin/python
# -*- coding: utf8 -*-
import os
import sys
from PyQt5 import QtCore, QtWidgets
from mainui import Ui_MainWindow
from drv_log_file import DrvLog


def warning_dialog(title, content):
    warning_box = QtWidgets.QMessageBox()
    warning_box.setWindowTitle(title)
    warning_box.setIcon(QtWidgets.QMessageBox.Warning)
    warning_box.setText(content)
    warning_box.setWindowModality(QtCore.Qt.ApplicationModal)
    warning_box.exec()


class PandasModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        QtCore.QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                # return str(self._data.iloc[index.row(), index.column()])
                return str(self._data.values[index.row()][index.column()])
        return None

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == QtCore.Qt.Vertical:
                return str(self._data.index[section])


class MyApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyApp, self).__init__()
        self.logfile = ''
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.setupUiExt(self)
        # self.ui.setupWidget(self)
        # self.initialize()
        self._setup_signal()

    def initialize(self):
        self.update_settings()
        try:
            pass
        except FileNotFoundError as e:
            warning_dialog("Warning", "{}: {}".format(e.strerror, e.filename))

    def _setup_signal(self):
        self.ui.action_load_logfile.triggered.connect(
            self.choose_log_file)

    def choose_log_file(self):
        self.logfile, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "select file", os.path.dirname(__file__),
            "Text Files (*.log)")
        if not self.logfile:
            return
        else:
            drvlog = DrvLog(self.logfile)
            drvlog.parse_acc_data()
            drvlog.parse_gyr_data()
            # print(drvlog.df_dict['accelerometer'])
            self.set_table_data(drvlog.df_dict['accelerometer'])

    def set_table_data(self, df):
        print(df.describe())
        model = PandasModel(df)
        view = self.ui.acc_data_tableView
        # view = self.ui.table_frame
        # app.setStyleSheet(load_stylesheet_pyqt5())
        # fnt = view.font()
        # fnt.setPointSize(9)
        # view.setFont(fnt)
        view.setModel(model)
        hh = view.horizontalHeader()

        # print(view.verticalHeader())
        # view.setWindowTitle('viewer')
        # view.resize(1080, 400)
        view.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

