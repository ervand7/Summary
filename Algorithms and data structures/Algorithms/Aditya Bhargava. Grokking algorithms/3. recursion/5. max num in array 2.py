def max_num(array, current=0):
    if len(array) == 1:
        return current if current > array[0] else array[0]

    current = current if current > array[0] else array[0]
    return max_num(array[1:], current)


print(max_num([1, 22, 3, 8181, 5]))  # 8181
