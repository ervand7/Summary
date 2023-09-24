# val not changes because we create a new var inside func

n = 1
print(hex(id(n)))  # 0x7fe78800e930


def some():
    n = 333
    print(hex(id(n)))  # 0x7fe7780b04f0


some()
print(n)  # 1
