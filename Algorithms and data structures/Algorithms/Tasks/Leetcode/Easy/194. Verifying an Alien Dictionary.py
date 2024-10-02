from typing import List


# my solution
def is_alien_sorted(words: List[str], order: str) -> bool:
    h = {}
    for i in range(len(order)):
        h[order[i]] = i

    for i in range(1, len(words)):

        for j in range(min(len(words[i]), len(words[i - 1]))):
            letter_prev = words[i - 1][j]
            letter_curr = words[i][j]
            if h[letter_prev] < h[letter_curr]:
                break
            elif h[letter_prev] == h[letter_curr]:
                continue
            else:
                return False

    penultimate = words[i - 1]
    last = words[i]
    if len(penultimate) > len(last):
        if penultimate[:len(last)] == last:
            return False

    return True
