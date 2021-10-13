# # |||||||||||||||||||||||||||||||||||||||||||||||||
# Базовые методы. Материал из уроков 1-6
from pprint import pprint


# • isinstance - проверить принадлежность объекта к классу. Первым параметром передаем объект, вторым
# класс, который хотим проверить
# print(isinstance(4, int))
# print(isinstance(list, object))


# • Объявление класса
class Car:
    pass


# • Создание экземпляра класса
a = Car()


# • Функция dir, которая показывает нам список магических методов,
# которые мы можем применить к экземпляру класса
# pprint(dir(a))

# • Теперь, после создания экземпляра класса, проверить принадлежность можно через type
# print(type(a))


# • Создание атрибута класса
class Car:
    model = 'BMW'
    engine = 1.6


# • Обращение к атрибуту класса
# print(Car.model)

# • Редко применяемое обращение к атрибуту класса. Тут атрибут берем в кавычки
# print(getattr(Car, 'model'))

# • Посмотреть все атрибуты, существующие в классе
# pprint(Car.__dict__)

# • .__sizeof__() Узнать, какое место в памяти занимает элемент
# print(Car.__dict__.__sizeof__())

# • Задаем значение атрибута класса
Car.color = 'black'

# • Редко применяемый способ задать значение атрибута класса. Тут тоже кавычки нужны
setattr(Car, 'window', 200)

# • Удаляем атрибут
del Car.color

# • Редко применяемый способ удалить атрибут класса. Тут тоже кавычки нужны
delattr(Car, 'window')


# • issubclass. Проверка наследования
class Home:
    pass


class Table(Home):
    pass


# print(issubclass(Table, Home))


# Базовые методы. Материал из уроков 1-6
# # |||||||||||||||||||||||||||||||||||||||||||||||||


# # |||||||||||||||||||||||||||||||||||||||||||||||||
# Конструктор и деструктор
class MyPoint:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        print('Удаление экземпляра: ' + self.__str__())


# pt = MyPoint()
# Конструктор и деструктор
# # |||||||||||||||||||||||||||||||||||||||||||||||||


# # |||||||||||||||||||||||||||||||||||||||||||||||||
#  Урок №7 Практика. Создание класса и его методов
from math import sqrt


