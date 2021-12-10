# https://ru.wikipedia.org/wiki/Отложенная_инициализация


class MyMetaClass(type):
    @property
    def my_data(cls):
        if getattr(cls, '_MY_DATA', None) is None:
            my_data = ...  # costly database call
            cls._MY_DATA = my_data
        return cls._MY_DATA


class MyClass(metaclass=MyMetaClass):
    pass
