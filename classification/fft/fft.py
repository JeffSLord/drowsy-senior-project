import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import fftpack

data1 = np.array([49.0,50.0,50.0,50.0,49.0,50.0,49.0,49.0,50.0,49.0,50.0,49.0,50.0,50.0,50.0,50.0,49.0,50.0,50.0,49.0,50.0,50.0,50.0,50.0,49.0,49.0,49.0,49.0,49.0,49.0,50.0,49.0,48.0,49.0,49.0,49.0,50.0,49.0,49.0,49.0,49.0,49.0,49.0,49.0,50.0,50.0,49.0,50.0,49.0,49.0,49.0,50.0,49.0,49.0,49.0,50.0,49.0,50.0,50.0,49.0,48.0,49.0,49.0,50.0,50.0,49.0,49.0,49.0,50.0,49.0,49.0,49.0,50.0,50.0,50.0,49.0,48.0,49.0,50.0,49.0,49.0,49.0,49.0,49.0,49.0,49.0,50.0,50.0,49.0,50.0,49.0,49.0,50.0,50.0,50.0,49.0,49.0,50.0,48.0,49.0,50.0,49.0,50.0,49.0,50.0,50.0,49.0,50.0,50.0,49.0,50.0,49.0,50.0,49.0,49.0,49.0,49.0,49.0,49.0,49.0,49.0,50.0,49.0,50.0,50.0,49.0,49.0,49.0,49.0,49.0,49.0,49.0,49.0,50.0,48.0,49.0,50.0,49.0,48.0,49.0,49.0,49.0,49.0,49.0,49.0,49.0,49.0,49.0,49.0,50.0,50.0,49.0,49.0,50.0,49.0,50.0,50.0,50.0,49.0,50.0,50.0,50.0,49.0,49.0,50.0,50.0,49.0,49.0,49.0,50.0,49.0,50.0,49.0,50.0,50.0,48.0,50.0,50.0,49.0,49.0,50.0,50.0,50.0,49.0,49.0,50.0,50.0,50.0,50.0,49.0,49.0,49.0,49.0,50.0,49.0,49.0,49.0,49.0,49.0,50.0,49.0,49.0,50.0,50.0,49.0,50.0,50.0,50.0,49.0,49.0,50.0,49.0,49.0,50.0,49.0,49.0,49.0,49.0,49.0,50.0,49.0,49.0,49.0,49.0,49.0,50.0,50.0,50.0,50.0,50.0,49.0,50.0,50.0,50.0,49.0,49.0,50.0,49.0,49.0,49.0,50.0,48.0,49.0,49.0,48.0,49.0,49.0,48.0,50.0,49.0,50.0,50.0,49.0,49.0,49.0,49.0,50.0,49.0,49.0,49.0,48.0,50.0,49.0,49.0,49.0,49.0,49.0,48.0,49.0,49.0,49.0,49.0,48.0,49.0,49.0,49.0,49.0,49.0,49.0,49.0,49.0,50.0,49.0,50.0,49.0,49.0,49.0,49.0,49.0,49.0,49.0,49.0,49.0,48.0,50.0,49.0,49.0,49.0,50.0,50.0,49.0,49.0,49.0,49.0,50.0,48.0,49.0,49.0,50.0,49.0,49.0,50.0,49.0,50.0,49.0,49.0,49.0,50.0,50.0,50.0,50.0,49.0,50.0,50.0,49.0,49.0,49.0,49.0,49.0,49.0,49.0,49.0,50.0,49.0,50.0,49.0,50.0,50.0,49.0,49.0,49.0,50.0,49.0,50.0,50.0,49.0,50.0,49.0,49.0,49.0,48.0,49.0,50.0,50.0,50.0,50.0,50.0,49.0,49.0,49.0,50.0,50.0,50.0,50.0,49.0,50.0,49.0,50.0,49.0,49.0,50.0,49.0,50.0,49.0,50.0,49.0,50.0,49.0,49.0,49.0,50.0,49.0,49.0,49.0,49.0,49.0,50.0,50.0,50.0,49.0,49.0,49.0,49.0,48.0,48.0,49.0,49.0,49.0,50.0,49.0,49.0,49.0,49.0,49.0,49.0,49.0,50.0,49.0,49.0,49.0,50.0,49.0,48.0,49.0,50.0,49.0,50.0,50.0,50.0,49.0,50.0,49.0,50.0,49.0,49.0,49.0,49.0,50.0,49.0,50.0,50.0,50.0,49.0,49.0,49.0,50.0,50.0,49.0,50.0,50.0,50.0,50.0,50.0,49.0,49.0,50.0,49.0,49.0,49.0,49.0,49.0,49.0,49.0,49.0,50.0,48.0,48.0,49.0,49.0,49.0,50.0,49.0,48.0,49.0,49.0,50.0,49.0,49.0,49.0,50.0,50.0,49.0,49.0,49.0,50.0,49.0,50.0,48.0,48.0,49.0,49.0,49.0,49.0,50.0,49.0,49.0,49.0,50.0,49.0,50.0,49.0,50.0,49.0,49.0,49.0,50.0,49.0,50.0,50.0,50.0,48.0,49.0,50.0,50.0,50.0,48.0,49.0,48.0,49.0,49.0,49.0,49.0])
data2 = np.array([49.0,50.0,50.0,49.0,50.0,49.0,49.0,50.0,49.0,50.0,50.0,49.0,49.0,50.0,50.0,50.0,50.0,50.0,49.0,49.0,50.0,50.0,49.0,50.0,49.0,49.0,49.0,49.0,49.0,48.0,50.0,50.0,50.0,50.0,49.0,50.0,49.0,49.0,50.0,49.0,50.0,50.0,49.0,49.0,49.0,50.0,49.0,50.0,49.0,50.0,49.0,50.0,50.0,50.0,49.0,49.0,50.0,49.0,50.0,49.0,49.0,50.0,49.0,50.0,50.0,49.0,49.0,50.0,49.0,50.0,50.0,50.0,49.0,50.0,50.0,49.0,49.0,50.0,48.0,49.0,49.0,49.0,49.0,49.0,50.0,49.0,50.0,49.0,49.0,50.0,49.0,49.0,49.0,49.0,49.0,49.0,49.0,50.0,49.0,50.0,50.0,49.0,49.0,49.0,49.0,50.0,50.0,49.0,49.0,49.0,50.0,50.0,50.0,49.0,50.0,50.0,49.0,49.0,50.0,49.0,50.0,50.0,49.0,50.0,50.0,50.0,50.0,49.0,49.0,49.0,49.0,49.0,49.0,50.0,50.0,50.0,49.0,50.0,50.0,50.0,50.0,50.0,49.0,50.0,49.0,49.0,50.0,50.0,50.0,50.0,49.0,50.0,49.0,49.0,48.0,50.0,49.0,50.0,49.0,50.0,49.0,49.0,50.0,49.0,50.0,49.0,49.0,50.0,49.0,49.0,50.0,50.0,50.0,49.0,50.0,50.0,50.0,49.0,50.0,49.0,49.0,50.0,49.0,49.0,49.0,50.0,49.0,50.0,50.0,49.0,50.0,50.0,50.0,50.0,50.0,50.0,49.0,49.0,49.0,50.0,50.0,50.0,49.0,50.0,50.0,50.0,50.0,49.0,49.0,49.0,50.0,49.0,49.0,50.0,49.0,49.0,49.0,49.0,48.0,49.0,49.0,49.0,49.0,49.0,49.0,49.0,49.0,49.0,48.0,49.0,49.0,50.0,49.0,49.0,49.0,49.0,49.0,49.0,49.0,49.0,49.0,50.0,49.0,49.0,50.0,49.0,48.0,49.0,48.0,49.0,49.0,49.0,49.0,49.0,48.0,49.0,50.0,49.0,49.0,50.0,50.0,50.0,49.0,50.0,50.0,49.0,50.0,49.0,49.0,50.0,50.0,48.0,50.0,49.0,49.0,50.0,49.0,50.0,50.0,50.0,49.0,49.0,50.0,50.0,50.0,49.0,50.0,50.0,50.0,50.0,49.0,50.0,50.0,50.0,49.0,50.0,49.0,49.0,50.0,50.0,50.0,50.0,49.0,49.0,50.0,49.0,49.0,50.0,49.0,50.0,49.0,50.0,48.0,50.0,50.0,50.0,50.0,50.0,49.0,49.0,50.0,49.0,50.0,50.0,50.0,50.0,49.0,50.0,49.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,49.0,50.0,49.0,50.0,50.0,50.0,49.0,50.0,50.0,50.0,49.0,50.0,50.0,50.0,50.0,49.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,49.0,50.0,49.0,49.0,50.0,50.0,50.0,48.0,50.0,50.0,50.0,50.0,49.0,50.0,50.0,50.0,49.0,50.0,49.0,49.0,50.0,49.0,49.0,49.0,50.0,50.0,49.0,49.0,49.0,49.0,50.0,49.0,49.0,49.0,50.0,48.0,50.0,50.0,50.0,50.0,50.0,49.0,50.0,48.0,49.0,49.0,49.0,50.0,50.0,50.0,49.0,49.0,50.0,50.0,50.0,49.0,49.0,50.0,50.0,50.0,50.0,50.0,49.0,50.0,51.0,49.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,49.0,50.0,50.0,50.0,50.0,49.0,49.0,49.0,49.0,50.0,50.0,49.0,49.0,50.0,50.0,49.0,50.0,50.0,50.0,50.0,49.0,49.0,50.0,49.0,49.0,50.0,49.0,50.0,49.0,49.0,49.0,48.0,49.0,50.0,49.0,48.0,49.0,50.0,49.0,50.0,49.0,50.0,49.0,50.0,49.0,49.0,50.0,50.0,49.0,49.0,49.0,50.0,50.0,50.0,49.0,49.0,49.0,49.0,49.0,49.0,49.0,49.0,48.0,50.0,49.0,49.0,50.0,50.0,49.0,49.0,49.0,49.0,50.0])

