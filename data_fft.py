#!/usr/bin/env python
# encoding: utf-8
"""
# Description:
"""
__filename__ = "random_data"
__version__ = "init"
__author__ = "@henry.fan"

import numpy as np
from pprint import pprint as pp
import matplotlib.pyplot as plt


def sine_signal_xHz(amp, fi, time_s, sample):
    return amp * np.sin(np.linspace(0, fi * time_s * 2 * np.pi, sample * time_s))


def show(ori_func, ft, sampling_period=5, **kwargs):
    title = kwargs.get('sensor', "unknown sensor") + ": " +\
            kwargs.get("axis", "unkown axis")


    plt.suptitle(title)
    n = len(ori_func)
    interval = sampling_period / n
    # plot original signal
    plt.subplot(2, 1, 1)
    plt.plot(np.arange(0, sampling_period, interval), ori_func, 'black')
    plt.xlabel('Time'), plt.ylabel('Amplitude')

    # plot fft transformation
    plt.subplot(2, 1, 2)
    frequency = np.arange(int(n / 2)) / sampling_period
    frequency = list(map(lambda x: float('%.1f' % x), frequency))
    nfft = abs(ft[range(int(n / 2))] / n)  # normalization and select half
    nfft = list(map(lambda x: float('%.2f' % x), nfft))

    frequency_list = list(set(frequency))
    nfft_list = [float('%.2f' % sum(nfft[frequency.index(f): frequency.index(f)+frequency.count(f)])) for f in set(frequency)]
    max_v = max(nfft_list[1:])
    idx = list.index(list(nfft_list), max_v)
    print(frequency_list[idx], max_v)
    plt.stem(frequency_list, nfft_list, use_line_collection=True)
    plt.xlabel('Freq (Hz)'), plt.ylabel('Amp. Spectrum')
    plt.annotate("  freq: %.1f" % frequency_list[idx],
                 xytext=(frequency_list[idx], max_v),
                 xy=(frequency_list[idx], max_v))
    plt.show()

# a = 0.5
# f = 12
# time = 200
# sample_rate = 50
#
# signal = np.random.normal(0, 9.8 / 12, sample_rate * time)
# g_noise = np.random.normal(0, 1, len(signal))
# signal = signal + g_noise
# plt.plot(signal)
# plt.show()
#
# # rand_l = np.concatenate((np.random.rand(5000)*10, np.random.rand(3000)*(-10)))
# # np.random.shuffle(signal)
# # pp(signal)
#
# sine = sine_signal_xHz(a, f, time, sample_rate)
# # time = np.arange(0, 20, 0.02)
# # sine = np.sin(2 * np.pi * 12 * time)
# sine = sine + np.random.normal(0, 0.02, time * sample_rate)
# plt.plot(sine)
# plt.show()
#
# signal_added = signal + sine
# # plt.plot(signal_added)
# # plt.show()
#
# fft = np.fft.fft(signal_added)
# # pp(fft.tolist())
# # plt.plot(f)
#
# # sp = np.fft.fft(sine)
# # freq = np.fft.fftfreq(time * sample_rate)
# # plt.plot(freq, sp.real, freq, sp.imag)
# # plt.show()
#
# show(signal_added, fft, time)
