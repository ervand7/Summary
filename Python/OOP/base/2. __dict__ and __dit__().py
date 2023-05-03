from pprint import pprint
from math import sqrt


class Point:
    list_points = []

    def __init__(self, coord_x=0, coord_y=0):
        self.x = coord_x
        self.y = coord_y
        Point.list_points.append(self)  # вот таким образом мы можем достучаться до
        # переменных (атрибутов класса) в функциях
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


# __dict__ - встроенный аттрибут класса с подробным описанием адресов памяти атрибутов
# и методов класса
pprint(Point.__dict__)
"""
mappingproxy({'__dict__': <attribute '__dict__' of 'Point' objects>,
              '__doc__': None,
              '__init__': <function Point.__init__ at 0x7fb3c22a0b80>,
              '__module__': '__main__',
              '__weakref__': <attribute '__weakref__' of 'Point' objects>,
              'calc_distance': <function Point.calc_distance at 0x7fb3c34bd0d0>,
              'go_home': <function Point.go_home at 0x7fb3c349ef70>,
              'list_points': [<__main__.Point object at 0x7fb3c222cee0>,
                              <__main__.Point object at 0x7fb3c206abe0>,
                              <__main__.Point object at 0x7fb3c3483cd0>],
              'move_to': <function Point.move_to at 0x7fb3c349eee0>,
              'print_point': <function Point.print_point at 0x7fb3c34bd040>})
"""

# __dir__() - встроенная функция, которая показывает список доступных магических
# методов, а также методы и аттрибуты самого класса
pprint(Point().__dir__())
"""
['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 'calc_distance',
 'go_home',
 'list_points',
 'move_to',
 'print_point']
"""
