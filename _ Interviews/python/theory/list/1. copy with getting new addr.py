# Here are ways how to get copy from another list with another addr

a1 = [1, 2, 3]
b1 = a1.copy()
print(hex(id(a1)))  # 0x7fe3a8083b00
print(hex(id(b1)))  # 0x7fe3a807e900

a2 = [1, 2, 3]
b2 = a2[:]
print(hex(id(a2)))  # 0x7fe8d817b640
print(hex(id(b2)))  # 0x7fe8d817b4c0

a3 = [1, 2, 3]
b3 = list(a3)
print(hex(id(a3)))  # 0x7f8cc0084440
print(hex(id(b3)))  # 0x7f8cc0083a40

a4 = [1, 2, 3]
b4 = [*a4]
print(hex(id(a4)))  # 0x7feb5817ba40
print(hex(id(b4)))  # 0x7feb5817b940


