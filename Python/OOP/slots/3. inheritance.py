# 1) by default, instance does not inherit __slots__
# 2) you should use `__slots__ = ()` in instance class to inherit __slots__

class Shape:
    __slots__ = 'wight', 'height'

    def __init__(self, value_1, value_2):
        self.wight = value_1
        self.height = value_2


class Square(Shape):
    pass


square = Square(1, 2)
print(square.__dict__)  # {}
square.qwerty = 150  # OK
print(square.qwerty)  # 150

# a subtle point needs to be taken into account:
del square.wight
square.wight = 999
print(square.__dict__)  # {'qwerty': 150}


class SquareWithSlots(Shape):
    __slots__ = ()

    def __init__(self, x, y):
        super(SquareWithSlots, self).__init__(value_1=x, value_2=y)


square_with_slots = SquareWithSlots(1, 2)

try:
    print(square_with_slots.__dict__)  # 'WithSlots' object has no attribute '__dict__'
except AttributeError as ex:
    print(ex)  # 'SquareWithSlots' object has no attribute '__dict__'