# def test1():
#     f = 10 # Frequency
#     f_s = 100 # Sampling rate
#
#     t = np.linspace(0,2,2*f_s,endpoint=False)
#     x = np.sin(f * 2 * np.pi * t)
#
#     fig, ax = plt.subplots()
#     ax.plot(t, x)
#     plt.show()
#
#
#     X = fftpack.fft(x)
#     freqs = fftpack.fftfreq(len(x)) * f_s
#     fig, ax = plt.subplots()
#     ax.stem(freqs, np.abs(X))
#     plt.show()

def test2():
    f_s = 512
    t = np.linspace(0, 512, 1 * f_s, endpoint=False)
    x = data2
    x = np.subtract(x, np.average(x))

    X = fftpack.fft(x)
    freqs = fftpack.fftfreq(len(x)) * f_s
    #freqs = fftpack.fftfreq(len(x))

    frange = np.linspace(0, 512, 512);
    print(freqs)
    #print(X)

    fig, ax = plt.subplots()
    ax.plot(t, x)
    plt.ylabel('amplitude')
    plt.xlabel('time (512 samples per second)')
    #plt.ylim(min(x) - 3, max(x) + 3)

    fig, ax = plt.subplots()
    ax.plot(freqs, np.abs(X))
    #ax.stem(freqs, X)
    #ax.plot(frange, np.abs(X))
    plt.ylabel('amplitude')
    plt.xlabel('frequency (abs)')
    ax.plot()
    #plt.ylim(0,50)

    ###
    fig, ax = plt.subplots()
    ax.plot(fftpack.fftshift(np.abs(X)))
    plt.ylabel('amplitude')
    plt.xlabel('frequency (shift)')
    ax.plot()

    fig, ax = plt.subplots()
    ax.plot(np.abs(X))
    plt.ylabel('amplitude')
    plt.xlabel('fft result (abs)')
    ax.plot()
    ###


    plt.show()



test2()