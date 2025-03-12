from typing import List


# my solution
def count_characters(words: List[str], chars: str) -> int:
    result = 0
    chars_table = {}
    for c in chars:
        chars_table[c] = chars_table.get(c, 0) + 1

    for w in words:
        h = {}
        for letter in w:
            h[letter] = h.get(letter, 0) + 1

        word_matched = True
        for k, v in h.items():
            if k not in chars_table:
                word_matched = False
                break
            if v > chars_table[k]:
                word_matched = False
                break

        if word_matched:
            result += len(w)

    return result
