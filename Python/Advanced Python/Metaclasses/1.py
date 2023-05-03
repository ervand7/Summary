"""
Для начала нужно понять, что MyList и newMyList - это одно и тоже.
Просто во втором примере показано то, как класс создается под капотом
"""


class MyList(list):
    def get_length(self):
        return len(self)


newMyList = type(
    'MyList',
    (list,),
    dict(get_length=lambda self: len(self))
)
