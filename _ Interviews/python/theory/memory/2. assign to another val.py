a = 1
b = a
print(hex(id(a)))  # 0x7fe1d802e930
print(hex(id(b)))  # 0x7fe1d802e930
print(a == b)  # True

a = "hello"
b = a
print(hex(id(a)))  # 0x7fd69805b630
print(hex(id(b)))  # 0x7fd69805b630
print(a == b)  # True

a = (1, 2, 3)
b = a
print(hex(id(a)))  # 0x7fd0680cc980
print(hex(id(b)))  # 0x7fd0680cc980
print(a == b)  # True

a = [1, 2, 3]
b = a
print(hex(id(a)))  # 0x7fb16012ba40
print(hex(id(b)))  # 0x7fb16012ba40
print(a == b)  # True

a = {1, 2, 3}
b = a
print(hex(id(a)))  # 0x7fda5819f660
print(hex(id(b)))  # 0x7fda5819f660
print(a == b)  # True

a = {1: 2}
b = a
print(hex(id(a)))  # 0x7f8ab803d5c0
print(hex(id(b)))  # 0x7f8ab803d5c0
print(a == b)  # True

a = lambda x: x > 0
b = a
print(hex(id(a)))  # 0x7fe6c81d1820
print(hex(id(b)))  # 0x7fe6c81d1820
print(a == b)  # True


class A: pass
B = A
print(hex(id(A)))  # 0x7fbd2a9146e0
print(hex(id(B)))  # 0x7fbd2a9146e0
print(A == B)  # True


class A: pass
B = A()
print(hex(id(A)))  # 0x7fcda0749310
print(hex(id(B)))  # 0x7fcda829afa0
print(A == B)  # False
