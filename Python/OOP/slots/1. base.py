# 1) __slots__ collection prohibits instances to have more than set
# attributes.
# 2) __slots__ restricts only instances attributes. It does not
# restrict class attributes.
# 3) using __slots__ we lose magic method __dict__ and thanks to this, we save
# member.
# 4) __slots__ relates only to attributes, not to methods.
# 5) __slots__ speeds up work with local attrs

import timeit


class WithoutSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


class WithSlots:
    __slots__ = ('x', 'y')  # все другие атрибуты будут запрещены

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


# Объекты __slots__ занимают меньше места в памяти. Это преимущество, так как у объектов
# без __slots__ все атрибуты хранятся в словаре (__dict__), который тоже
# занимает место в памяти
withoutSlots = WithoutSlots(3, 4)
withSlots = WithSlots(3, 4)

print(withoutSlots.__sizeof__() + withoutSlots.__dict__.__sizeof__())  # 120
print(withSlots.__sizeof__())  # 32

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

print(withSlots.__slots__)  # ('x', 'y')
print(hex(id(WithSlots.__slots__)))  # 0x7fb89016c800
print(hex(id(withSlots.__slots__)))  # 0x7fb89016c800

# __slots__ does not restrict class attributes
WithSlots.Hello = "world"

# __slots__ speeds up work with local attrs
print(timeit.timeit(withoutSlots.calc))  # 0.22895575
print(timeit.timeit(withSlots.calc))  # 0.169595167
