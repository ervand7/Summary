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
