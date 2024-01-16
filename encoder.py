from scipy.io.wavfile import write
import numpy as np
from alphabet import alphabet_to_morse

fc = 600
fs = 7119
t_dit = 1e-1 # 100 ms
t_dah = 3*t_dit

user_input = input("Type the text you want to encode to morse: ").upper()

morse_code = ' '.join([alphabet_to_morse.get(char.upper(), char) for char in user_input])

print(morse_code)