from typing import Type


class Descriptor:
    """Создаем дескриптор с __set_name__ согласно API документации."""

    def __set_name__(self, owner: 'Point', name: str):
        """
        Какое отличие от создания дескриптора через __init__:
        1) при присваивании нам уже ничего не нужно передавать в класс-дескриптор: param=Descriptor()
        дескриптор автоматически определит name
        2) он также автоматически вызывается при присваивании
        """
        print('__set_name__ called')
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
    coord_x = Descriptor()
    coord_y = Descriptor()
    coord_n = Descriptor()

    def __init__(self, x=0, y=0):
        self.coord_x = x
        self.coord_y = y


p = Point(1, 2)
# __set_name__ called
# __set_name__ called
# __set_name__ called

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

print(p.__dict__)  # {'coord_x': 1, 'coord_y': 4, 'coord_n': 9}

del p.coord_n
# deleter called
