"""
Делегирование в Python. Функция super(). Delegating methods in python
Функция super() позволяет вызвать в дочернем классе помимо текущей функции
одноименную функцию родительского класса (другими словами - произвести делегирование).
Принято вызывать эту функцию до исполнения аналогичной в дочернем классе.

1) после super() прописываем метод родительского класса, который хотим вызвать
2) прописываем, если нужно, в скобках аргументы этого матода родительского класса
"""


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.age = 50
        self.wight = 100

    def breathe(self):
        print('Человек дышит')


class Doctor(Person):
    def __init__(self, name, surname, age):
        super().__init__(name=name, surname=surname)
        # если бы прописали self.age до super(), то 25 перезатерлось бы на 50
        self.age = age

    def breathe(self):
        super().breathe()
        print('Доктор дышит')


semen = Doctor('Семен', 'Семенов', 25)

print(semen.name, semen.surname, semen.age, semen.wight)
semen.breathe()
