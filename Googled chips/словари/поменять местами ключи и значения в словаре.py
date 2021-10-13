# Поменять местами ключи и значения в словаре
my_dict = {'qwe': 123, 'asd': 345, 'zxc': 567}
changed_dict = {v: k for k, v in my_dict.items()}
print(changed_dict)