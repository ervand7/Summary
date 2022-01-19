class A(list):
    pass


# 3.9
print(isinstance(1, (int, str)))  # True
print(issubclass(A, (int, list)))  # True

# 3.10
print(isinstance(1, int | str))  # True
print(issubclass(A, int | list))  # True
