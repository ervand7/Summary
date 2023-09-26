from typing import Type


# Type - означает сам класс (или его наследники)
# отсутствие Type будет означать экземпляр класса (или экземпляры его наследников)

class Parent:
    pass


class Child(Parent):
    pass


# получаем сам класс и возвращаем экземпляр
def factory_obj(cls: Type[Parent]) -> Parent:
    return cls()


a = factory_obj(Parent)
b = factory_obj(Child)
