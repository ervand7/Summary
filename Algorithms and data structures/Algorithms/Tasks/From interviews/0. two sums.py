# Дан список целых неповторяющихся чисел и целое число. Необходимо
# найти все пары в списке, сумма которых равна заданному числу.
# Перестановки (i, j) и (j, i) считаются одной и той же парой, можно вывести любую из них.
# Пример:
# Ввод:  nums = [2, 4, 5, 3], k = 7
# Вывод: [ [2, 5], [4, 3] ]

# Логика решения: проходясь по циклу, мы предугадываем второе слагаемое,
# сохраняя его в ключе хеш-таблицы


def find_sums(nums, target) -> list:
    result = []
    dct = {}
    for i in nums:
        dct[target - i] = i
        if i in dct:
            result.append([dct[i], i])

    return result


print(find_sums(nums=[2, 4, 5, 3], target=7))  # [[2, 5], [4, 3]]


def find_sums2(nums, target) -> list:
    """ Делает то же, что и предыдущая, только возвращает индексы"""
    result = []
    dct = {}
    for idx, n in enumerate(nums):
        dct[target - n] = idx
        if n in dct:
            result.append([dct[n], idx])
    return result


print(find_sums2(nums=[2, 4, 5, 3], target=7))  # [[0, 2], [1, 3]]


# ------------------------------------------------------------------
# для поиска значений, а не индексов есть еще вариант решения с хеш-таблицей,
# значения которой пустые:
def find_sums(nums: list, target: int) -> list:
    result = []
    dct = {}
    for i in nums:
        dct[target - i] = True
        if i in dct:
            result.append([target - i, i])
    return result


print(find_sums(nums=[2, 4, 5, 3], target=7))  # [[2, 5], [4, 3]]
