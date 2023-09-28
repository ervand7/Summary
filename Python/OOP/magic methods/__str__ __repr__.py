"""
1) при методах print и str отрабатывает __str__. Если он не определен, то __repr__.
2) __repr__ обычно отрабатывает в консоли:
    >>> a = Lion("my")
    >>> a # The object Lion - my
"""


class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        """ Предоставляет инфо для отладки """
        return f'The object Lion - {self.name}'

    def __str__(self):
        """ Предоставляет инфо для вывода """
        return f'Lion - {self.name}'


a = Lion('Simba')
b = Lion('Vasya')

print(a)
print(b)
