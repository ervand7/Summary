# можем спокойно пробрасывать ошибку вверх по стеку через raise

class ParentException(Exception):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.x = x
        self.y = y

    def __str__(self):
        return f"{ChildException.__name__}: {self.x}, {self.y}"


class ChildException(ParentException):
    pass


def first() -> None:
    try:
        second()
    except ParentException as err:
        print(hex(id(err)))  # 0x7fd4400df100
        print(isinstance(err, ParentException))  # True

        print(err)  # v


def second() -> None:
    try:
        third()
    except ChildException as err:
        print(hex(id(err)))  # 0x7fd4400df100
        raise err


def third() -> None:
    try:
        {"hello": "world"}[777]
    except KeyError as err:
        exc = ChildException(44, 55)
        print(hex(id(exc)))  # 0x7fd4400df100
        raise exc from err


first()
