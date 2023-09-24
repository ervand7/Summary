from time import time
from typing import Callable


def measure(func: Callable):
    def inner(*args, **kwargs):
        start = time()
        # if args == (), *args means absense of any data
        # if kwargs == {}, **kwargs means absense of any data
        result = func(*args, **kwargs)
        print(time() - start)
        return result

    return inner


@measure
def say_hello_with_args(*args, **kwargs):
    print(*args, **kwargs)


say_hello_with_args(1, 2, 3, {"hello": "world"})


# 1 2 3 {'hello': 'world'}
# 2.5033950805664062e-05


@measure
def say_hello_without_args():
    print("without args and kwargs")


say_hello_without_args()
# without args and kwargs
# 3.0994415283203125e-06
