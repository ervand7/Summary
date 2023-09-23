from typing import Generator

data = [1, 2, 3]


def my_func(d: list) -> Generator:
    yield from d


print(type(my_func(data)))  # <class 'generator'>

for i in my_func(data):
    print(i, end=" ")  # 1 2 3
