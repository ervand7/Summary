# for iter() and next()

class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step

    def __next__(self):
        print("__next__ called", end=" ")
        if (self.start + self.step) <= self.stop:
            current_value = self.start
            self.start += self.step
            return current_value
        raise StopIteration

    def __iter__(self):
        """
        Вызовется при iter(instance).
        Без этого метода нельзя использовать instance при обходе через цикл.
        Однако можно обойтись без него при использовании next(instance), но лучше все таки
        всегда его определять вместе с __next__.
        """
        return self


fr = FRange(0, 2, 0.5)
print(type(fr))  # <class '__main__.FRange'>

print(fr)  # <__main__.FRange object at 0x7f92f8175fd0>
print(iter(fr))  # <__main__.FRange object at 0x7f87b8175fd0>

print(next(fr))  # __next__ called 0.0
print(next(fr))  # __next__ called 0.5
print(next(fr))  # __next__ called 1.0
print(next(fr))  # __next__ called 1.5

# ничего не выведется, так как мы уже обходили итератор fr до этого 1 раз
for x in fr:
    print(x)
