from collections import defaultdict
from typing import List


# ChatGPT solution
def num_equiv_domino_pairs(dominoes: List[List[int]]) -> int:
    count = defaultdict(int)
    result = 0

    for a, b in dominoes:
        key = tuple(sorted((a, b)))  # normalize to (min, max)
        result += count[key]
        count[key] += 1

    return result


print(num_equiv_domino_pairs([[2, 1], [1, 2], [1, 2], [1, 2], [2, 1], [1, 1], [1, 2], [2, 2]]))
