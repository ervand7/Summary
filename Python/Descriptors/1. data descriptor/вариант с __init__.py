from typing import Type


class Descriptor:
    """Создаем дескриптор с __init__ согласно API документации."""

    def __init__(self, name: str):
        print('Descriptor __init__ called')
        self.__name = name

    def __get__(self, instance: "Point", owner: Type['Point']):
        # instance - это экземпляр, в данном случае `p`
        # owner - это сам класс, в данном случае `Point`
        print('getter called')
        return instance.__dict__.get(self.__name)

    def __set__(self, instance: "Point", value: int):
        # instance - это экземпляр, в данном случае `p`
        print('setter called')
        instance.__dict__[self.__name] = value * value

    def __delete__(self, obj: "Point"):
        # obj - это экземпляр, в данном случае `p`
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


p = Point()
# Descriptor __init__ called
# Descriptor __init__ called
# Descriptor __init__ called

print(p.coord_x)
# getter called
# None

p.coord_x = 1
# setter called

print(p.coord_x)
# getter called
# 1

p.coord_y = 2
# setter called

print(p.coord_y)
# getter called
# 4

p.coord_n = 3
# setter called

print(p.coord_n)
# getter called
# 9

print(p.__dict__)  # {'descriptor for coord_x': 1, 'descriptor for coord_y': 4, 'descriptor for coord_n': 9}

del p.coord_n
# deleter called

print(p.__dict__)  # {'descriptor for coord_x': 1, 'descriptor for coord_y': 4}
