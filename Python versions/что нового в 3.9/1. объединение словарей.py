# 3.8:
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'c': 100, 'd': 200}
union_dict = {**dict1, **dict2}
print(union_dict)  # {'a': 1, 'b': 2, 'c': 100, 'd': 200}

# 3.9:
# теперь словари можно объединять так:
union_dict = dict1 | dict2
print(union_dict)  # {'a': 1, 'b': 2, 'c': 100, 'd': 200}
