# By themselves, classes and class instances are hashable. But if we define
# __eq__ for them, then they cease to be hashable. So we also need to
# define the __hash__ method

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __hash__(self):
        """
        So we can restore hash function.
        """
        return hash((self.x, self.y))


p1 = Point(2, 3)
p2 = Point(2, 3)

# we can see, that address of variables are different
print(hex(id(p1)))  # 0x7ff63812ffd0
print(hex(id(p2)))  # 0x7ff63812ff10

# but hashes are equals
print(hash(p1))  # 8409376899596376432
print(hash(p2))  # 8409376899596376432

# and thanks __eq__, we can have custom comparing
print(p1 == p2)  # True

# hashes are equal. So in dict we will see only one obj
print({p1: 1, p2: 2})  # {<__main__.Point object at 0x7fa1e8196eb0>: 2}
