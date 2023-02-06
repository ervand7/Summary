"""
Пример того, как можно использовать метакласс.
Сделаем так, что все наши public методы станут private.
"""


class AllPrivateMeta(type):
    def __new__(mcs, name: str, bases: tuple, attrs: dict) -> type:
        new_attrs = {}
        for i in attrs:
            new_name = i if i.startswith('__') else '__' + i
            new_attrs[new_name] = attrs[i]

        return super().__new__(mcs, name, bases, new_attrs)


class MyList(list, metaclass=AllPrivateMeta):
    def get_length(self):
        return len(self)


m = MyList()
print(m.__get_length())  # 0
