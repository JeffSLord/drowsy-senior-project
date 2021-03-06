import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt
import csv

PLOT = False
FREQ = False
DATA_PATH = "output_organized.csv"
OUTPUT_PATH = "output_fft.csv"
FFT_OUTPUT = []
HEADER = ["id", "status", "trial"]
for i in range(512):
    HEADER.append("ff" + str(i))

# data_test = np.array(["id", "status", "trial", "packet", 49.0, 50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 50.0, 49.0, 50.0, 50.0, 49.0, 49.0, 50.0, 50.0, 50.0, 50.0, 50.0, 49.0, 49.0, 50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 49.0, 49.0, 49.0, 48.0, 50.0, 50.0, 50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 50.0, 49.0, 50.0, 50.0, 49.0, 49.0, 49.0, 50.0, 49.0, 50.0, 49.0, 50.0, 49.0, 50.0, 50.0, 50.0, 49.0, 49.0, 50.0, 49.0, 50.0, 49.0, 49.0, 50.0, 49.0, 50.0, 50.0, 49.0, 49.0, 50.0, 49.0, 50.0, 50.0, 50.0, 49.0, 50.0, 50.0, 49.0, 49.0, 50.0, 48.0, 49.0, 49.0, 49.0, 49.0, 49.0, 50.0, 49.0, 50.0, 49.0, 49.0, 50.0, 49.0, 49.0, 49.0, 49.0, 49.0, 49.0, 49.0, 50.0, 49.0, 50.0, 50.0, 49.0, 49.0, 49.0, 49.0, 50.0, 50.0, 49.0, 49.0, 49.0, 50.0, 50.0, 50.0, 49.0, 50.0, 50.0, 49.0, 49.0, 50.0, 49.0, 50.0, 50.0, 49.0, 50.0, 50.0, 50.0, 50.0, 49.0, 49.0, 49.0, 49.0, 49.0, 49.0, 50.0, 50.0, 50.0, 49.0, 50.0, 50.0, 50.0, 50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 50.0, 50.0, 50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 48.0, 50.0, 49.0, 50.0, 49.0, 50.0, 49.0, 49.0, 50.0, 49.0, 50.0, 49.0, 49.0, 50.0, 49.0, 49.0, 50.0, 50.0, 50.0, 49.0, 50.0, 50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 50.0, 49.0, 49.0, 49.0, 50.0, 49.0, 50.0, 50.0, 49.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 49.0, 49.0, 49.0, 50.0, 50.0, 50.0, 49.0, 50.0, 50.0, 50.0, 50.0, 49.0, 49.0, 49.0, 50.0, 49.0, 49.0, 50.0, 49.0, 49.0, 49.0, 49.0, 48.0, 49.0, 49.0, 49.0, 49.0, 49.0, 49.0, 49.0, 49.0, 49.0, 48.0, 49.0, 49.0, 50.0, 49.0, 49.0, 49.0, 49.0, 49.0, 49.0, 49.0, 49.0, 49.0, 50.0, 49.0, 49.0, 50.0, 49.0, 48.0, 49.0, 48.0, 49.0, 49.0, 49.0, 49.0, 49.0,
#                       48.0, 49.0, 50.0, 49.0, 49.0, 50.0, 50.0, 50.0, 49.0, 50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 50.0, 50.0, 48.0, 50.0, 49.0, 49.0, 50.0, 49.0, 50.0, 50.0, 50.0, 49.0, 49.0, 50.0, 50.0, 50.0, 49.0, 50.0, 50.0, 50.0, 50.0, 49.0, 50.0, 50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 50.0, 50.0, 50.0, 50.0, 49.0, 49.0, 50.0, 49.0, 49.0, 50.0, 49.0, 50.0, 49.0, 50.0, 48.0, 50.0, 50.0, 50.0, 50.0, 50.0, 49.0, 49.0, 50.0, 49.0, 50.0, 50.0, 50.0, 50.0, 49.0, 50.0, 49.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 49.0, 50.0, 49.0, 50.0, 50.0, 50.0, 49.0, 50.0, 50.0, 50.0, 49.0, 50.0, 50.0, 50.0, 50.0, 49.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 50.0, 50.0, 50.0, 48.0, 50.0, 50.0, 50.0, 50.0, 49.0, 50.0, 50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 50.0, 49.0, 49.0, 49.0, 50.0, 50.0, 49.0, 49.0, 49.0, 49.0, 50.0, 49.0, 49.0, 49.0, 50.0, 48.0, 50.0, 50.0, 50.0, 50.0, 50.0, 49.0, 50.0, 48.0, 49.0, 49.0, 49.0, 50.0, 50.0, 50.0, 49.0, 49.0, 50.0, 50.0, 50.0, 49.0, 49.0, 50.0, 50.0, 50.0, 50.0, 50.0, 49.0, 50.0, 51.0, 49.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 49.0, 50.0, 50.0, 50.0, 50.0, 49.0, 49.0, 49.0, 49.0, 50.0, 50.0, 49.0, 49.0, 50.0, 50.0, 49.0, 50.0, 50.0, 50.0, 50.0, 49.0, 49.0, 50.0, 49.0, 49.0, 50.0, 49.0, 50.0, 49.0, 49.0, 49.0, 48.0, 49.0, 50.0, 49.0, 48.0, 49.0, 50.0, 49.0, 50.0, 49.0, 50.0, 49.0, 50.0, 49.0, 49.0, 50.0, 50.0, 49.0, 49.0, 49.0, 50.0, 50.0, 50.0, 49.0, 49.0, 49.0, 49.0, 49.0, 49.0, 49.0, 49.0, 48.0, 50.0, 49.0, 49.0, 50.0, 50.0, 49.0, 49.0, 49.0, 49.0, 50.0])

