"""
Создадим метакласс.
"""


class MyMeta(type):
    def __init__(cls, name, bases, attrs):
        print('Ervand created {}'.format(cls))
        super(MyMeta, cls).__init__(name, bases, attrs)


class MyList(list, metaclass=MyMeta):
    def get_length(self):
        return len(self)


# у всех обычных классов метакласс по умолчанию - это type. По факту мы его просто подменяем
m = MyList()  # Ervand created <class '__main__.MyList'>
