# словарь изменится, так идет обращение к одному и тому же адресу памяти

def add_new_key(dct: dict):
    print(hex(id(dct)))  # 0x7ff2d003c580
    dct['c'] = 3
    print(dct)  # {'a': 1, 'b': 2, 'c': 3}


def main():
    dct = {'a': 1, 'b': 2}
    print(hex(id(dct)))  # 0x7ff2d003c580
    print(dct)  # {'a': 1, 'b': 2}

    add_new_key(dct)
    print(hex(id(dct)))  # 0x7ff2d003c580
    print(dct)  # {'a': 1, 'b': 2, 'c': 3}


main()
