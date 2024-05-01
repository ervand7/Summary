from typing import List


# my solution
def most_common_word(paragraph: str, banned: List[str]) -> str:
    banned = set(banned)
    words = ""
    for letter in paragraph:
        if letter.isalpha():
            words += letter.lower()
        else:
            words += " "

    h = {}
    max_count = 0
    result = None
    words = words.split()

    for word in words:
        if word not in banned:
            temp = h[word] = h.get(word, 0) + 1
            if temp > max_count:
                result = word
                max_count = temp

    return result
