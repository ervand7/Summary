# оба объекта изменятся


a = [1, 2, 3]
b = a
print(hex(id(a)))  # 0x7ff4b817b940
print(hex(id(b)))  # 0x7ff4b817b940

b.append(4)
print(b)  # [1, 2, 3, 4]
print(a)  # [1, 2, 3, 4]
