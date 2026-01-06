"""
Behavior of the same method of class and his child must be the same.
So we can get expected result independent of calling method get_some
whether from Father or from Son.

However, this is point of contention, as this contradicts ability of overriding.
"""


class Father:
    def get_some(self):
        return 1


class Son(Father):
    pass


assert Father().get_some() == Son().get_some()
