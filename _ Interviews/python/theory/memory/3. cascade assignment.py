# all addresses are the same

a = b = c = 0

print(hex(id(a)))  # 0x7f78f002e910
print(hex(id(b)))  # 0x7f78f002e910
print(hex(id(c)))  # 0x7f78f002e910
