from typing import List


# my solution
def di_string_match(s: str) -> List[int]:
    n = len(s) + 1
    i = sorted([i for i in range(n)])
    d = list(reversed(i))

    result = []
    for letter in s:
        if letter == "I":
            result.append(d.pop())
        else:
            result.append(i.pop())

    result.append(i.pop())

    return result


# ChatGPT solution
def di_string_match(s: str) -> List[int]:
    n = len(s)
    low, high = 0, n
    perm = []

    for char in s:
        if char == 'I':
            perm.append(low)
            low += 1
        else:  # char == 'D'
            perm.append(high)
            high -= 1

    # Append the last remaining number.
    perm.append(low)
    return perm
