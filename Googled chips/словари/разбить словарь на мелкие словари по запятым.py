# Разбить словарь на мелкие словари по запятым
# На выходе получаем список с мелкими словарями
# https://coderoad.ru/22878743/%D0%9A%D0%B0%D0%BA-%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%BE-%D1%80%D0%B0%D0%B7%D0%B1%D0%B8%D1%82%D1%8C-%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C-%D0%BD%D0%B0-%D0%BD%D0%B5%D1%81%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%BE-%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D0%B5%D0%B9
from itertools import islice

initial_dict = {'qwe': 123, 'asd': 345, 'zxc': 567}
print(list(islice(initial_dict, 2)))


def chunks(data, size=0):
    it = iter(data)
    for i in range(0, len(data), size):
        yield {k: data[k] for k in islice(it, size)}


lst_of_small_dicts = []
for item in chunks({i: a for i, a in initial_dict.items()}, 1):
    lst_of_small_dicts.append(item)
print(lst_of_small_dicts)


# example for my Diploma
def splitting(dct, start=1):
    iter_initial_dict = iter(dct)
    for i in range(len(initial_dict)):
        yield {k: initial_dict[k] for k in islice(iter_initial_dict, start)}


lst_of_small_dicts = []
for item in splitting(initial_dict):
    lst_of_small_dicts.append(item)
print(lst_of_small_dicts)
