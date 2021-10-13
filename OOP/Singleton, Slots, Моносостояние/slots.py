# Using magic method __slots__ we prohibit the class to have more than set attributes
# In this case we lose magic method __dict__ and to thanks this we save member
class WithoutSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class WithSlots:
    __slots__ = ('x', 'y')  # в __slots__ мы прописываем кортежем атрибуты. Все другие атрибуты будут запрещены

    def __init__(self, x, y):
        self.x = x
        self.y = y


# Объекты __slots__ занимают меньше места в памяти - это преимущество
a = WithoutSlots(3, 4)
b = WithSlots(3, 4)

# так как у объектов без __slots__ все атрибуты хранятся в словаре (__dict__), который тоже занимает место в памяти
# также преимущество в скорости выполнения операций
print(a.__sizeof__(), a.__dict__.__sizeof__())  # 32 88
print(b.__sizeof__())  # 32

# проверим, что не получается создать новый атрибут у экземпляра класса WithSlots (в отличие от WithoutSlots)
a.new_attribute = 3  # OK
# b.new_attribute = 3  # AttributeError: 'WithSlots' object has no attribute 'new_attribute'

# проверим, что теперь у экземпляра класса WithSlots нет аттрибута __dict__ (в отличие от WithoutSlots)
print(a.__dict__)  # {'x': 3, 'y': 4, 'new_attribute': 3}
# print(b.__dict__)  # 'WithSlots' object has no attribute '__dict__'


# _________________________________________________________________________________________________
# Обход запрета на Slots через @property
# С помощью @property мы можем формально обойти запрет от __slots__, так как то,
# что у нас будет под @property - будет уже свойством, а не атрибутом
class Ivan:
    __slots__ = 'height', 'weight'

    def __init__(self, value_1, value_2):
        self.height = value_1
        self.weight = value_2

    @property
    def height_weight_sum(self):
        return self.height + self.weight


ivan = Ivan(value_1=170, value_2=70)
print(ivan.height)  # 170
print(ivan.weight)  # 70
print(ivan.height_weight_sum)  # 240  /тут мы формально обошли запрет. Но тем не менее height_weight_sum -
# у нас все равно не атрибут, а свойство


# _________________________________________________________________________________________________
# Пример сложной логики присваивания значения инкапсулированным атрибутам через property
class Rectangle:
    __slots__ = '__wight', 'height'

    def __init__(self, value_1, value_2):
        self.wight = value_1  # здесь специально wight не инкапсулируется, чтобы вызывалась функция setter.
        # Потому что тут wight - это уже ссылка на свойство (функцию), находящееся под декоратором @property.
        # Именно в этот момент у нас вызывается @wight.setter, который присваивает защищенному атрибуту __wight
        # значение. И далее мы будем получать значение этого __wight через getter
        self.height = value_2

    @property
    def wight(self):
        return self.__wight

    @wight.setter
    def wight(self, value):
        print('setter called')
        self.__wight = value


n = Rectangle(5, 6)  # setter called
print(n.wight)  # 5
# Но, несмотря на наличие свойства wight, у нас все еще имеется защищенный атрибут __wight,
# до которого мы можем достучаться через n._Rectangle__wight (редактор будет ругаться)
print(n._Rectangle__wight)  # 5


# _________________________________________________________________________________________________
# Slots: наследование
class Square(Rectangle):
    pass


square = Square(1, 2)  # setter called
# И тут мы видем весь парадокс ситуации. В экземпляре класса Square уже будет присутствовать переменная __dict__,
# несмотря на то, что в родительском классе это було запрещено из-за __slots__
print(square.__dict__)  # {}  /ошибок нет
square.qwerty = 150  # OK
print(square.qwerty)  # 150


# Чтобы и в дочернем классе запретить создавать атрибуты, кроме тех, что в __slots__ родительского класса, нам
# нужно заново прописать __slots__. Но тут не нужно прописывать заново атрибуты из кортежа __slots__
class SquareWithSlots(Rectangle):
    __slots__ = ()  # достаточно прописать пустой кортеж

    def __init__(self, x, y):
        super(SquareWithSlots, self).__init__(value_1=x, value_2=y)


square_with_slots = SquareWithSlots(1, 2)
# print(square_with_slots.__dict__)  # Видим, что уже не имеем attribute '__dict__'
# Видим, что у нас есть опять атрибуты из __slots__
print(square_with_slots.wight)  # 1
print(square_with_slots.height)  # 2
