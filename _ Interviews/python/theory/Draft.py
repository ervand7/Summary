import weakref


class MyClass:
    pass


obj = MyClass()
callback = weakref.WeakMethod(obj.my_method)
