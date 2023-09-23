a = "hello"

# str not changes
print(hex(id(a)))  # 0x7fa7a01356b0
print(hex(id(a.upper())))  # 0x7fa7a0141a30
print(hex(id(a.capitalize())))  # 0x7fa7a0143570
print(hex(id(a)))  # 0x7fa7a01356b0
