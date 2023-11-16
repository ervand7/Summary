# O(n^2)
from typing import List

"""
Разница между этим алгоритмом и сортировкой выборкой в том,
что тут при добавлении неотсортированного элемента в конец
уже отсортированного списка, программа уже не будет повторно сортировать
все с самого начала. То есть этот алгоритм чуточку быстрее.
"""


def sort_by_inserts(array: List[int]) -> List[int]:
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break

    return array


print(sort_by_inserts([999, -3, 5, 0, -8, 1, 10, -177]))
