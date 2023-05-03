def header(func):
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')

    inner.__name__ = func.__name__  # we write this so as
    inner.__doc__ = func.__doc__  # not to lose the documentation of the func

    return inner


def sqr(x):
    """math function"""
    print(x ** 2)


print(sqr.__doc__)  # math function


@header
def sqr2(x):
    """math function"""
    print(x ** 2)


print(sqr2.__doc__)  # math function
sqr2(2)
# <h1>
# 4
# </h1>
