# we can use protected methods and attrs of parent class inside of child class

class Geom:
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f"инициализатор Geom для {self.__class__}")
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self._fill = fill

        print(getattr(self, "_x1"))  # 15


r = Rect(15, 0, 10, 20)
# we see protected attrs of parent class in child.__dict__
print(r.__dict__)  # {'_x1': 15, '_y1': 0, '_x2': 10, '_y2': 20, '_fill': 'red'}
