# O(n)
from typing import List


def reverse_array(array: List[int]) -> List[int]:
    for i in range(0, len(array) // 2):
        array[i], array[len(array) - 1 - i] = array[len(array) - i - 1], array[i]
    return array


print(reverse_array([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # [9, 8, 7, 6, 5, 4, 3, 2, 1]
