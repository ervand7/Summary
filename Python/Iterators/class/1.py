class MyRange:

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __iter__(self):  # without this __iter__(self) it will be TypeError: 'MyRange' object is not iterable
        return self

    def __next__(self):
        if self.start == self.end:
            raise StopIteration

        current_value = self.start
        self.start += 1

        return current_value


for i in MyRange(1, 10):
    print(i, end=" ")

# 1 2 3 4 5 6 7 8 9
