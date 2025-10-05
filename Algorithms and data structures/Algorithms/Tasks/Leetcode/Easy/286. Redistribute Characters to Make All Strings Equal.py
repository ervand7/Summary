from typing import List


def make_equal(words: List[str]) -> bool:
    len_words = len(words)
    h = {}
    for word in words:
        for i in word:
            h[i] = h.get(i, 0) + 1

    for v in h.values():
        if v % len_words != 0:
            return False

    return True
