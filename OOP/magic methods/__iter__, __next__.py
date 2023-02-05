# реализуем арифметическую последовательность вещественных чисел
class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration

    def __iter__(self):
        self.value = self.start - self.step
        return self


fr = FRange(0, 2, 0.5)
print(next(fr))  # 0.0
print(next(fr))  # 0.5
print(next(fr))  # 1.0
print(next(fr))  # 1.5

for x in fr:
    print(x)
# 0.0
# 0.5
# 1.0
# 1.5
