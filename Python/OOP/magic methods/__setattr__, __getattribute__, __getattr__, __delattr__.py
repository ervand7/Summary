class Point:
    MAX_COORD = 100
    MIN_COORD = 50

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __getattribute__(self, item):
        """ Автоматически отрабатывает при обращении к атрибуту. """
        print(f"__getattribute__ was called for item={item}")
        # или можно так: return object.__getattribute__(self, item)
        return super().__getattribute__(item)

    def __setattr__(self, key, value):
        """ Автоматически отрабатывает при присвоении атрибуту какого-либо значения. """
        print(f"__setattr__ was called for key={key}, val={value}")
        # или можно так: object.__setattr__(self, key, value)
        super().__setattr__(key, value)

    def __getattr__(self, item):
        """ Автоматически вызывается, если __getattribute__ не нашел аттрибута. """
        print("__getattr__ was called: " + item)
        return False

    def __delattr__(self, item):
        print(f"__delattr__ was called for item={item}")
        # или можно так: return object.__delattr__(self, item)
        return super().__delattr__(item)


p = Point(10, 20)
# __setattr__ was called for key=_Point__x, val=10
# __setattr__ was called for key=_Point__y, val=20

print(p.MIN_COORD)
# __getattribute__ was called for item=MIN_COORD
# 50

p.MIN_COORD = 3
# __setattr__ was called for key=MIN_COORD, val=3

print(p.qwe)
# __getattribute__ was called for item=qwe
# __getattr__ was called: qwe
#  False

del p.MIN_COORD
# __delattr__ was called for item=MIN_COORD
