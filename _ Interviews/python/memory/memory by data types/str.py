a = "q"
b = a * 1_000_000
print(a.__sizeof__())  # 50
print(b.__sizeof__())  # 1000049
