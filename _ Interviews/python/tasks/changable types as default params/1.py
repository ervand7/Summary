def func(n: int, data=[]) -> list:
    data.append(n)
    return data


print(func(1))  # [1]
print(func(2, []))  # [2]
print(func(3, []))  # [3]
print(func(4))  # [1, 4]
