class C(object):
    def __init__(self):
        self._x = None

    def getx(self):
        print('getter called')
        return self._x

    def setx(self, value):
        print('setter called')
        self._x = value

    def delx(self):
        print('deleter called')
        del self._x

    x = property(fget=getx, fset=setx, fdel=delx, doc="I'm the 'x' property.")


c = C()
c.x = 'Hello'
# setter called

print(c.x)
# getter called
# Hello

del c.x
# deleter called
