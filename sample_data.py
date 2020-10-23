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


def show(ori_func, ft, sampling_period=5):
    n = len(ori_func)
    interval = sampling_period / n
    # plot original signal
    plt.subplot(2, 1, 1)
    plt.plot(np.arange(0, sampling_period, interval), ori_func, 'black')
    plt.xlabel('Time'), plt.ylabel('Amplitude')
    # plot fft transformation
    plt.subplot(2, 1, 2)
    frequency = np.arange(n / 2) / sampling_period
    nfft = abs(ft[range(int(n / 2))] / n)
    pp(nfft)
    max_v = max(nfft.tolist())
    idx = list.index(nfft.tolist(), max_v)
    print(frequency[idx])

    plt.plot(frequency, nfft, 'red')
    plt.xlabel('Freq (Hz)'), plt.ylabel('Amp. Spectrum')
    plt.show()

a = 0.5
f = 12
time = 200
sample_rate = 50

signal = np.random.normal(0, 9.8 / 12, sample_rate * time)
g_noise = np.random.normal(0, 1, len(signal))
signal = signal + g_noise
plt.plot(signal)
plt.show()

# rand_l = np.concatenate((np.random.rand(5000)*10, np.random.rand(3000)*(-10)))
# np.random.shuffle(signal)
# pp(signal)

sine = sine_signal_xHz(a, f, time, sample_rate)
# time = np.arange(0, 20, 0.02)
# sine = np.sin(2 * np.pi * 12 * time)
sine = sine + np.random.normal(0, 0.02, time * sample_rate)
plt.plot(sine)
plt.show()

signal_added = signal + sine
# plt.plot(signal_added)
# plt.show()

fft = np.fft.fft(signal_added)
# pp(fft.tolist())
# plt.plot(f)

# sp = np.fft.fft(sine)
# freq = np.fft.fftfreq(time * sample_rate)
# plt.plot(freq, sp.real, freq, sp.imag)
# plt.show()

show(signal_added, fft, time)
