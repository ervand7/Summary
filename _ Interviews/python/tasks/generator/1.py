from typing import Iterable


def fib(n: int) -> Iterable:
    if n in {0, 1}:
        yield n

    else:
        a, b = 0, 1
        for _ in range(n - 1):
            yield b
            a, b = b, a + b


gen = fib(7)
for i in gen:
    print(i)
