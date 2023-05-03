from collections import namedtuple
from datetime import datetime
from typing import NamedTuple


class Point:
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y


# имя класса (PointV2) должно совпадать с аргументом. Атрибуты перечисляются в строке через пробел
PointV2 = namedtuple('PointV2', 'x y')
p1 = PointV2(2, 3)
# теперь мы можем обращаться как по индексам, так и по названиям атрибутов
print(p1[0])  # 2
print(p1.x)  # 2

Human = namedtuple('Person', 'name surname date country')
print(Human)  # <class '__main__.Person'>
h = Human(name='Joseph', surname='Bauer', date='1980-05-19', country='Canada')
print(h)  # Person(name='Joseph', surname='Bauer', date='1980-05-19', country='Canada')
print(isinstance(h, (tuple, Human)))  # True

# методы namedtuple
print(h.count('Bauer'))  # 1
print(h.count('Baue'))  # 0
print(h._asdict())  # {'name': 'Joseph', 'surname': 'Bauer', 'date': '1980-05-19', 'country': 'Canada'}
print(h._fields)  # ('name', 'surname', 'date', 'country')

# namedtuple, как и обычный кортеж, поддерживает неизменяемость
h.name = 'qwewfewfwe'  # AttributeError: can't set attribute

# но в namedtuple мы все же можем изменять значения атрибутов через _replace
h._replace(name='Ivan')


# чтобы поддерживать аннотацию типов мы можем создать класс и наследоваться
#  от NamedTuple из модуля typing

class AnnotatedPerson(NamedTuple):
    name: str
    surname: str
    date: datetime
    country: str


AnnotatedPerson(name='Joseph', surname='Bauer', date=datetime.now(), country='Canada')
