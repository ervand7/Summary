# my solution
def num_different_integers(word: str) -> int:
    len_word = len(word)
    h = {}
    val = ""
    for idx, i in enumerate(word):
        if i.isdigit():
            val += i
        if i.isdigit() is False or idx == (len_word - 1):
            if val:
                while len(val) > 1 and val[0] == "0":
                    val = val[1:]
                h[val] = True
                val = ""

    return len(h)


# ChatGPT solution
import re


def num_different_integers(word: str) -> int:
    # Replace every non-digit with space, then split into tokens
    tokens = re.split(r'\D+', word)

    # Normalize by stripping leading zeros and ignore empty strings
    numbers = {str(int(token)) for token in tokens if token}

    return len(numbers)


def num_different_integers(word: str) -> int:
    nums = set()
    current = ""

    for ch in word:
        if ch.isdigit():
            current += ch
        else:
            if current:
                nums.add(str(int(current)))
                current = ""
    if current:
        nums.add(str(int(current)))

    return len(nums)
