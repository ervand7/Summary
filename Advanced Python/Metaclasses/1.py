"""
Для начала нужно понять, что MyList и MyList2 - это одно и тоже.
Просто во втором примере показано то, как класс создается под капотом
"""


class MyList(list):
    def get_length(self):
        return len(self)


MyList2 = type(
    'MyList',
    (list,),
    dict(my_length=lambda self: len(self))
)