class Point:
    list_points = []

    def __init__(self, coord_x=0, coord_y=0):
        self.x = coord_x
        self.y = coord_y
        Point.list_points.append(self)  # вот таким образом мы можем достучаться до
        # переменых (атрибутов класса) в функциях
        print(Point.list_points)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.x = 0
        self.y = 0

    def print_point(self):
        print(f'Точка с координатами ({self.x}, {self.y})')

    def calc_distance(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError('Аргумент должен принадлежать классу Точка')
        return sqrt((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2)


# p5 = Point()
# p5.print_point()
# p5.move_to(7, -43)
# p5.print_point()
#
# p7 = Point(6, 0)
# p8 = Point(0, 8)

# print(p7.calc_distance(p8))

#  Урок №7 Практика. Создание класса и его методов
# # |||||||||||||||||||||||||||||||||||||||||||||||||


# # |||||||||||||||||||||||||||||||||||||||||||||||||
# #  Урок №8 МОНОСОСТОЯНИЕ
# # Смысл в том, что изменяя значение атрибута одного экземпляра класса,
# # мы можем изменять сразу все значения атрибутов других экземпляров в классе.
# # Здесь работает жесткая схема, ее просто надо выучить:
class Cat:  # сразу после объявления класса, еще до создания методов пришем приватную переменную,
    # которая будет равна словарю, в котором прописываются атрибуты и их значения(аргументы)
    __shared_attr = {  # Обязательно должна быть приватная переменная
        'breed': 'pers',
        'color': 'black'
    }

    # далее все это инициализируется.
    def __init__(self):
        self.__dict__ = Cat.__shared_attr


d = Cat()
g = Cat()

d.breed = 'siam'
d.name = 'Bob'


# h = Cat()


# #  Урок №8 МОНОСОСТОЯНИЕ
# # |||||||||||||||||||||||||||||||||||||||||||||||||


# # |||||||||||||||||||||||||||||||||||||||||||||||||
# #  Урок №9 Инкапсуляция
# # Инкапсуляция - это сокрытие
# # Public, protected and private attr and methods
class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_private_data(self):
        print(self.__name, self.__balance, self.__passport)

    def print_public_data(self):
        self.__print_private_data()

    # Приватными могут быть и методы. Но к таким методам доступ будет только внутри класса
    def __print_private_data(self):
        print(self.__name, self.__balance, self.__passport)


account1 = BankAccount('Bob', 10000, 4545454545)


# account1.print_private_data()  # Вне класса получаем доступ, так как сам
# метод - публичный (см. первый метод после инит)


# account1.__print_private_data() # Доступ вне класса запрещен к приватным методам!
# Вне класса доступ к атрибутам запрещен
# print(account1.__name) # Доступ зпрещен!
# print(account1.__balance) # Доступ зпрещен!
# print(account1.__passport) # Доступ зпрещен!

# account1.print_public_data()  # так мы получаем защищенные данные методом print_public_data(), дергая
# внутри метод __print_private_data()

# Проверив с помощью dir возможные домтупные методы мы видим 2 черных метода с доступом к приватным данным
# pprint(dir(account1))
# account1._BankAccount__print_private_data()  # Черный метод №1. Он подкрашивается, но будет работать
# print(account1._BankAccount__balance)  # Черный метод №2. Он подкрашивается, но будет работать

# # Чтобы полностью доступ закрыть нужно воспользоваться accessify и его
# декораторами protected and private, но это нужно гуглить
# #  Урок №9 Инкапсуляция
# # |||||||||||||||||||||||||||||||||||||||||||||||||


# # |||||||||||||||||||||||||||||||||||||||||||||||||
# #  Урок №10 Property, getter-метод и setter-метод

class BankAccount2:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print('get balance method')
        return self.__balance

    def set_balance(self, value):
        print('set balance method')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    def delete_balance(self):
        print('delete balance method')
        del self.__balance

    # property - это фишка питона по созданию свойства. Используется с комбинацией fget, fset, fdel

    # План создания такой:
    # 1) Прописываем название нашего свойства. Помним, что это св-во будет выполнять одновременно множество функций
    # 2) Прописываем, что наше св-во равно property и открываем скобки.
    # Пример: balance = property(
    # 3) Прописываем внутри скобок fget, fset, fdel и приравниваем их к нужным нам методам.
    # Например: fget=get_balance, fset=set_balance и тд.
    # 4) И в. итоге мы получаем:
    balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)


# # 5) Важно!!! При вызове свойства мы не используем (). Пример: del d.balance
# d = BankAccount('Masha', 400)
# print(d.balance)  # тут мы применяем метод get_balance. Обратите внимание, что balance - это свойство,
# # а не что либо другое. Мы к нему обращаемся без вызова ()
# d.balance = 789  # тут мы применяем метод set_balance
# # d.balance =  'qwe' # Проверяем на правильность ввода данных
# del d.balance  # проверяем работу метода delete_balance
# d.balance = 8  # снова используем set_balance
# print(d.balance)  # снова используем get_balance
# del d.balance  # проверяем работу метода delete_balance
# print(d.balance)  # пытаемся использовать get_balance и получаем ошибку

# #  Урок №10 Property, getter-метод и setter-метод
# # |||||||||||||||||||||||||||||||||||||||||||||||||


# # |||||||||||||||||||||||||||||||||||||||||||||||||
# # Урок №25 Наследование
class Person:  # parent
    def can_think(self):
        print('Я могу думать')

    def can_walk(self):
        print('Я могу ходить')


class Doctor(Person):  # subclass
    def can_cure(self):
        print('Я могу лечить')


class Orthopedist(Doctor):
    pass


class Architect(Person):  # subclass
    def can_build(self):
        print('Я могу построить здание')


# d = Doctor()
# d.can_cure()
# d.can_think()
# d.can_walk()
# print()

# v = Architect()
# v.can_build()
# v.can_think()
# v.can_walk()
# print()

# e = Orthopedist()
# e.can_walk()
# e.can_think()
# e.can_cure()


# print()
# print(issubclass(Doctor, Person))
# print(isinstance(d, Person))
# # Урок №25 Наследование
# # |||||||||||||||||||||||||||||||||||||||||||||||||


# # |||||||||||||||||||||||||||||||||||||||||||||||||
# # Урок №26 АЗЫ АЗОВ!!!! Наследование от object и от других встроенных типов. object parent class Python


class Person2:
    pass


class MyList2(list):
    pass


class Doctor2(Person2):
    pass


class Architect2(Person2):
    pass


# # в Python все является object
# print(isinstance((3, 4), object))
# print(issubclass(int, object))
# print(isinstance(int, object))
# print(issubclass(Person2, object))
# # pprint(dir(object))
# pprint(dir(Person))

t = MyList2()


# print(t)

# # Урок №26  АЗЫ АЗОВ!!!! Наследование от object и от других встроенных типов. object parent class Python
# # |||||||||||||||||||||||||||||||||||||||||||||||||


# # |||||||||||||||||||||||||||||||||||||||||||||||||
# # Урок №27 Переопределение методов в Python. Method overriding in Python
# # Переопределить метод - это значит внутри дочернего класса создать метод с таким же названием,
# как и у родительского класса, но задать ему совершенно другое поведение.

# # Переопределить атрибут - это значит внутри дочернего класса создать атрибут с таким же
# названием, как и у родительского класса, но задать ему совершенно другое значение.
class Person3:

    def __init__(self, name):
        # print('init вызывается у Person3')
        self.name = name

    def breathe(self):
        print('Человек дышит')

    def walk(self):
        print('Человек идет')

    def __str__(self):
        return f'Person {self.name}'

    def sleep(self):
        print('Человек спит')

    def combo(self):
        self.breathe()
        self.walk()
        self.sleep()


class Doctor3(Person3):  # subclass
    def breathe(self):
        print('Доктор дышит')

    def __str__(self):
        return f'Doctor {self.name}'


# d = Doctor3('John')
# p = Person3('Adam')
# print(p.name, d.name)
# d.combo()


# # Урок №27 Переопределение методов в Python. Method overriding in Python
# # |||||||||||||||||||||||||||||||||||||||||||||||||


# # |||||||||||||||||||||||||||||||||||||||||||||||||
# # Урок Полиморфизм https://www.youtube.com/watch?v=9qr3neFX0Rs&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=14
# # • • • • Вариант 1 - порочная практика. Из-за этого и придумали полиморфизм!
class Rectangle:  # прямоугольник
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_per_rectangle(self):  # метод возвращает периметр прямоугольника
        return 2 * (self.w + self.h)


class Square:  # квадрат
    def __init__(self, a):
        self.a = a

    def get_per_sq(self):  # метод возвращает периметр квадрата
        return 4 * self.a


r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)
# print(r1.get_per_rectangle(), r2.get_per_rectangle())

