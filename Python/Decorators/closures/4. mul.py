def mul(e):
    def inner(b):
        return e * b

    return inner


print(mul(5)(2))  # 10
print(mul(5)(3))  # 15
