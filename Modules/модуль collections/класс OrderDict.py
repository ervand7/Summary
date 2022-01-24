from collections import OrderedDict

first = {1: 1, 2: 2}
second = {2: 2, 1: 1}
# для встроенноего dict при сравнении словарей порядок элементов в словарях не имеет значения
print(first == second)  # True

# а для OrderedDict порядок элементов имеет значение
print(OrderedDict(first) == OrderedDict(second))  # False

# различия в popitem()
dct = {'hello': 1, 'world': 2, 'hi': 3}
print(dct.popitem())  # ('hi', 3)
print(OrderedDict(dct).popitem(last=False))  # ('hello', 1)

# move_to_end
dct = OrderedDict({'hello': 1, 'world': 2, 'hi': 3})
dct.move_to_end('hello')  # сдвигаем элемент 'hello' в конец
print(dct)  # OrderedDict([('world', 2), ('hi', 3), ('hello', 1)])
dct.move_to_end('hello', last=False)  # сдвигаем элемент 'hello' в начало
print(dct)  # OrderedDict([('hello', 1), ('world', 2), ('hi', 3)])

# надо учитывать, что OrderedDict занимает в 2 раза больше памяти, чем обычный
my_dict = {'qwe': 123, 'asd': 456, 'zxc': 789}
print(my_dict.__sizeof__())  # 216
print(OrderedDict(my_dict).__sizeof__())  # 440
