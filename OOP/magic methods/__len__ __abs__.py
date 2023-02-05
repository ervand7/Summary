class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __len__(self):
        return len(self.name + self.surname)  # Конкатенация


p = Person('Петр', 'Иванов')
print(p.__len__())


class Snippet:
    def __init__(self, point1, point2):
        self.x1 = point1
        self.x2 = point2

    def __len__(self):
        return abs(self)  # тут вызовется self.__abs__()

    def __abs__(self):
        """
        В данном примере мы используем __abs__ для вычитания из меньшего числа
        большего, а также, если одно из значений отрицательное.
        """
        return abs(self.x2 - self.x1)


s = Snippet(3, 9)
print(len(s))

s = Snippet(10, 2)
print(len(s))
