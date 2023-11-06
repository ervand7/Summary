def max_num(array: list):
    if len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]
    sub = max_num(array[1:])
    return array[0] if array[0] > sub else sub


print(max_num([1, 2, 3, 4]))
