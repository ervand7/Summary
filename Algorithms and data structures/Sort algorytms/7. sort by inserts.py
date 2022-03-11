# Сложность O(n^2)
"""
Разница между этим алгоритмом и сортировкой выборкой в том,
что тут при добавлении неотсортированного элемента в конец
уже отсортированного списка, программа уже не будет повторно сортировать
все с самого начала. То есть этот алгоритм чуточку быстрее.
"""

array = [-3, 5, 0, -8, 1, 10, -177]
len_array = len(array)

for i in range(1, len_array):
    for j in range(i, 0, -1):
        array_j = array[j]  # for debug
        array_before_j = array[j - 1]  # for debug
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)
