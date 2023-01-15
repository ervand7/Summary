# список изменится, так как изменение по индексу меняет переданный в функцию список

def change_by_idx(arr: list):
    arr[0] = 777
    print(arr)  # [777, 2, 3]


def main():
    arr = [1, 2, 3]
    print(arr)  # [1, 2, 3]

    change_by_idx(arr)
    print(arr)  # [777, 2, 3]


main()
