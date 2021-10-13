# варианты для сортировки словаря
dct = {'qwe': 123, 'asd': 234, 'zxc': 345}

# 1) по ключам:
a = sorted(dct.items(), key=lambda x: x[0])
print(a)

# 2) по значениям:
b = sorted(dct.items(), key=lambda x: x[1])
print(b)

# В обоих случаях возвращается список с кортежами
