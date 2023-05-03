from typing import Callable, Type

MAX_RETRIES = 3


def checker(tries: int, exc: Type[Exception]):
    def decorator(func: Callable):

        def inner(*args, **kwargs):
            counter = 0
            for i in range(tries):
                try:
                    counter += 1
                    return func(*args, **kwargs)
                except exc:
                    print(exc.__name__)
            if counter == MAX_RETRIES:
                print('stop trying')

        return inner

    return decorator


@checker(5, ZeroDivisionError)
def multiplier(a, b):
    return a / b


multiplier(1, 0)
# division by zero
# division by zero
# division by zero
# division by zero
# division by zero
