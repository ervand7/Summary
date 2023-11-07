a = (1, 2, 3)
b = a[:]
# the same addr
print(hex(id(a)))  # 0x7f8c301d1d00
print(hex(id(b)))  # 0x7f8c301d1d00

