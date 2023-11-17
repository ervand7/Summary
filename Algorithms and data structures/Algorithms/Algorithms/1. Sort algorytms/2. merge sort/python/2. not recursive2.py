# O(n)
# can merge only sorted lists
from typing import List


def merge_sort(first: List[int], second: List[int]) -> List[int]:
    result = []
    while len(first) != 0 and len(second) != 0:
        if first[0] < second[0]:
            result.append(first.pop(0))
        else:
            result.append(second.pop(0))

    result += first
    result += second

    return result


print(merge_sort(
    first=[2, 8, 8, 16, 19, 54, 65, 76, 87],
    second=[3, 4, 5, 5, 10, 11, 12]
))  # [2, 3, 4, 5, 5, 8, 8, 10, 11, 12, 16, 19, 54, 65, 76, 87]
