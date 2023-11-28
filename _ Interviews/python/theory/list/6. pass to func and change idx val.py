# список изменится, так идет обращение к одному и тому же адресу памяти

def change_by_idx(arr: list):
    print(hex(id(arr)))  # 0x7fdbb019cf00
    arr[0] = 777
    print(arr)  # [777, 2, 3]


def main():
    arr = [1, 2, 3]
    print(hex(id(arr)))   # 0x7fdbb019cf00
    print(arr)  # [1, 2, 3]

    change_by_idx(arr)
    print(arr)  # [777, 2, 3]


main()
