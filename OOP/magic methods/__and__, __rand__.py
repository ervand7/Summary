class Point:
    def __init__(self, x: set):
        self.x = x

    def __iter__(self):
        return iter(self.x)

    def __and__(self, other):
        return self.x.intersection(other)

    def __rand__(self, other):
        return self.x.intersection(other)


p = Point({1, 2, 3})
print(p.__and__({2, 3, 4}))  # {2, 3}

print({2, 3, 4}.intersection(p))  # {2, 3}
