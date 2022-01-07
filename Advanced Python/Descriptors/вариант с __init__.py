class Descriptor:
    """Создаем дескриптор согласно API документации."""
    def __init__(self, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value * value

    def __delete__(self, obj):
        del obj.__dict__[self.__name]


class Point:
    # С помощью дескриптора можно одной строкой заменить написание
    # геттера, сеттера и делитера для нового свойства. Предварительно прописав всю логику
    # в классе дескриптора (Descriptor)
    coord_x = Descriptor('descriptor for coord_x')
    coord_y = Descriptor('descriptor for coord_y')
    # вот если сейчас мы пропишем строку:
    coord_n = Descriptor('descriptor for coord_n')
    # то мы по сути избавляемся от того, чтобы прописывать геттер, сеттер и делиттер для coord_n

    def __init__(self, x=0, y=0):
        self.coord_x = x
        self.coord_y = y


a = Point(1, 2)
b = Point(10, 20)
print(a.coord_x, a.coord_y)
print(b.coord_x, b.coord_y)
