from scipy.io.wavfile import write
import numpy as np
from alphabet import alphabet_to_morse

fc = 600
fs = 7119
t_dit = 1e-1  # 100 ms
t_dah = 3 * t_dit

user_input = input("Type the text you want to encode to morse: ").upper()

morse_code = ' '.join([alphabet_to_morse.get(char.upper(), char) for char in user_input])

duration = 0
morse_elements = {
    "0": t_dit,
    "1": t_dah,
    ".": t_dit,
    " ": t_dit
}
duration = sum([morse_elements.get(i, 0) + t_dit for i in morse_code], 6*t_dit)
t = np.arange(0, duration, 1/fs)

signal = np.zeros_like(t)

current_time = 0

for i in morse_code:
    pulse_length = morse_elements.get(i, 0)
    if i != "." and i != " ":
        signal[current_time:int(current_time + pulse_length * fs)] = np.sin(2 * np.pi * fc * t[:int(pulse_length * fs)])
        current_time += int(pulse_length * fs)
    else:
        signal[current_time:int(current_time + pulse_length * fs)] = 0
        current_time += int(pulse_length * fs)

    pause_length = t_dit
    signal[current_time:int(current_time + pause_length * fs)] = 0
    current_time += int(pause_length * fs)
signal[current_time:int(current_time + 6*t_dit * fs)] = 0

signal /= np.max(np.abs(signal))

write('morse_code.wav', fs, signal)
