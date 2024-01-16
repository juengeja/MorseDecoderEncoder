from scipy.io.wavfile import read
from scipy.signal import butter, lfilter
import numpy as np
from alphabet import morse_to_alphabet

fc = 600
fs = 7119
t_dit = 1e-1  # 100 ms
t_dah = 3 * t_dit
threshold = 0.5

user_input = input("Type the name of the .wav file to decode it: ")
_, signal = read(user_input)

b, a = butter(5, [590, 610], fs=fs, btype='band')
y = lfilter(b, a, signal)

signal = np.maximum(signal, 0)

first_index = np.argmax(signal > threshold)
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
bits.append(0)
ones = 0
zeros = 0
symbol = ""
symbols = []

for i in range(len(bits)):
    if bits[i] == 1 and zeros < 2:
        ones += 1
        zeros = 0
    elif bits[i] == 1 and zeros < 5:
        symbols.append(symbol)
        symbol = ""
        ones += 1
        zeros = 0
    elif bits[i] == 1 and zeros > 4:
        symbols.append(symbol)
        symbols.append(".")
        symbol = ""
        ones += 1
        zeros = 0
    elif bits[i] == 0 and ones > 0:
        if ones == 1:
            symbol += "0"
        else:
            symbol += "1"
        ones = 0
        zeros += 1
    else:
        zeros += 1
symbols.append(symbol)

text = ""
text += ''.join([morse_to_alphabet.get(i) for i in symbols])

print(text)