"""
Пример того, как можно использовать метакласс.
Сделаем так, что все наши public методы станут private.
"""


class AllPrivateMeta(type):
    def __new__(mcs, name, bases, attrs):
        new_attrs = {}
        for attr_name in attrs:
            new_name = attr_name if attr_name.startswith('__') else '__' + attr_name
            new_attrs[new_name] = attrs[attr_name]

        return super().__new__(mcs, name, bases, new_attrs)


class MyList(list, metaclass=AllPrivateMeta):
    def get_length(self):
        return len(self)


m = MyList()
print(m.__get_length())
