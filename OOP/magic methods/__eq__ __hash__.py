class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        """
        Problem:
        After creating of __eq__ function we lose hash value
        of both variables (self.x, self.y).
        """
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __hash__(self):
        """
        So we can restore hash function.
        """
        return hash((self.x, self.y))


p1 = Point(2, 3)
p2 = Point(2, 3)

# we can see, that ids of variables are different
print(id(p1))  # 140255162496048
print(id(p2))  # 140255162529584

# but thanks to the function we created __eq__
print(p1 == p2)  # True

print(hash(p2))  # 8409376899596376432
