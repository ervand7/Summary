class Rectangle:
    __slots__ = 'wight', 'height'

    def __init__(self, value_1, value_2):
        self.wight = value_1
        self.height = value_2


class Square(Rectangle):
    pass


square = Square(1, 2)
# И тут мы видим весь парадокс ситуации. В экземпляре класса Square уже будет
# присутствовать переменная __dict__, несмотря на то, что в родительском классе
# его не было из-за __slots__
print(square.__dict__)  # {} ошибок нет
square.qwerty = 150  # OK
print(square.qwerty)  # 150


# Чтобы и в дочернем классе запретить создавать атрибуты, кроме тех, что в __slots__
# родительского класса, нам нужно заново прописать __slots__. Но тут не нужно
# прописывать заново атрибуты из кортежа __slots__, достаточно прописать пустой кортеж
class SquareWithSlots(Rectangle):
    __slots__ = ()

    def __init__(self, x, y):
        super(SquareWithSlots, self).__init__(value_1=x, value_2=y)


square_with_slots = SquareWithSlots(1, 2)

try:
    print(square_with_slots.__dict__)  # 'WithSlots' object has no attribute '__dict__'
except AttributeError as ex:
    print(ex)  # 'SquareWithSlots' object has no attribute '__dict__'
