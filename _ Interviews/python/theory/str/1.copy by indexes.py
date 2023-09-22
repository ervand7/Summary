# the same addr

a = "hello"
b = a[:]
print(hex(id(a)))  # 0x7feb08155630
print(hex(id(b)))  # 0x7feb08155630
