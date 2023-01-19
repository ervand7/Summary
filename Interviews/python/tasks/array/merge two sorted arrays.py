"""
Дано 2 отсортированных (по возрастанию) массива A и B длины M и N. Нужно слить их
в один отсортированный (по возрастанию) массив, состоящий из элементов первых двух.
Пример:
Ввод
[1, 2, 5]
[1, 2, 3, 4, 6]
Вывод
[1, 1, 2, 2, 3, 4, 5, 6]
"""


def sorted_array_merge(arr_a: list, arr_b: list) -> list:
    result = []
    while len(arr_a) != 0 and len(arr_b) != 0:
        if arr_a[0] < arr_b[0]:
            result.append(arr_a.pop(0))
        else:
            result.append(arr_b.pop(0))

    result += arr_a
    result += arr_b

    return result


print(sorted_array_merge([1, 2, 5], [1, 2, 3, 4, 6]))  # [1, 1, 2, 2, 3, 4, 5, 6]
