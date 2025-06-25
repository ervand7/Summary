from typing import Callable

TRIES = 10


def decorator(func: Callable):
    def inner(*args, **kwargs):
        error = None
        for i in range(TRIES):
            try:
                return func(*args, **kwargs)
            except Exception as my_exception:
                error = my_exception
                print(f'The number of trying №{i + 1}')

        print(error)

    return inner


@decorator
def multiplier(a, b):
    return a / b


multiplier(1, 0)
# The number of trying №1
# The number of trying №2
# The number of trying №3
# The number of trying №4
# The number of trying №5
# The number of trying №6
# The number of trying №7
# The number of trying №8
# The number of trying №9
# The number of trying №10
# division by zero
