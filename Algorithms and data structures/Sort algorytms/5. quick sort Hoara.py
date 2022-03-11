"""
Единственное отличие этого алгоритма (быстрая сортировка Хоара)
от обычного quick_sort в том, что при каждом рекурсивном
вызове support_el у нас берется рандомный.
"""
from datetime import datetime
from random import randint

my_array = [7, 5, 2]


def quick_sort_hoara(array):
    if len(array) <= 1:
        return array

    support_el = array[randint(0, len(array) - 1)]  # случайное опорное значение
    left = list(filter(lambda x: x < support_el, array))
    center = [i for i in array if i == support_el]
    right = list(filter(lambda x: x > support_el, array))

    return quick_sort_hoara(left) + center + quick_sort_hoara(right)


if __name__ == '__main__':
    start = datetime.now()
    print(*quick_sort_hoara(my_array))
    end = datetime.now() - start
    print(f'the duration is {end}')
