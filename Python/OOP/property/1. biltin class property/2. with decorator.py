class C(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        print('getter called')
        return self._x

    @x.setter
    def x(self, value):
        print('setter called')
        self._x = value

    @x.deleter
    def x(self):
        print('deleter called')
        del self._x


c = C()
c.x = 'Hello'
# setter called

print(c.x)
# getter called
# Hello

del c.x
# deleter called
