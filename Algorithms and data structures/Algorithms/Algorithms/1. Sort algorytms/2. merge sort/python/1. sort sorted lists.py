# O(n)
# can merge only sorted lists
from typing import List


def merge_sort(first: List[int], second: List[int]) -> List[int]:
    i = j = 0
    result = []
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            result.append(first[i])
            i += 1
        else:
            result.append(second[j])
            j += 1

    result += first[i:]
    result += second[j:]
    return result


print(merge_sort(
    first=[2, 8, 8, 16, 19, 54, 65, 76, 87],
    second=[3, 4, 5, 5, 10, 11, 12]
))  # [2, 3, 4, 5, 5, 8, 8, 10, 11, 12, 16, 19, 54, 65, 76, 87]
