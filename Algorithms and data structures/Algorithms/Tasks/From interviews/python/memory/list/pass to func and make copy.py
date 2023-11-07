# список не изменится, так идет обращение к другому объекту памяти

def append(arr: list):
    arr = arr.copy()
    arr.append(111)
    print(hex(id(arr)))  # 0x7f91d0083ac0
    print(arr)  # [1, 2, 3, 111]


def main():
    arr = [1, 2, 3]
    print(hex(id(arr)))  # 0x7f91d0083900
    print(arr)  # 1, 2, 3]

    append(arr)
    print(hex(id(arr)))  # 0x7f91d0083900
    print(arr)  # 1, 2, 3]


main()
