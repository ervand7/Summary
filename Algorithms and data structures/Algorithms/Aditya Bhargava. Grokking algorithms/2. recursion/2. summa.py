def summa(array: list):
    if len(array) == 0:
        return 0
    return array[0] + summa(array[1:])


print(summa([1, 2, 3, 12, 100]))  # 118
