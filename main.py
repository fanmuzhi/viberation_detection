#!/usr/bin/python
# -*- coding: utf8 -*-
import os
import sys
from PyQt5 import QtCore, QtWidgets
from drv_log_file import DrvLog

import numpy as np
import matplotlib.pyplot as plt
from mainui import Ui_MainWindow


def plot_result(dataframe, **kwargs):
    fig = plt.figure()
    title = kwargs.get('sensor', "unknown sensor")
    plt.suptitle(title)
    for axis, ori_func in dataframe[['x', 'y', 'z']].iteritems():
        n = dataframe.describe()['timestamp(ms)']['count']
        sampling_period = dataframe.describe(
        )['timestamp(ms)']['max'] - dataframe.describe()['timestamp(ms)']['min']
        sampling_period = sampling_period / 1000
        interval = sampling_period / (n - 1)
        # plot original signal
        # plt.subplot(2, 1, 1)
        col_num = dataframe.columns.tolist().index(axis)
        fig.add_subplot(3, 2, 2 * col_num + 1)
        # plt.plot(np.arange(0, sampling_period, interval), ori_func, 'black')
        plt.plot(
            (dataframe['timestamp(ms)'] -
             dataframe['timestamp(ms)'][0]) /
            1000,
            dataframe[axis],
            'black')
        plt.xlabel('Time')
        plt.ylabel('Axis: {}\nAmplitude'.format(axis))

        # plot fft transformation
        fig.add_subplot(3, 2, 2 * col_num + 2)
        # plt.subplot(6, 1, 2)
        frequency = np.arange(int(n / 2)) / sampling_period
        frequency = list(map(lambda x: float('%.1f' % x), frequency))
        ft = np.fft.fft(ori_func)
        nfft = abs(ft[range(int(n / 2))] / n)  # normalization and select half
        nfft = list(map(lambda x: float('%.2f' % x), nfft))

        frequency_list = list(set(frequency))
        nfft_list = [float('%.2f' %
                           sum(nfft[frequency.index(f): frequency.index(f) +
                                    frequency.count(f)])) for f in set(frequency)]
        max_v = max(nfft_list[1:])
        idx = list.index(list(nfft_list), max_v)
        # print(frequency_list[idx], max_v)
        plt.stem(frequency_list, nfft_list, use_line_collection=True, linefmt='grey', markerfmt='o')
        plt.stem([frequency_list[idx]], [max_v], use_line_collection=True, linefmt='red', markerfmt='Dr')
        plt.xlabel('Freq (Hz)'), plt.ylabel('Amp. Spectrum')
        plt.annotate("Freq: %.1f" % frequency_list[idx],
                     xy=(frequency_list[idx], max_v),
                     xytext=(10, 5),
                     color='r',
                     textcoords='offset points',
                     ha='center', va='bottom'
                     )
    # plt.get_current_fig_manager().window.showMaximized()
    plt.show()


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

    def headerData(self, section, orientation, role=None):
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
        self.initialize()
        self._setup_signal()
        self.drvlog = None
        self.activesensor = 'accelerometer'

    def initialize(self):
        try:
            self.ui.select_file_button.hide()
            self.ui.analyze_button.setDisabled(True)
        except FileNotFoundError as e:
            warning_dialog("Warning", "{}: {}".format(e.strerror, e.filename))

    def _setup_signal(self):
        self.ui.select_file_button.clicked.connect(self.choose_log_file)
        self.ui.action_load_logfile.triggered.connect(self.choose_log_file)
        self.ui.analyze_button.clicked.connect(self.show_fft_result)
        # self.ui.analyze_button.clicked.connect(self.show_fft_result)

    def choose_log_file(self):
        self.logfile, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "select file", os.path.dirname(__file__),
            "Text Files (*.log)")
        if self.logfile:
            self.ui.label.setText(self.logfile)
            self.drvlog = DrvLog(self.logfile)
            self.drvlog.parse_acc_data()
            self.drvlog.parse_gyr_data()
            self.set_table_data(
                self.drvlog.df_dict['accelerometer'],
                self.ui.acc_data_tableView)
            self.set_table_data(
                self.drvlog.df_dict['gyroscope'],
                self.ui.gyr_data_tableView)
            self.ui.analyze_button.setEnabled(True)
        else:
            # warning_dialog("File Not Found", "cannot find selected file")
            self.ui.analyze_button.setDisabled(True)

    def set_table_data(self, df, table_widget):
        model = PandasModel(df)
        view = table_widget
        fnt = view.font()
        fnt.setPointSize(9)
        view.setFont(fnt)
        view.setModel(model)
        view.horizontalHeader().stretchLastSection()
        view.verticalHeader().stretchLastSection()
        # view.resizeColumnsToContents()
        # view.setWindowTitle('viewer')
        view.show()
        # self.adjustSize()

    def show_fft_result(self):
        if self.ui.tabWidget.currentIndex() == 0:
            self.activesensor = "accelerometer"
        elif self.ui.tabWidget.currentIndex() == 1:
            self.activesensor = "gyroscope"
        # sample_period = self.drvlog.df_dict[sensor].describe()['timestamp(ms)']['max'] -\
        #                 self.drvlog.df_dict[sensor].describe()['timestamp(ms)']['min']  # sampling period(ms)
        # sample_period = sample_period / 1000
        # # plot_series(
        plot_result(
            self.drvlog.df_dict[self.activesensor], sensor=self.activesensor)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
