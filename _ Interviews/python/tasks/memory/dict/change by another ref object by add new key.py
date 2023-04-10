# оба объекта изменятся


def main():
    a = {'a': 1, 'b': 2}
    b = a
    print(hex(id(a)))  # 0x7fdfc81544c0
    print(hex(id(b)))  # 0x7fdfc81544c0

    b['a'] = 777
    print(b)  # {'a': 777, 'b': 2}
    print(a)  # {'a': 777, 'b': 2}


main()
