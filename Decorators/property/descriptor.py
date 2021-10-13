class Descriptor:
    def __init__(self, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value

    def __delete__(self, obj):
        del obj.__dict__[self.__name]


class Point:
    # coord_x и coord_y - это и есть дескрипторы
    coord_x = Descriptor('coord_x')
    coord_y = Descriptor('coord_y')

    def __init__(self, x=0, y=0):
        self.coord_x = x
        self.coord_y = y


a = Point(1, 2)
b = Point(10, 20)
print(a.coord_x, a.coord_y)
print(b.coord_x, b.coord_y)