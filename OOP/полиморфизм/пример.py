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


"""
Полиморфизм - это то, что мы всем этим трём методам дали 
одинаковое название get_we_need. И все!
"""

r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)

s1 = Square(10)
s2 = Square(20)

t1 = Triangle(1, 2, 3)
t2 = Triangle(4, 5, 6)

lst = [r1, r2, s1, s2, t1, t2]

for i in lst:
    print(i.get_perimeter(), end=' ')

# 6 14 40 80 6 15
