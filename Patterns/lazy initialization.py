# https://ru.wikipedia.org/wiki/Отложенная_инициализация
# Смотри также из моего конспекта:
# https://github.com/ervand7/Summary/blob/master/Modules/модуль%20functools/cashed_property.py

"""
Минусы этого паттерна:
1) обновление кеша и несоответствие кеша тому, что может поменяться на сервере
2) недетерминированное время выполнения прогнраммы
"""


class MyMetaClass(type):
    @property
    def my_data(cls):
        if getattr(cls, '_MY_DATA', None) is None:
            my_data = ...  # costly database call
            cls._MY_DATA = my_data
        return cls._MY_DATA


class MyClass(metaclass=MyMetaClass):
    pass
