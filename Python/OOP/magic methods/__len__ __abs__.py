# for using len() and abs() for instance

class Point:
    def __init__(self, *args):
        self.coords = args

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        return list(map(abs, self.coords))


p = Point(22, -33)
print(len(p))  # 2
print(abs(p))  # [22, 33]
