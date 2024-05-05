from typing import List


# my solution
def large_group_positions(s: str) -> List[List[int]]:
    if len(s) < 3:
        return []

    result = []
    start = 0
    end = 0

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            end += 1

        else:
            if (end - start) >= 2:
                result.append([start, end])
            start = end = i

    if s[i] == s[i - 1]:
        if (end - start) >= 2:
            result.append([start, end])

    return result


# ChatGPT solution
def large_group_positions(s):
    result = []
    start = 0
    for i in range(1, len(s) + 1):
        if i == len(s) or s[i] != s[i - 1]:
            if i - start >= 3:
                result.append([start, i - 1])
            start = i

    return result


large_group_positions("aaa")
