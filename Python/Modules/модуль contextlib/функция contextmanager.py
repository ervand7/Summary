from contextlib import contextmanager


class FinishException(Exception):
    pass


@contextmanager
def log_progress(message, result):
    try:
        print(f'{message} => {result}')
        yield  # log_progress must be generator
    except FinishException:
        print(f'{message} => finished')


def say_hello(names: list):
    """simple recursive func"""
    if len(names) == 0:
        return
    name = names[0]
    with log_progress(say_hello.__name__, name):
        print('Hello ' + name)
        say_hello(names[1:])


say_hello(['Vasya', 'Ivan', 'Jack'])
"""
say_hello => Vasya
Hello Vasya
say_hello => Ivan
Hello Ivan
say_hello => Jack
Hello Jack
"""