# Using magic method __slots__ we prohibit the class to have more than set attributes
# In this case we lose magic method __dict__ and thanks this we save member.
# __slots__ relates only to attributes, not to methods.
class WithoutSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class WithSlots:
    __slots__ = ('x', 'y')  # все другие атрибуты будут запрещены

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def say(self):
        print(self)


# Объекты __slots__ занимают меньше места в памяти. Это преимущество, так как у объектов
# без __slots__ все атрибуты хранятся в словаре (__dict__), который тоже
# занимает место в памяти
withoutSlots = WithoutSlots(3, 4)
withSlots = WithSlots(3, 4)

print(withoutSlots.__sizeof__(), withoutSlots.__dict__.__sizeof__())  # 32 88
print(withSlots.__sizeof__(), withSlots.__slots__.__sizeof__())  # 32 40

# проверим, что не получается создать новый атрибут у экземпляра класса WithSlots
# в отличие от WithoutSlots
withoutSlots.new_attribute = 3  # OK
try:
    withSlots.new_attribute = 3
except AttributeError as ex:
    print(ex)  # 'WithSlots' object has no attribute 'new_attribute'

# проверим, что теперь у экземпляра класса WithSlots нет аттрибута __dict__ (в отличие от WithoutSlots)
print(withoutSlots.__dict__)  # {'x': 3, 'y': 4, 'new_attribute': 3}

try:
    print(withSlots.__dict__)  # 'WithSlots' object has no attribute '__dict__'
except AttributeError as ex:
    print(ex)  # 'WithSlots' object has no attribute '__dict__'

# it does not affect class methods
withSlots.say()  # <__main__.WithSlots object at 0x7fb92001dd60>

print(withSlots.__slots__)  # ('x', 'y')
print(hex(id(WithSlots.__slots__)))  # 0x7fb89016c800
print(hex(id(withSlots.__slots__)))  # 0x7fb89016c800
