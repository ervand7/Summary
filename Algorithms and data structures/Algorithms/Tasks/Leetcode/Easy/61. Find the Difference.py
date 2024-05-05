# my solution
def find_the_difference(s: str, t: str) -> str:
    h1 = {}
    h2 = {}
    for i in s:
        h1[i] = h1.get(i, 0) + 1

    for i in t:
        h2[i] = h2.get(i, 0) + 1

    for i in h2:
        if h1.get(i) is None or h1[i] < h2[i]:
            return i


# ChatGPT solution
def find_the_difference(s: str, t: str) -> str:
    count = {}

    for char in t:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for char in s:
        count[char] -= 1
        if count[char] == 0:
            del count[char]

    for char in count:
        return char
