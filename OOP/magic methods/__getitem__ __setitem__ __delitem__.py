class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __getitem__(self, item: int):  # item in this case means index from variable self.values
        print('__getitem__ called')
        if 0 <= item <= len(self.values):
            return self.values[item]
        else:
            raise IndexError('Index is out of range our collection')

    def __setitem__(self, key: int, value):  # where 'key' is index, which you want to change, 'value' is a new value
        print('__setitem__ called')
        if 0 <= key <= len(self.values):
            self.values[key] = value
        else:
            raise IndexError('Index is out of range our collection')

    def __delitem__(self, key):
        print('__delitem__ called')
        if 0 <= key <= len(self.values):
            del self.values[key]
        else:
            raise IndexError('Index is out of range our collection')


v = Vector(1, 2, 3, 4, 5)
print(v[3])

v[3] = 155
print(list(v))

del v[0]

print(list(v))
