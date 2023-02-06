# https://proproprogs.ru/python_oop/magicheskie-metody-setattr-getattribute-getattr-i-delattr
class Point:
    MAX_COORD = 100
    MIN_COORD = 50

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __getattribute__(self, item):
        """ Автоматически отрабатывает при обращении к атрибуту. """
        print("__getattribute__ was called")
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        """ Автоматически отрабатывает при присвоении атрибуту какого-либо значения. """
        print("__setattr__ was called")
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        """ Автоматически вызывается, когда идет обращение к несуществующему атрибуту класса. """
        print("__getattr__ was called: " + item)
        return False

    def __delattr__(self, item):
        print("__delattr__ was called: " + item)
        return super(Point, self).__delattr__(item)


p = Point(10, 20)
print(p.MIN_COORD)
# __getattribute__ was called
# 50

p.MIN_COORD = 3
# __setattr__ was called

print(p.qwe)
# __getattr__ was called: qwe
# False

del p.MIN_COORD
# __delattr__ was called: MIN_COORD
