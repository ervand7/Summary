# реализуем арифметическую последовательность вещественных чисел
class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step

    def __next__(self):
        if (self.start + self.step) <= self.stop:
            current_value = self.start
            self.start += self.step
            return current_value
        raise StopIteration

    def __iter__(self):
        return self


fr = FRange(0, 2, 0.5)
print(type(fr))  # <class '__main__.FRange'>

print(next(fr))  # 0.0
print(next(fr))  # 0.5
print(next(fr))  # 1.0
print(next(fr))  # 1.5

# ничего не выведется, так как мы уже обходили итератор fr до этого 1 раз
for x in fr:
    print(x)
