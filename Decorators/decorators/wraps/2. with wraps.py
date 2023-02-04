from functools import wraps


# creating decorator
def header(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')

    return inner


@header
def sqr(x):
    """math function"""
    print(x ** 2)


print(sqr.__doc__)  # math function
sqr(2)
# <h1>
# 4
# </h1>
