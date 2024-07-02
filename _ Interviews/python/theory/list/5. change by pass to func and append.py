# список изменится, так как идет обращение к одному и тому же адресу памяти

def append(arr: list):
    print(hex(id(arr)))  # 0x7ff2e017b900
    arr.append(111)
    print(arr)  # [1, 2, 3, 111]


def main():
    arr = [1, 2, 3]
    print(hex(id(arr)))  # 0x7ff2e017b900
    print(arr)  # [1, 2, 3]

    append(arr)
    print(hex(id(arr)))  # 0x7ff2e017b900
    print(arr)  # [1, 2, 3, 111]


main()
