# `sorted` returns new addr

a = [1, 2, 3]
print(hex(id(a)))  # 0x7fdec017bd80

a = sorted(a)
print(hex(id(a)))  # 0x7fdec0176b40
