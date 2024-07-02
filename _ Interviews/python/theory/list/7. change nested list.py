# оба объекта изменятся

a = [1, [1, 2, 3, 4]]
b = a
a[1].append(777)
print(b)  # [1, [1, 2, 3, 4]]

print(hex(id(a)))  # 0x7f91e003b100
print(hex(id(b)))  # 0x7f91e003b100
