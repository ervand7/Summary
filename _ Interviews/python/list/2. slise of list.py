# we receive new object when we take slice of list

a = [1, 2, 3]
b = a[1:]
print(hex(id(a)))  # 0x7fd1a8083b80
print(hex(id(b)))  # 0x7fd1a807e940
