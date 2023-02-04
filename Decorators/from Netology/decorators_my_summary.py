from pprint import pprint


def foo():
    print(f'function {foo.__name__} is called')


# pprint(foo.__dir__())  # we look there method __call__ thanks which our function is callable.
#  Exactly __call__ distinguishes functions from other methods
# _________________________________________________________________________

# You also can add functions in list and iter with them
x = foo
n = foo
y = foo
lst = [x, n, y, foo]

# for i in lst:
#     i.__call__()  # the same that i()
# _________________________________________________________________________

# You can put one function into other
from typing import Callable


def foo2(function: Callable):
    print(f'function {foo2.__name__} is called')
    function()


# foo2(foo)
# _________________________________________________________________________

# Let's try create function via class
class MyFunction:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print('The exemplar of class MyFunction is called')


my_exemplar = MyFunction()


# my_exemplar.__call__()  # the same that my_exemplar()
# _________________________________________________________________________

def multiplier(a, b):
    return a * b


def print_fabric(old_function: Callable):
    def new_function(a, b):
        print(f'Вызвана функция {old_function.__name__}')
        print(f'С аргументами {a, b}')
        result = old_function(a, b)
        print(f'Получили результат {result}')
        return result

    return new_function


multiplier = print_fabric(multiplier)  # Now there is a new functional in multiplier


# multiplier.__call__(2, 3)
# _________________________________________________________________________
@print_fabric
def multiplier2(a, b):
    return a * b


# multiplier.__call__(2, 3)

# _________________________________________________________________________
def print_decor(old_function: Callable): ...


def my_foo(*args, **kwargs):
    print(args)
    print(kwargs)


# my_foo(1, 2, 3, a=4, b=5)  # unnamed args will go to tuple (1, 2, 3), named arguments will go dict {'a': 4, 'b': 5}


# _________________________________________________________________________
# let's try unpack tuple & dict on other example
def foo_(a, b, c, d, e):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)


tuple_ = 1, 2, 3
dict_ = {
    'd': 4,
    'e': 5
}


# foo_(*tuple_, **dict_)


# _________________________________________________________________________


def _fabric(old_function):
    def new_function(*args, **kwargs):
        print(f'Вызвана функция {old_function.__name__}')
        print(f'С аргументами {args, kwargs}')
        result = old_function(*args, **kwargs)
        print(f'Получили результат {result}')
        return result

    return new_function


@_fabric
def multiplier3(a, b):
    return a * b


# multiplier3.__call__(1, 2)
# _________________________________________________________________________

# let's engage our decorator in <try> constructions
TRIES = 10


def attempted_decorator(any_function: Callable):
    def new_function(*args, **kwargs):
        my_error = None  # we had to use combination <my_error = None> to avoid this error:
        # variable <my_exception> mae be referenced before assignment
        for i in range(TRIES):
            try:
                return any_function(*args, **kwargs)
            except Exception as my_exception:
                my_error = my_exception
                print(f'The number of trying №{i + 1}')
                print(my_error)
        raise my_error

    return new_function


@attempted_decorator
def multiplier4(a, b):
    return a / b


# x = multiplier4(2, 0)
# print(x)
# _________________________________________________________________________
# let's try append my_error into list payload_errors
TRIES2 = 5


def send_errors(errors):
    print(errors)


def attempted_decorator2(any_function2: Callable):
    payload_errors = []
    max_errors = 3

    def new_function2(*args, **kwargs):
        nonlocal payload_errors
        my_error = None  # we had to use combination <my_error = None> to avoid this error:
        # variable <my_exception> mae be referenced before assignment
        for i in range(TRIES2):
            try:
                return any_function2(*args, **kwargs)
            except Exception as my_exception:
                my_error = my_exception
                print(f'The number of trying №{i + 1}')
                print(my_error)
        payload_errors.append(my_error)
        if len(payload_errors) == max_errors:
            send_errors(payload_errors)
            payload_errors = []  # zero out

    return new_function2


@attempted_decorator2
def multiplier5(a, b):
    return a / b


# x = multiplier5(2, 0)
# x1 = multiplier5(2, 0)
# x2 = multiplier5(2, 0)
# print(x, x1, x2)


# _________________________________________________________________________
# now let's write a decorator which receive arguments
def print_errors_(errors):
    print(errors)


