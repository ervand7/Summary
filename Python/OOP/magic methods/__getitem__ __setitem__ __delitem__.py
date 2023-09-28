class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __getitem__(self, key: int):
        """
        Автоматически вызывается, когда мы обращаемся к экземпляру класса как к коллекции
        и пытаемся получить какое-то значение по ключу
        """
        if self.__check_cond(key):
            return self.values[key]
        else:
            raise IndexError('Index is out of range')

    def __setitem__(self, key: int, value):
        """
        Автоматически вызывается, когда мы обращаемся к экземпляру класса как к коллекции
        и пытаемся задать какое-то значение по ключу
        """
        if self.__check_cond(key):
            self.values[key] = value
        else:
            raise IndexError('Index is out of range')

    def __delitem__(self, key):
        """
        Автоматически вызывается, когда мы обращаемся к экземпляру класса как к коллекции
        и пытаемся удалить какое-то значение по ключу
        """
        if self.__check_cond(key):
            del self.values[key]
        else:
            raise IndexError('Index is out of range')

    def __check_cond(self, key):
        if key >= 0:
            return 0 <= key < len(self.values)
        return 0 < abs(key) <= len(self.values)


v = Vector(1, 2, 3, 4, 5)
print(v[3])  # 4
print(v[-1])  # 5
print(v[-5])  # 1

v[3] = 155
print(list(v))  # [1, 2, 3, 155, 5]

del v[0]
print(list(v))  # [2, 3, 155, 5]
