class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __getitem__(self, item: int):
        """
        Автоматически вызывается, когда мы обращаемся к экземпляру класса как к коллекции
        и пытаемся получить какое-то значение по ключу
        """
        if 0 <= item < len(self.values):
            return self.values[item]
        else:
            raise IndexError('Index is out of range')

    def __setitem__(self, key: int, value):
        """
        Автоматически вызывается, когда мы обращаемся к экземпляру класса как к коллекции
        и пытаемся задать какое-то значение по ключу
        """
        if 0 <= key < len(self.values):
            self.values[key] = value
        else:
            raise IndexError('Index is out of range')

    def __delitem__(self, key):
        """
        Автоматически вызывается, когда мы обращаемся к экземпляру класса как к коллекции
        и пытаемся удалить какое-то значение по ключу
        """
        if 0 <= key < len(self.values):
            del self.values[key]
        else:
            raise IndexError('Index is out of range')


v = Vector(1, 2, 3, 4, 5)
print(v[3])  # 4

v[3] = 155
print(list(v))  # [1, 2, 3, 155, 5]

del v[0]
print(list(v))  # [2, 3, 155, 5]
