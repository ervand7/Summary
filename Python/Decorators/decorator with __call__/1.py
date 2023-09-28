from datetime import datetime
from typing import Callable


class Timer:
    def __init__(self, func: Callable):
        self.fn = func

    def __call__(self, *args, **kwargs):
        print(f'Вызывается функция {self.fn.__name__}')
        start = datetime.now()
        result = self.fn(*args, **kwargs)
        finish = datetime.now() - start
        print(f'Функция отработала за {finish}')
        return result


@Timer
def factorial(number: int):
    pr = 1
    for i in range(1, number + 1):
        pr *= i
    return pr


print(factorial(4))
# Вызывается функция factorial
# Функция отработала за 0:00:00.000111
# 24
