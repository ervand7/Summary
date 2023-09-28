# for +=

class Point:
    def __init__(self, x: int):
        self.x = x

    def __iadd__(self, other):
        self.x += other
        return self


i = Point(1)
i += 5
print(i.x)
