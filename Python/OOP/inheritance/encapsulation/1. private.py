# we can not use private methods and attrs of parent class inside of child class

class Geom:
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f"инициализатор Geom для {self.__class__}")
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self.__fill = fill

        print(getattr(self, "__x1", "Not exists!"))  # Not exists!


r = Rect(0, 0, 10, 20)
# we see private attrs of parent class in child.__dict__
print(r.__dict__)  # {'_Geom__x1': 0, '_Geom__y1': 0, '_Geom__x2': 10, '_Geom__y2': 20, '_Rect__fill': 'red'}