s1 = Square(10)
s2 = Square(20)
# print(s1.get_per_sq(), s2.get_per_sq())

geom = [r1, r2, s1, s2]


# Ниже указана ПОРОЧНАЯ, плохая практика в программировании
# for g in geom:
#     if isinstance(g, Rectangle):
#         print(g.get_per_rectangle())
#     else:
#         print(g.get_per_sq())

# print()


# ``````````````````````````````````````````````````````````````````
# # • • • • Вариант 2 - хороший вариант с применением полиморфизма:
class Rectangle:  # прямоугольник
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_perimeter(self):  # метод возвращает периметр прямоугольника
        return 2 * (self.w + self.h)


class Square:  # квадрат
    def __init__(self, a):
        self.a = a

    def get_perimeter(self):  # метод возвращает периметр квадрата
        return 4 * self.a


class Triangle:  # треугольник
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):  # метод возвращает сумму всех сторон треугольника
        return self.a + self.b + self.c


# # Полиморфизм - это то, что мы всем этим трём методам дали одинаковое название get_we_need. И все!

r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)

s1 = Square(10)
s2 = Square(20)

t1 = Triangle(1, 2, 3)
t2 = Triangle(4, 5, 6)

geom2 = [r1, r2, s1, s2, t1, t2]


# Ниже указана нормальная практика с применением полиморфизма
# for g in geom2:
#     print(g.get_perimeter())

