# 3.10
a = (1, 2, 3, 4)
b = [1, 2, 3]
print(list(zip(a, b, strict=True)))  # ValueError: zip() argument 2 is shorter than argument 1
