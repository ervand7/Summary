class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        if isinstance(other, BankAccount):  # we want to directly add b to b2
            return self.balance + other.balance
        if isinstance(other, (int, float)):  # we want for example add b + 3
            return self.balance + other
        raise NotImplemented  # for all other cases

    def __radd__(self, other):
        """
        Magic method right add.
        If we want change places variables. Example 10 + b
        """
        print('__radd__ called')
        return self + other


b = BankAccount('Anya', 12)
b2 = BankAccount('Vanya', 15)

print(b.__add__(b2))
print(10 + b2)  # here calling method __radd__

"""
The remaining methods 
__mul__ (__rmul__)
__sub__ (__rsub__)
__truediv__ (__rtruediv__)
we can implement according to the same principle
"""

