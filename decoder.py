from scipy.io.wavfile import read
import numpy as np
from alphabet import morse_to_alphabet

fc = 600
fs = 7119
t_dit = 1e-1  # 100 ms
t_dah = 3 * t_dit

