a = {1: 1, 2: 2}
b = a.copy()
print(hex(id(a)))  # 0x7f915803c8c0
print(hex(id(b)))  # 0x7f915803c980
