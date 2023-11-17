# O(n log n), в худшем случае O(n^2) в зависимости от выбора опорного элемента

# Единственное отличие этого алгоритма (быстрая сортировка Хоара)
# от обычного quick_sort в том, что при каждом рекурсивном
# вызове support_el у нас берется рандомный.

from random import randint


def quick_sort_hoara(array):
    if len(array) <= 1:
        return array

    support_el = array[randint(0, len(array) - 1)]  # случайное опорное значение
    left = list(filter(lambda x: x < support_el, array))
    center = [i for i in array if i == support_el]
    right = list(filter(lambda x: x > support_el, array))

    return quick_sort_hoara(left) + center + quick_sort_hoara(right)


print(quick_sort_hoara([7, 5, 2, 3, 9, 8, 6]))  # [2, 3, 5, 6, 7, 8, 9]
