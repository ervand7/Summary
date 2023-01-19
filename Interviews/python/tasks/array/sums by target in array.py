from typing import List

"""
Условие задачи
Дан список целых неповторяющихся чисел и целое число. Необходимо 
найти все пары в списке, сумма которых равна заданному числу. 
Перестановки (i, j) и (j, i) считаются одной и той же парой, можно вывести любую из них.
Пример:
Ввод:   nums = [2, 4, 5, 3], k = 7
Вывод: [ [2, 5], [4, 3] ]
"""


def find_sums(nums: List[int], target: int) -> List[list]:
    result = []
    dct = {}
    for value in nums:
        dct[target - value] = value
        if value in dct:
            result.append([dct[value], value])

    return result


print(find_sums(nums=[2, 4, 5, 3], target=7))  # [[2, 5], [4, 3]]


def find_sums_idxs(nums: List[int], target: int) -> List[int]:
    """ Делает то же, что и предыдущая, только возвращает индексы"""
    dct = {}
    for idx, number in enumerate(nums):
        dct[target - number] = idx
        if number in dct:
            return [dct[number], idx]


print(find_sums_idxs(nums=[2, 4, 5, 3], target=7))
