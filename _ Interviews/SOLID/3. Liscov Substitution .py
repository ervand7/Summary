"""
Objects of a superclass must be replaceable with objects of its subclass
without breaking the correctness of the program.

This does NOT mean methods cannot be overridden.
It means overriding must preserve the expected behavior (the contract).
"""


class Father:
    def get_value(self) -> int:
        return 1


class Son(Father):
    # Overriding is allowed as long as the contract is preserved
    def get_value(self) -> int:
        return 1


def use(obj: Father) -> int:
    return obj.get_value()


# Substitution works
assert use(Father()) == 1
assert use(Son()) == 1
