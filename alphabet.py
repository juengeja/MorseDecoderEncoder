# 0 equals dit, one equals dah
alphabet_to_morse = {
    "A": "01",
    "B": "1000",
    "C": "1010",
    "D": "100",
    "E": "0",
    "F": "0010",
    "G": "110",
    "H": "0000",
    "I": "00",
    "J": "0111",
    "K": "101",
    "L": "0100",
    "M": "11",
    "N": "10",
    "O": "111",
    "P": "0110",
    "Q": "1101",
    "R": "010",
    "S": "000",
    "T": "1",
    "U": "001",
    "V": "0001",
    "W": "011",
    "X": "1001",
    "Y": "1011",
    "Z": "1100",
    "0": "11111",
    "1": "01111",
    "2": "00111",
    "3": "00011",
    "4": "00001",
    "5": "00000",
    "6": "10000",
    "7": "11000",
    "8": "11100",
    "9": "11110",
    "Ä": "0101",
    "Ü": "0011",
    "Ö": "1110",
    "ß": "0001100",
    "À": "01101",
    "È": "01001",
    "É": "00100",
    "0": "010101",
    ",": "110011",
    ":": "111000",
    ";": "101010",
    "?": "001100",
    "1": "100001",
    "_": "001101",
    "(": "10110",
    ")": "101101",
    "'": "011110",
    "=": "10001",
    "+": "01010",
    "/": "10010",
    "@": "011010",
    "Ñ": "11011",
    " ": ".",
    "" : "-"
}

morse_to_alphabet = {v: k for k, v in alphabet_to_morse.items()}