# data_test2 = np.array([50.0, 50.0, 50.0, 50.0, 49.0, 49.0, 50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 49.0, 49.0, 49.0, 48.0, 50.0, 50.0, 50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 50.0, 49.0, 50.0, 50.0, 49.0, 49.0, 49.0, 50.0, 49.0, 50.0, 49.0, 50.0, 49.0, 50.0, 50.0, 50.0, 49.0, 49.0, 50.0, 49.0, 50.0, 49.0, 49.0, 50.0, 49.0, 50.0, 50.0, 49.0, 49.0, 50.0, 49.0, 50.0, 50.0, 50.0, 49.0, 50.0, 50.0, 49.0, 49.0, 50.0, 48.0, 49.0, 49.0, 49.0, 49.0, 49.0, 50.0, 49.0, 50.0, 49.0, 49.0, 50.0, 49.0, 49.0, 49.0, 49.0, 49.0, 49.0, 49.0, 50.0, 49.0, 50.0, 50.0, 49.0, 49.0, 49.0, 49.0, 50.0, 50.0, 49.0, 49.0, 49.0, 50.0, 50.0, 50.0, 49.0, 50.0, 50.0, 49.0, 49.0, 50.0, 49.0, 50.0, 50.0, 49.0, 50.0, 50.0, 50.0, 50.0, 49.0, 49.0, 49.0, 49.0, 49.0, 49.0, 50.0, 50.0, 50.0, 49.0, 50.0, 50.0, 50.0, 50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 50.0, 50.0, 50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 48.0, 50.0, 49.0, 50.0, 49.0, 50.0, 49.0, 49.0, 50.0, 49.0, 50.0, 49.0, 49.0, 50.0, 49.0, 49.0, 50.0, 50.0, 50.0, 49.0, 50.0, 50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 50.0, 49.0, 49.0, 49.0, 50.0, 49.0, 50.0, 50.0, 49.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 49.0, 49.0, 49.0, 50.0, 50.0, 50.0, 49.0, 50.0, 50.0, 50.0, 50.0, 49.0, 49.0, 49.0, 50.0, 49.0, 49.0, 50.0, 49.0, 49.0, 49.0, 49.0, 48.0, 49.0, 49.0, 49.0, 49.0, 49.0, 49.0, 49.0, 49.0, 49.0, 48.0, 49.0, 49.0, 50.0, 49.0, 49.0, 49.0, 49.0, 49.0, 49.0, 49.0, 49.0, 49.0, 50.0, 49.0, 49.0, 50.0, 49.0, 48.0, 49.0, 48.0, 49.0, 49.0, 49.0, 49.0, 49.0,
#                        48.0, 49.0, 50.0, 49.0, 49.0, 50.0, 50.0, 50.0, 49.0, 50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 50.0, 50.0, 48.0, 50.0, 49.0, 49.0, 50.0, 49.0, 50.0, 50.0, 50.0, 49.0, 49.0, 50.0, 50.0, 50.0, 49.0, 50.0, 50.0, 50.0, 50.0, 49.0, 50.0, 50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 50.0, 50.0, 50.0, 50.0, 49.0, 49.0, 50.0, 49.0, 49.0, 50.0, 49.0, 50.0, 49.0, 50.0, 48.0, 50.0, 50.0, 50.0, 50.0, 50.0, 49.0, 49.0, 50.0, 49.0, 50.0, 50.0, 50.0, 50.0, 49.0, 50.0, 49.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 49.0, 50.0, 49.0, 50.0, 50.0, 50.0, 49.0, 50.0, 50.0, 50.0, 49.0, 50.0, 50.0, 50.0, 50.0, 49.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 50.0, 50.0, 50.0, 48.0, 50.0, 50.0, 50.0, 50.0, 49.0, 50.0, 50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 50.0, 49.0, 49.0, 49.0, 50.0, 50.0, 49.0, 49.0, 49.0, 49.0, 50.0, 49.0, 49.0, 49.0, 50.0, 48.0, 50.0, 50.0, 50.0, 50.0, 50.0, 49.0, 50.0, 48.0, 49.0, 49.0, 49.0, 50.0, 50.0, 50.0, 49.0, 49.0, 50.0, 50.0, 50.0, 49.0, 49.0, 50.0, 50.0, 50.0, 50.0, 50.0, 49.0, 50.0, 51.0, 49.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 49.0, 50.0, 50.0, 50.0, 50.0, 49.0, 49.0, 49.0, 49.0, 50.0, 50.0, 49.0, 49.0, 50.0, 50.0, 49.0, 50.0, 50.0, 50.0, 50.0, 49.0, 49.0, 50.0, 49.0, 49.0, 50.0, 49.0, 50.0, 49.0, 49.0, 49.0, 48.0, 49.0, 50.0, 49.0, 48.0, 49.0, 50.0, 49.0, 50.0, 49.0, 50.0, 49.0, 50.0, 49.0, 49.0, 50.0, 50.0, 49.0, 49.0, 49.0, 50.0, 50.0, 50.0, 49.0, 49.0, 49.0, 49.0, 49.0, 49.0, 49.0, 49.0, 48.0, 50.0, 49.0, 49.0, 50.0, 50.0, 49.0, 49.0, 49.0, 49.0, 50.0, 49.0, 50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 50.0, 49.0, 50.0, 50.0, 49.0, 49.0, 50.0])

