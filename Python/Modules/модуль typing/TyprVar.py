from typing import Type, TypeVar


class Parent:
    pass


class Child(Parent):
    pass


# Есть еще такой вариант. Обозначаем, что ждем Parent и все его дочерние классы
T = TypeVar("T", bound=Parent)


def factory_obj(cls: Type[T]) -> T:
    return cls()


a: Parent = factory_obj(Parent)
b: Child = factory_obj(Child)
