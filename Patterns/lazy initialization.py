# https://ru.wikipedia.org/wiki/Отложенная_инициализация
# Смотри также из моего конспекта:
# https://github.com/ervand7/Summary/blob/master/Modules/модуль%20functools/cashed_property.py


class MyMetaClass(type):
    @property
    def my_data(cls):
        if getattr(cls, '_MY_DATA', None) is None:
            my_data = ...  # costly database call
            cls._MY_DATA = my_data
        return cls._MY_DATA


class MyClass(metaclass=MyMetaClass):
    pass