#! only need first half of array, the second half is symmetric

# data = np.genfromtxt("output_raw.csv", delimiter=",", names=True)
# print(data)
# print(data.shape)
# print(data['id'])
# print(data.dtype.names)


def fft(row):
    sampling_rate = 512
    t = np.linspace(0, 512, 1 * sampling_rate, endpoint=False)
    t_half = np.linspace(0, 512/2, 512/2, endpoint=False)
    t_50 = np.linspace(0, 50, 50, endpoint=False)

    data = np.asarray(row[3:])
    data = data.astype(np.float)
    # print(data)
    # print(len(data))
    #! subtract average of set from all elements
    x = np.subtract(data, np.average(data))
    #! fft
    ff = fftpack.fft(x)

    if(FREQ):
        freqs = fftpack.fftfreq(len(x), 1.0/5.0)
        print(freqs)

    if(PLOT):
        fig, ax = plt.subplots()
        ax.plot(t, x)
        plt.ylabel('amplitude')
        plt.xlabel('time (512 samples per second)')

        fig, ax = plt.subplots()
        ax.stem(t_half, np.abs(ff[0:256]))
        plt.ylabel('amplitude')
        plt.xlabel('time (512 samples per second)')

        fig, ax = plt.subplots()
        ax.stem(t_50, np.abs(ff[0:50]))
        plt.ylabel('amplitude')
        plt.xlabel('time (512 samples per second)')

        plt.show()

    return ff


f = open(OUTPUT_PATH, "w+")
f.close()

with open(DATA_PATH, 'r') as file_in:
    with open(OUTPUT_PATH, "w") as file_out:
        reader = csv.reader(file_in, delimiter=",")
        writer = csv.writer(file_out, delimiter=",")
        next(reader)
        writer.writerow(HEADER)
        for row in reader:
            res = []
            res.extend([row[0], row[1], row[2]])
            res.extend(fft(row))
            writer.writerow(res)
            print(res)
