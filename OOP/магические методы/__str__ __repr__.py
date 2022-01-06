"""
__repr__ нужен, чтобы предоставлять информацию строкой для разработчиков
__str__ нужен, чтобы предоставлять информацию строкой для пользователей

Здесь описаны тонкие различия между __str__ и __repr__:
https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr
"""


class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'The object Lion - {self.name}'

    def __str__(self):
        return f'Lion - {self.name}'


L = Lion('Simba')
w = Lion('Vasya')

print(L)
print(w)
