# The yield statement turns a regular Python function into a generator.
# Она замораживает генератор на каждой итерации. Следующий старт идет с
# того момента, где произошла заморозка
from typing import Generator


def fact(n) -> Generator:
    pr = 1
    for i in range(1, n + 1):
        pr *= i
        yield pr


print(type(fact(10)))  # <class 'generator'>

for i in fact(10):
    print(i, end=" ")  # 1 2 6 24 120 720 5040 40320 362880 3628800
