# O(log (n))
import datetime
from random import randint


def binary_search(array, number):
    array = sorted(array)
    lower_bound = 0
    upper_bound = len(array)
    if number > upper_bound or number < lower_bound:
        return 'Not found'

    while lower_bound <= upper_bound:
        center = (lower_bound + upper_bound) // 2

        if array[center] == number:
            return center
        elif array[center] > number:
            upper_bound = center - 1
        elif array[center] < number:
            lower_bound = center + 1

    return 'Not found'


arr = list(range(8000000))
num = 133
print(binary_search(arr, num))
