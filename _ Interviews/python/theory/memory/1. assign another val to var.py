a = 1
print(a)
print(hex(id(a)))  # 0x7ff39002e930

a = 2
print(a)
print(hex(id(a)))  # 0x7fa1f802e950

a = "hello"
print(a)
print(hex(id(a)))  # 0x7ff380059930

a = [1, 2, 3]
print(a)
print(hex(id(a)))  # 0x7ff38017b8c0
