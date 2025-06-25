"""
Переопределить метод - это значит внутри дочернего класса создать 
метод с таким же названием, как и у родительского 
класса, но задать ему совершенно другое поведение.

Переопределить атрибут - это значит внутри дочернего класса создать 
атрибут с таким же названием, как и у родительского класса, но 
задать ему совершенно другое значение.
"""


class Person:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Person {self.name}'

    def breathe(self):
        print('Человек дышит')

    def walk(self):
        print('Человек идет')

    def sleep(self):
        print('Человек спит')

    def combo(self):
        self.breathe()
        self.walk()
        self.sleep()


class Doctor(Person):
    def breathe(self):
        print('Доктор дышит')

    def __str__(self):
        return f'Doctor {self.name}'


d = Doctor('John')
p = Person('Adam')
print(p.name)
print(d.name)

d.combo()
# Доктор дышит
# Человек идет
# Человек спит
