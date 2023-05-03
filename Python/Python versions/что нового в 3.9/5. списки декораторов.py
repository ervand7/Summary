# 3.9
"""
Теперь декораторы можно помезать в списки, и устанавливать
декоратор через обращение к индексу списка.
"""


def decorator_h1(func):
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')

    return inner


def decorator_h2(func):
    def inner(*args, **kwargs):
        print('<h2>')
        func(*args, **kwargs)
        print('</h2>')

    return inner


lst = [decorator_h1, decorator_h2]


@lst[1]
def hello():
    print('hello')


hello()
# <h2>
# hello
# </h2>
