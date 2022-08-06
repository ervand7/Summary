def count(array: list):
    if len(array) == 0:
        return 0
    return 1 + count(array[1:])


print(count([1, 2, 1, 2, 3, 2, 1, 4]))
