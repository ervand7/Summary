def adder(value):
    def inner(n):
        return value + n

    return inner


a = adder(100)
print(a(2))  # 102
print(a(1))  # 101
print(a(10))  # 110