# # Урок Полиморфизм https://www.youtube.com/watch?v=9qr3neFX0Rs&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=14
# # |||||||||||||||||||||||||||||||||||||||||||||||||


# # Урок №28 Extending |||||||||||||||||||||||||||||||||||||||||||||||||
# # extending - это не что иное как создание в дочернем классе атрибутов, которых нет в родительском
# # Урок №28 Extending |||||||||||||||||||||||||||||||||||||||||||||||||


# # |||||||||||||||||||||||||||||||||||||||||||||||||
# # Урок №30 Множественное наследование. __mro__. Multiple inheritance in Python
# # Смысл в том, что сначала при вызове одинаковых методов родительских классов система сначала будет
# # искать в классе, который первым прописан как родитель

# # Правило использования super():
# # 1) Пришем super(). точку обязательно ставим
# # 2) Прописываем метод родительского класса, который хотим вызвать
# # 3) Прописываем, если нужно, в скобках аргументы этого матода родительского класса
class Doctor5:
    def can_cure(self):
        print('Я доктор, я умею лечить')

    def graduate(self):
        print('Ура! Я отучился на доктора')

    def can_build(self):
        print('Я доктор, я тоже умею строить, но не очень')


class Builder5:
    def can_build(self):
        print('Я строитель, я умею строить')

    def graduate(self):
        print('Ура! Я отучился на строителя')


class Person5(Doctor5, Builder5):
    def graduate(self):
        print('Посмотрим, кем я стал')
        super().graduate()
        Builder5.graduate(self)  # это нужно в том лишь случае6 если мы хотим, чтобы вывелся метод и
        # у второго записанного родителя


s = Person5()


# s.can_build()
# s.can_cure()
# pprint(Person5.__mro__)  # показывает летсницу насленования
# s.graduate()


# # Урок №30 Множественное наследование. __mro__. Multiple inheritance in Python
# # |||||||||||||||||||||||||||||||||||||||||||||||||


# # |||||||||||||||||||||||||||||||||||||||||||||||||
# # Урок №15 ООП Магические методы __str__ и __repr__
# # __repr__ нужен для того, чтобы предоставлять информацию строкой для разработчиков
# # __str__ нужен для того, чтобы предоставлять информацию строкой для пользователей
class Lion:
    def __init__(self, name):
        self.name = name

    # def __repr__(self):
    #     return f'The object Lion - {self.name}'

    def __str__(self):
        return f'Lion - {self.name}'


L = Lion('Simba')
w = Lion('Vasya')


# print(L)
# print(w)


# # Урок №15 ООП Магические методы __str__ и __repr__
# # |||||||||||||||||||||||||||||||||||||||||||||||||


# # |||||||||||||||||||||||||||||||||||||||||||||||||
# # Урок №16 Магические методы __len__ и. __abs__ (Dander methods)
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __len__(self):
        return len(self.name + self.surname)  # Конкатенация


e = Person('qwe', 'asd')


# print(e.__len__())
# print()


class Otrezok:
    def __init__(self, point1, point2):
        self.x1 = point1
        self.x2 = point2

    def __len__(self):
        return abs(self)  # self.__abs__()

    def __abs__(
            self):  # В данном примере мы используем __abs__ для вычитания из меньшего числа
        # большего, а также, если одно из значений отрицательное
        return abs(self.x2 - self.x1)


q = Otrezok(3, 9)
# print(len(q))
# # или
# print(q.__len__())

s = Otrezok(10, 2)


# print(len(s))
# # или
# print(w.__len__())

# # Урок №16 Магические методы __len__ и. __abs__ (Dander methods)
# # |||||||||||||||||||||||||||||||||||||||||||||||||


