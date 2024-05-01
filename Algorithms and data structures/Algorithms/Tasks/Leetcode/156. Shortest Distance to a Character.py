from typing import List


# my solution
def shortest_to_char(s: str, c: str) -> List[int]:
    n = len(s) - 1
    result = []
    for i in range(len(s)):
        if s[i] == c:
            result.append(0)
        else:
            pointer_pos = i + 1
            pointer_neg = i - 1
            while pointer_pos <= n or pointer_neg >= 0:
                if pointer_pos <= n:
                    if s[pointer_pos] == c:
                        result.append(pointer_pos - i)
                        break
                    pointer_pos += 1
                if pointer_neg >= 0:
                    if s[pointer_neg] == c:
                        result.append(i - pointer_neg)
                        break
                    pointer_neg -= 1

    return result


# ChatGPT smart solution
def shortest_to_char(s: str, c: str) -> List[int]:
    len_s = len(s)
    result = [float('inf')] * len_s  # Start with large distances initially.

    # Forward pass
    prev = float('-inf')  # Initially, set it far left out of bounds.
    for i in range(len_s):
        if s[i] == c:
            prev = i
        result[i] = min(result[i], abs(i - prev))

    # Backward pass
    prev = float('inf')  # Reset to far right out of bounds.
    for i in range(len_s - 1, -1, -1):
        if s[i] == c:
            prev = i
        result[i] = min(result[i], abs(i - prev))

    return result


shortest_to_char(s="loveleetcode", c="e")
