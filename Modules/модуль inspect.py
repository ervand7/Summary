# основная статья: http://www.ilnurgi1.ru/docs/python/modules/inspect.html
import inspect

"""Получить информацию о стеке интерпретатора можно с помощью функции inspect.stack(). Она возвращает список кортежей, 
в которых есть следующие элементы: (фрейм–объект, имя_файла, строка_в_файле, имя_функции, список_строк_исходного_кода, 
номер_строки_в_коде)"""
print(inspect.stack())


class Person:
    def __new__(cls, *args, **kwargs):
        super(Person, self).__new__()

    def __init__(self):
        pass


a = inspect.getsource(Person)
print(a)
