# O(n)
from typing import List

"""
Function to reverse arr[] from start to end.
Create a copy array and store reversed elements.
This needs O(n) extra space and is an example of not-in-place algorithm.
"""


def reverse_array_not_in_place(array: List[int]) -> List[int]:
    temp = len(array) * [0]
    for i in range(0, len(array)):
        temp[len(array) - i - 1] = array[i]  # - 1 here to avoid IndexError
    # now copy reversed
    for i in range(0, len(array)):
        array[i] = temp[i]
    return array


print(reverse_array_not_in_place([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # [9, 8, 7, 6, 5, 4, 3, 2, 1]
