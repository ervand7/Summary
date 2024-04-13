from typing import List


# my solution
def shortest_completing_word(license_plate: str, words: List[str]) -> str:
    h_license = {}
    for i in license_plate.lower():
        if i.isalpha():
            h_license[i] = h_license.get(i, 0) + 1

    shortest_length = float("inf")
    shortest = ""
    len_h_license = len(h_license)

    for word in words:
        word = word.lower()
        counter = 0
        h_word = {}
        for letter in word:
            h_word[letter] = h_word.get(letter, 0) + 1
            license_val = h_license.get(letter, 0)
            if license_val == h_word[letter]:
                counter += 1

        if counter == len_h_license:
            len_word = len(word)
            if len_word < shortest_length:
                shortest = word
                shortest_length = len_word

    return shortest
