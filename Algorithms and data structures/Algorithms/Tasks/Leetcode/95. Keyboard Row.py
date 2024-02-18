from typing import List


# my solution
def find_words(words: List[str]) -> List[str]:
    first = set("qwertyuiop")
    second = set("asdfghjkl")
    third = set("zxcvbnm")

    result = []
    for word in words:
        s = set(word.lower())
        if s <= first or s <= second or s <= third:
            result.append(word)

    return result
