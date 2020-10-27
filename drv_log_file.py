#!/usr/bin/env python
# encoding: utf-8
"""
# Description:
"""
__filename__ = "drv_log_file"
__version__ = "init"
__author__ = "@henry.fan"
import os
import re
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pprint import pprint as pp

from data_fft import *


class DrvLog(object):
    acc_pattern = re.compile(
        r'acc_lsb\s+<\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+>.+[\n|\r]'
        r'.+?acc\s+frame.+[\n|\r]'
        r'.+?acc\.remaped.+[\n|\r]'
        r'.+?dl_meta_acc:<\s?0x\w+\W+(?P<ts_hh>\d+)\W+(?P<ts_lh>\d+)\W+\d+\s?>.+[\n|\r]'
        # , re.S
    )

    gyr_pattern = re.compile(
        r'gyr_lsb\s+<\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+>.+[\n|\r]'
        r'.+?b\.lsb.+[\n|\r]'
        r'.+?a\.lsb.+[\n|\r]'
        r'.+?gyr\.remaped.+[\n|\r]'
        r'.+?gyr\s+num.+[\n|\r]'
        r'.+?dl_meta_gyr:<\s?0x\w+\W+(?P<ts_hh>\d+)\W+(?P<ts_lh>\d+)\W+\d+\s?>.+[\n|\r]'
        # , re.S
    )

    def __init__(self, filename):
        try:
            with open(filename, 'r+') as f:
                self.text = f.read()

        except OSError as e:
            print(e.args)
        except UnicodeDecodeError as e:
            print(e.args)

    def extract_data(self, pattern):
        data_list = pattern.findall(self.text)
        return data_list

    def calc_timestamp(self, ts_tuple):
        return eval(ts_tuple[0]) << 32 | ts_tuple[1]

drv_log = DrvLog(r'./bmi270_6hz.log')

acc_list = drv_log.acc_pattern.findall(drv_log.text)
gyr_list = drv_log.gyr_pattern.findall(drv_log.text)

acc_df = pd.DataFrame(acc_list, columns=['x', 'y', 'z', 'ts_hh', 'ts_lh'])
# acc_df = acc_df[176:9080]
gyr_df = pd.DataFrame(gyr_list, columns=['x', 'y', 'z', 'ts_hh', 'ts_lh'])
print("file loaded and parsed!")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

dataframes = {'accelerator': acc_df, 'gyroscope': gyr_df}
for sensor, df in dataframes.items():
    for c_name, _ in df.iteritems():
        df[c_name] = pd.to_numeric(df[c_name])
    # formater = "{0:.03f}".format
    # acc_df.applymap(formater)
    # gyr_df.applymap(formater)
    df['timestamp'] = np.bitwise_or(np.left_shift(df['ts_hh'], 32), df['ts_lh'])
    time = (df['timestamp'].tolist()[-1] - df['timestamp'].tolist()[0]) / 19200 / 1000  # sampling period(s)
    sample_rate = (len(df)-1) / time
    print(time, "s", sample_rate, "Hz")

    # desc = df.describe()
    # print(desc)
    for axis in ('x', 'y', 'z'):
        # pp(df[axis])
        signal = df[axis]
        time = len(signal) / sample_rate
        fft = np.fft.fft(signal)
        show(signal, fft, time, sensor=sensor, axis=axis)
    # nd_data = df[['x', 'y', 'z']]
    # nfft = np.fft.fftn(nd_data)
    # show(nd_data, nfft, time)
