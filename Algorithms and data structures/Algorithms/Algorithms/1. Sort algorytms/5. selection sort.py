# O(n^2)
from typing import List


def selection_sort(array: List[int]) -> List[int]:
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

    return array


print(selection_sort([999, -3, 5, 0, -8, 1, 10, -177]))  # [-177, -8, -3, 0, 1, 5, 10, 999]
