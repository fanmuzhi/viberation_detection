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
import pandas as pd
from matplotlib import pyplot as plt
from pprint import pprint as pp

class Drv_Log(object):
    acc_lsb_pattern = re.compile(
        r'acc_lsb\s+<\s+(?P<x>-?\d+)\s+(?P<y>-?\d+)\s+(?P<z>-?\d+)\s+>')
    acc_ts_pattern = re.compile(
        r'dl_meta_acc:<\s?0x\w+\W+(\w+)\W+(\w+)\W+\d+\s?>')
    gyr_lsb_pattern = re.compile(
        r'gyr_lsb\s+<\s+(?P<x>-?\d+)\s+(?P<y>-?\d+)\s+(?P<z>-?\d+)\s+>')
    gyr_ts_pattern = re.compile(
        r'dl_meta_gyr:<\s?0x.+\s+0x.+\s+(\d+)\s+\d+\s?>')

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

drv_log = Drv_Log(r'C:\workspace\BPDD\SEE\mini_dm\bmi270.log')
drv_log = Drv_Log(r'C:\workspace\BPDD\SEE\mini_dm\bmi270.log')
# print(drv_log.text)
keywords = re.compile(
            r'.acc_lsb\s+<\s+(?P<x>-?\d+)\s+(?P<y>-?\d+)\s+(?P<z>-?\d+)\s+>[.|\n|\r]+'
            r'.acc\sframe'
            # r'.remaped[.|\n|\r]+'
            # r'.dl_meta_acc:<\s?0x\w+\W+(?P<ts_hh>\d+)\W+(?P<ts_lh>\d+)\W+\d+\s?>[.|\n|\r]'
            # , re.S
        )
# print("111")
r = keywords.findall(drv_log.text)
print(r)

# acc_data = drv_log.extract_data(Drv_Log.acc_lsb_pattern)
# # acc_ts = list(map(drv_log.calc_timestamp, drv_log.extract_data(Drv_Log.acc_ts_pattern)))
# acc_ts = drv_log.extract_data(Drv_Log.acc_ts_pattern)
# acc_df = pd.DataFrame(acc_data, columns=['x', 'y', 'z'])
# acc_ts_df = pd.DataFrame(acc_ts, columns=['ts_hh', 'ts_lh'])
# print(acc_data)
# acc_df = pd.concat([acc_df, acc_ts_df], axis=1, ignore_index=True)
# for c_name, _ in acc_df.iteritems():
#     acc_df[c_name] = pd.to_numeric(acc_df[c_name])
# print(acc_df)
# acc_df['timestamp'] = acc_df['ts_hh'] << 32 | acc_df['ts_lh']
# print(acc_df)

#
# acc_df['timestamp(ms)'] = acc_df['timestamp']/19200
# acc_df['interval(ms)'] = acc_df['timestamp(ms)'].diff()
#
#
# gyr_data = drv_log.extract_data(Drv_Log.gyr_lsb_pattern)
# gyr_ts = drv_log.extract_data(Drv_Log.gyr_ts_pattern)
# gyr_df = pd.DataFrame(gyr_data, columns=['x', 'y', 'z'])
# gyr_df['timestamp'] = gyr_ts
#
# for c_name, _ in gyr_df.iteritems():
#     gyr_df[c_name] = pd.to_numeric(gyr_df[c_name])
# gyr_df['timestamp(ms)'] = gyr_df['timestamp']/19200
# gyr_df['interval(ms)'] = gyr_df['timestamp(ms)'].diff()
#
# acc_df[['x', 'y', 'z', 'interval(ms)']].plot(subplots=True)
# pp(acc_df.loc[acc_df['interval(ms)'] < 0])
# print(acc_df['timestamp'].tolist())