# # |||||||||||||||||||||||||||||||||||||||||||||||||
# # Урок №17 Магические методы __add__, __mul__, __sub__ и __truediv__
class BankAccount7:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        if isinstance(other, BankAccount7):  # we want to directly add a7 to b7
            return self.balance + other.balance
        if isinstance(other, (int, float)):  # we want for example add a7 + 3
            return self.balance + other
        raise NotImplemented  # for all other cases

    def __radd__(self, other):  # 'magic method rite add'. If we want change places variables. Example 10 + a7
        return self + other


a7 = BankAccount7('Anya', 12)
b7 = BankAccount7('Vanya', 15)


# print(a7.__add__(b7))
# print(10 + b7)  # here calling method __radd__
# # the remaining methods (__mul__, __sub__ и __truediv__) we can implement according to the same principle
# # Урок №17 Магические методы __add__, __mul__, __sub__ и __truediv__
# # |||||||||||||||||||||||||||||||||||||||||||||||||


# # |||||||||||||||||||||||||||||||||||||||||||||||||
# # Урок №23 Магические методы __getitem__ , __setitem__ и __delitem__. Обращение по индексу к экземпляру
class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __getitem__(self, item):  # item in this case means index from variable self.values
        if 0 <= item <= len(self.values):
            return self.values[item]
        else:
            raise IndexError('Index is out of range our collection')

    def __setitem__(self, key, value):  # where 'key' is index, which you want to change, 'value' is a new value
        if 0 <= key <= len(self.values):
            self.values[key] = value
        else:
            raise IndexError('Index is out of range our collection')

    def __delitem__(self, key):
        if 0 <= key <= len(self.values):
            del self.values[key]
        else:
            raise IndexError('Index is out of range our collection')


v = Vector(1, 2, 3, 4, 5)
# print(v[3])

v[3] = 155
# print(list(v))

del v[0]


# print(list(v))

# # Урок №23 Магические методы __getitem__ , __setitem__ и __delitem__. Обращение по индексу к экземпляру
# # |||||||||||||||||||||||||||||||||||||||||||||||||


# # |||||||||||||||||||||||||||||||||||||||||||||||||
# # Урок 19 Магические методы __eq__ и __hash__
class Point10:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point10) and self.x == other.x and self.y == other.y

    #  BUT AFTER CREATING OF THIS FUNCTION WE LOSE HASH VALUE OF BOTH VARIABLES
    # so we can restore hash function

    def __hash__(self):
        return hash((self.x, self.y))


p10 = Point10(2, 3)
p11 = Point10(2, 3)


# # we can see, that ids of variables are different
# print(id(p10))
# print(id(p11))
#
# # but thanks to the function we created __eq__
# print(p10 == p11)  # values are equal
#
# print(hash(p11))

# # Урок 19 Магические методы __eq__ и __hash__
# # |||||||||||||||||||||||||||||||||||||||||||||||||


# # |||||||||||||||||||||||||||||||||||||||||||||||||
# # Урок 18 Специальные методы сравнения объектов классов
# __eq__ (equal) отвечает за ==
# __ne__ (not equal) отвечает за !=
# __lt__ (less than) отвечает за <
# __le__ (less equal) отвечает за <=
# __gt__ (greater than) отвечает за >
# __ge__ (greater equal) отвечает за >=

class Tracks3:
    def __init__(self, duration):
        self.duration = duration

    def __eq__(self, other):
        if isinstance(other, Tracks3):
            return self.duration == other.duration

    def __lt__(self, other):
        return self.duration < other.duration

    def __le__(self, other):
        return self.duration <= other.duration

    def __gt__(self, other):
        return self.duration > other.duration

    def __ne__(self, other):
        return self.duration != other.duration

    def __ge__(self, other):
        return self.duration >= other.duration


track1 = Tracks3(12)
track2 = Tracks3(14)
track3 = Tracks3(12)


# print(track1 == track3)
# print(track1 < track2)
# print(track3 <= track2)
# print(track3 != track2)
# print(track1 >= track3)

# # Урок 18 Специальные методы сравнения объектов классов
# # |||||||||||||||||||||||||||||||||||||||||||||||||
