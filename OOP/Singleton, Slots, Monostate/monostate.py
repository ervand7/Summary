"""
Изменяя значение атрибута одного экземпляра класса, мы можем изменять значение этого атрибута
сразу у всех других экземпляров класса.
Этого поведения нам удается добиться благодаря тому, что у всех экземпляров класса переменная
__dict__ будет ссылаться на один и тот же объект в памяти (в данном примере на hacked_dict).
И, если один экземпляр класса меняет состояние hacked_dict, то и значение всех __dict__ у остальных
экземпляров класса будет соответствовать текущему состоянию измененного hacked_dict.
"""

hacked_dict = {}


class Cat:
    def __init__(self):
        self.__dict__ = hacked_dict


a = Cat()
b = Cat()

a.breed = 'siam'
a.name = 'Bob'
a.surname = 'Jonson'

print(a.__dict__)  # {'breed': 'siam', 'color': 'black', 'name': 'Bob', 'surname': 'Jonson'}
print(b.__dict__)  # {'breed': 'siam', 'color': 'black', 'name': 'Bob', 'surname': 'Jonson'}
