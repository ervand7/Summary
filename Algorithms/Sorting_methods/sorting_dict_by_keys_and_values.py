# # Варианты для сортировки словаря:
# 1) по значениям:
dict_1 = {'qwe': 123, 'asd': 234, 'zxc': 345}
a = sorted(dict_1.items(), key=lambda x: x[1])
print(a)

# 2) по ключам:
dict_1 = {'qwe': 123, 'asd': 234, 'zxc': 345}
b = sorted(dict_1.items(), key=lambda x: x[0])
print(b)

# В обоих случаях возвращается список с кортежами
