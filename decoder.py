from scipy.io.wavfile import read
from scipy.signal import butter, lfilter
import numpy as np
from alphabet import morse_to_alphabet

fc = 600
fs = 7119
t_dit = 1e-1  # 100 ms
t_dah = 3 * t_dit

user_input = input("Type the name of the .wav file to decode it: ")
_, signal = read(user_input)

b, a = butter(5, [590, 610], fs=fs, btype='band')
y = lfilter(b, a, signal)

signal = np.maximum(signal, 0)

first_index = np.argmax(signal > 0.5)
signal = signal[first_index:]
current_index = int(fs*t_dit)
sum_arr = []

while current_index <= len(signal):
    sum_arr.append(sum(signal[int(current_index-fs*t_dit):current_index]))
    current_index += int(fs*t_dit)

avrg = np.mean(sum_arr)
bits = []

for i in range(len(sum_arr)):
    if sum_arr[i] > avrg:
        bits.append(1)
    else:
        bits.append(0)

bits = np.trim_zeros(bits)

print(bits)