from abc import ABC, abstractmethod


# Define an abstract class (shape) with an abstract method (area)
class Shape(ABC):
    @abstractmethod
    def get_perimeter(self):
        raise NotImplemented


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_perimeter(self):  # метод возвращает периметр прямоугольника
        return 2 * (self.w + self.h)


class Square(Shape):
    def __init__(self, a):
        self.a = a

    def get_perimeter(self):  # метод возвращает периметр квадрата
        return 4 * self.a


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):  # метод возвращает сумму всех сторон треугольника
        return self.a + self.b + self.c


r = Rectangle(1, 2)
s = Square(10)
t = Triangle(1, 2, 3)

for i in (r, s, t):
    print(i.get_perimeter(), end=' ')  # 6 40 6
