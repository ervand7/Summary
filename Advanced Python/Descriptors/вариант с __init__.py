from typing import Type


class Descriptor:
    """Создаем дескриптор с __init__ согласно API документации."""

    def __init__(self, name: str):
        print('__init__ called')
        self.__name = name

    def __get__(self, instance: Type['Point'], owner: 'Point'):
        print('getter called')
        return instance.__dict__[self.__name]

    def __set__(self, instance: Type['Point'], value: int):
        print('setter called')
        instance.__dict__[self.__name] = value * value

    def __delete__(self, obj: Type['Point']):
        print('deleter called')
        del obj.__dict__[self.__name]


class Point:
    # С помощью дескриптора можно одной строкой заменить написание
    # геттера, сеттера и делитера для нового свойства. Предварительно прописав всю логику
    # в классе дескриптора (Descriptor)
    coord_x = Descriptor('descriptor for coord_x')
    coord_y = Descriptor('descriptor for coord_y')
    coord_n = Descriptor('descriptor for coord_n')

    # таким образом мы создали геттеры, сеттеры и делитеры для coord_x, coord_y, coord_n

    def __init__(self, x=0, y=0):
        self.coord_x = x
        self.coord_y = y


p = Point(1, 2)
# __init__ called
# __init__ called
# __init__ called

p.coord_x = 1
print(p.coord_x)
# setter called
# getter called
# 1

p.coord_y = 2
print(p.coord_y)
# setter called
# getter called
# 4

p.coord_n = 3
print(p.coord_n)
# setter called
# getter called
# 9

print(p.__dict__)  # {'descriptor for coord_x': 1, 'descriptor for coord_y': 4, 'descriptor for coord_n': 9}

del p.coord_n
# deleter called
