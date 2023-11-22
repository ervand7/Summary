# O(n)
# Function to reverse arr[] from start to end.
# Create a copy array and store reversed elements.
# This needs extra space for temp array.
from typing import List


def reverse_array(array: List[int]) -> List[int]:
    temp = len(array) * [0]
    for i in range(0, len(array)):
        temp[len(array) - 1 - i] = array[i]
    for i in range(0, len(array)):
        array[i] = temp[i]
    return array


print(reverse_array([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # [9, 8, 7, 6, 5, 4, 3, 2, 1]
