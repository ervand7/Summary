def counter():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner


q = counter()
print(q())  # 1
print(q())  # 2
print(q())  # 3
print(q())  # 4
