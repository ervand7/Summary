# Сложность O(n^2)

array = [-3, 5, 0, -8, 1, 10, -177]
len_array = len(array)

for i in range(len_array-1):
    for j in range(i+1, len_array):
        array_i = array[i]  # for debug
        array_j = array[j]  # for debug
        if array[i] > array[j]:
            array[i], array[j] = array[j], array[i]

print(array)
