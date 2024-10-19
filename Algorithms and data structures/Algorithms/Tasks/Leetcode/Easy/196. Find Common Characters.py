from typing import List


# my solution
def common_chars(words: List[str]) -> List[str]:
    if len(words) == 1:
        return list(words[0])

    prev = {}
    for i in words[0]:
        prev[i] = prev.get(i, 0) + 1

    for i in range(1, len(words)):
        current = {}
        for j in words[i]:
            current[j] = current.get(j, 0) + 1

        prev = {k: min(prev[k], current[k]) for k in prev if k in current}

    result = []
    for k, v in prev.items():
        result.extend([k] * v)
    return result
