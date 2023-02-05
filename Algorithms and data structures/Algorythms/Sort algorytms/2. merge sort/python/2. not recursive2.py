# O(n)
# can merge only sorted lists
from typing import List


def merge_lists(first: List[int], second: List[int]) -> List[int]:
    result = []
    while len(first) != 0 and len(second) != 0:
        if first[0] < second[0]:
            result.append(first.pop(0))
        else:
            result.append(second.pop(0))

    result += first
    result += second

    return result


print(merge_lists([1, 2, 5], [1, 2, 3, 4, 6]))  # [1, 1, 2, 2, 3, 4, 5, 6]
