class B1:
    pass


class B2:
    pass


def some_method(self):
    self.hello = 'world'
    print(self.__dict__)


newClass = type(
    'Point',
    (B1, B2),
    {'MAX_COORD': 100, 'some_method': some_method}
)

a = newClass()
a.some_method()  # {'hello': 'world'}
