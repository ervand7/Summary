def counter():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    print(hex(id(inner)))  # 0x7f78a001a0d0
    return inner


q = counter()
print(hex(id(q)))  # 0x7f78a001a0d0

print(q())  # 1
print(q())  # 2
print(q())  # 3
print(q())  # 4
