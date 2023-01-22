# словарь изменится, так как изменение по индексу меняет переданный в функцию список

def change_by_key(dct: dict):
    dct['a'] = 777
    print(dct)  # {'a': 777, 'b': 2}


def main():
    dct = {'a': 1, 'b': 2}
    print(dct)  # {'a': 1, 'b': 2}

    change_by_key(dct)
    print(dct)  # {'a': 777, 'b': 2}


main()
