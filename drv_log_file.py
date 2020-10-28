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
        self.df_dict = {
            'accelerometer': pd.DataFrame,
            'gyroscope': pd.DataFrame
        }

    def extract_data(self, pattern):
        data_list = pattern.findall(self.text)
        return data_list

    def parse_df(self, pattern):
        data_list = self.extract_data(pattern)
        df = pd.DataFrame(data_list,
                          columns=['x', 'y', 'z', 'ts_hh', 'ts_lh'])
        for c_name, _ in df.iteritems():
            df[c_name] = pd.to_numeric(df[c_name])
        ts = (np.bitwise_or(np.left_shift(df['ts_hh'], 32), df['ts_lh']))
        df['timestamp(ms)'] = ts / 19200
        df['ts_interval'] = df['timestamp(ms)'].diff()
        df = df.applymap(lambda x: '%.2f' % x if isinstance(x, float) else x)
        return df

    def parse_acc_data(self):
        self.df_dict.update(
            {'accelerometer': self.parse_df(self.acc_pattern)})

    def parse_gyr_data(self):
        self.df_dict.update(
            {'gyroscope': self.parse_df(self.gyr_pattern)})


if __name__ == "__main__":
    drv_log = DrvLog(r'./bmi270_6hz.log')
    drv_log.parse_acc_data()
    drv_log.parse_gyr_data()
    # print(drv_log.df_dict['accelerometer'])

    dataframes = drv_log.df_dict
    for sensor, df in dataframes.items():
        sample_period = df.describe()['timestamp(ms)']['max'] -\
                        df.describe()['timestamp(ms)']['min']  # sampling period(ms)
        sample_period = sample_period / 1000  # sampling period(s)
        sample_rate = df.describe()['timestamp(ms)']['count'] / sample_period
        # print(df.size)
        print(sample_period, "s", sample_rate, "Hz")

        show(df['x'], np.fft.fft(df['x']), sample_period, sensor=sensor, axis='x')
        show(df['x'], np.fft.fft(df['y']), sample_period, sensor=sensor, axis='y')
        show(df['z'], np.fft.fft(df['z']), sample_period, sensor=sensor, axis='z')
