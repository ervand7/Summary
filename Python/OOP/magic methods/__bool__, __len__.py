# 1) if __bool__ is not defined, __len__ will be called

class Point:
    def __init__(self, *args):
        self.data = args

    def __len__(self):
        return len(self.data)

    def __bool__(self):
        return bool(self.data)


a = Point()
print(bool(a))  # False
