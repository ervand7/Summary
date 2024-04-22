import string
from typing import List


def unique_morse_representations(words: List[str]) -> int:
    morse_alphabet = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                      "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    english_alphabet = string.ascii_lowercase
    h = {english_alphabet[i]: morse_alphabet[i] for i in range(len(morse_alphabet))}

    values = set()
    for word in words:
        morse_word = ""
        for letter in word:
            morse_word += h[letter]

        values.add(morse_word)

    return len(values)