def superstructure_over_decorator(n_tries, errors):
    def decorator(old_function: Callable):
        list_errors = []
        max_errors = 3

        def new_function(*args, **kwargs):
            nonlocal list_errors
            error = None
            for i in range(n_tries):
                try:
                    return old_function(*args, **kwargs)
                except errors as my_error:
                    print(my_error)
            list_errors.append(error)
            if len(list_errors) == max_errors:
                print_errors_(list_errors)
                list_errors = []

        return new_function

    return decorator


@superstructure_over_decorator(5, ZeroDivisionError)
def multiplier_(a, b):
    return a / b


# x = multiplier_(1, 8)
# y = multiplier_(1, 0)
# print(y)
# print(x)
# _________________________________________________________________________
# 2 decorators from teacher

import datetime
import logging
from logging.handlers import RotatingFileHandler
from typing import Callable, Any


def make_trace(path: str) -> Callable:
    """Вариант с записью в файл"""

    def trace(old_function: Callable) -> Callable:
        def new_function(*args, **kwargs) -> Any:
            result = old_function(*args, **kwargs)

            with open(path, 'a') as log:
                log.write(f'\n{datetime.datetime.utcnow()}: called {old_function.__name__}\n'
                          f'\t args: {args}\n'
                          f'\t kwargs: {kwargs}\n'
                          f'\t result: {result}\n')

            return result

        return new_function

    return trace


def make_log(path: str) -> Callable:
    """Вариант с использованием logging"""

    def log(old_function: Callable) -> Callable:
        logger = logging.getLogger(path)
        logger.setLevel(logging.INFO)
        handler = RotatingFileHandler(path, backupCount=10, maxBytes=1000000)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        def new_function(*args, **kwargs) -> Any:
            result = old_function(*args, **kwargs)

            logger.info(f'called: {old_function.__name__}\n'
                        f'\t args: {args}\n'
                        f'\t kwargs: {kwargs}\n'
                        f'\t result: {result}\n')
            return result

        return new_function

    return log


# _________________________________________________________________________
# size decorators from teacher
from pympler import asizeof


def size_decor(old_function):
    calls = 0
    total_size = 0

    def new_function(*args, **kwargs):
        nonlocal calls, total_size
        calls += 1

        result = old_function(*args, **kwargs)
        size_result = asizeof.asizeof(result)
        total_size += size_result
        medium_size = total_size / calls

        print(f'Вызов:{old_function.__name__}\n'
              f'Размер: {size_result}\n'
              f'В среднем: {medium_size}\n')

    return new_function


def parametrized_size_decor(min_size):
    calls = 0
    total_size = 0

    def my_size_decor(old_function):
        def new_function(*args, **kwargs):
            nonlocal calls, total_size
            calls += 1

            result = old_function(*args, **kwargs)
            size_result = asizeof.asizeof(result)
            total_size += size_result
            medium_size = total_size / calls

            if size_result >= min_size:
                print(f'Вызов:{old_function.__name__}\n'
                      f'Размер: {size_result}\n'
                      f'В среднем: {round(medium_size, 2)}\n')
            else:
                raise ValueError('ERROR: size_result <= min_size')

            return result

        return new_function

    return my_size_decor


@size_decor
def foo(number):
    return [i for i in range(number)]


@parametrized_size_decor(999)
def foo2(n):
    return [i for i in range(n)]


# if __name__ == '__main__':
#     foo2(73333)
#     foo2(433)
#     foo2(544)
#     foo(123)
#     foo(321)
#     foo(432)
# _________________________________________________________________________
# one more example from teacher

import time
from collections import OrderedDict


def wrap_decorator(param):
    my_cache = OrderedDict()

    def my_decorator(old_function):

        def inner(*args, **kwargs):
            print(len(my_cache) * 10)
            key = (print(f"{old_function.__name__}\n"), str(args), str(kwargs))
            result = my_cache.get(key)
            if result is not None:
                return result
            else:
                result = old_function(*args, **kwargs)
                my_cache[key] = result
                if len(my_cache) > param:
                    my_cache.popitem(last=False)
                return result

        return inner

    return my_decorator


@wrap_decorator(7)
def concatenate(str_1, str_2):
    time.sleep(0.5)
    return f'{str_1}{str_2}'


# print(concatenate('abc', 'erd'))
# print(concatenate('abc', 'asd'))
# print(concatenate('abc', 'zxc'))
# print(concatenate('abc', 'xcv'))
# print(concatenate('abc', 'vbn'))
# print(concatenate('abc', 'ghj'))
