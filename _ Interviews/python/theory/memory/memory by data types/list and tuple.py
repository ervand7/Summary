a = [1]
print(a.__sizeof__())  # 48

a = [i for i in range(1_000_000)]
print(a.__sizeof__())  # 8448712

a = tuple([i for i in range(1_000_000)])
print(a.__sizeof__())  # 8000024
