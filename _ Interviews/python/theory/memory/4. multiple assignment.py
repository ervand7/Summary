# all addresses are the same

a, b = 0, 0

print(hex(id(a)))  # 0x7fb48002e910
print(hex(id(b)))  # 0x7fb48002e910

# but here are diff
a, b = 0, 1
print(hex(id(a)))  # 0x7fb48002e910
print(hex(id(b)))  # 0x7fb48002e930
