# |||||||||||||||||||||||||| first lesson ||||||||||||||||||||||||||
# first let's remember, what we learned at the last lesson about closures
def say():
    print("say's function worked out!")


def my_blank():
    print("my_blank's function worked out!")


def prototype_of_decorator(any_func):
    def inner():
        print('start decorator')
        any_func()
        print('finish decorator')

    return inner  # without()


d = prototype_of_decorator(say)  # function 'say' without()
# print(d)  # <function prototype_of_decorator.<locals>.inner at 0x7fa28528f5e0>

# creating decorator for say()
say = prototype_of_decorator(say)  # function 'say' without()
# say()

# creating decorator for my_blank()
my_blank = prototype_of_decorator(my_blank)  # function 'my_blank' without()


# my_blank()

# # !!!! but given examples (say() and my_blank()) can not receive arguments
# _____________________________________________________________________


# by this reason we should use everywhere as arguments *args and **kwargs
def say2(name, surname, age):
    print("say's function worked out!")


def my_blank2(a, b, c):
    print("my_blank's function worked out!")


def prototype_of_decorator2(any_func):
    def inner(*args, **kwargs):
        print('start decorator')
        any_func(*args, **kwargs)
        print('finish decorator')

    return inner  # without()


# creating decorator for say2()
say2 = prototype_of_decorator2(say2)  # function 'say2' without()
# say2('Peter', 'Ivanov', 35)

# creating decorator for my_blank2()
my_blank2 = prototype_of_decorator2(my_blank2)  # function 'my_blank2' without()


# my_blank2(31, 32, 488)
# # !!!! but given examples (say() and my_blank()) can not receive arguments


# _____________________________________________________________________
# also we can create nested decorators
def say3(name, surname, age):
    print(f"{name, surname, age} say's function worked out!")


# first decorator
def header(any_func):
    def inner(*args, **kwargs):
        print('<h1>')
        any_func(*args, **kwargs)
        print('</h1>')

    return inner  # without()


# second decorator
def table(any_func):
    def inner(*args, **kwargs):
        print('<table>')
        any_func(*args, **kwargs)
        print('</table>')

    return inner  # without()


# creating decorator for say3()
say3 = table(header(say3))  # or header(table(say3)) ||| function 'say3' without()


# say3('Peter', 'Ivanov', 35)
# _____________________________________________________________________
# Decorators are designated by symbol @


# first decorator
def my_header(any_func):
    def inner(*args, **kwargs):
        print('<h1>')
        any_func(*args, **kwargs)
        print('</h1>')

    return inner  # without()


# second decorator
def my_table(any_func):
    def inner(*args, **kwargs):
        print('<table>')
        any_func(*args, **kwargs)
        print('</table>')

    return inner  # without()


@header  # my_say = header(my_say)
def my_say():
    name = 'John'
    surname = 'Adams'
    age = 77
    print(f"{name} {surname}, {age}. say's function worked out!")


# my_say()
# print()


@table  # my_say = table(my_say)
def my_say():
    name = 'John'
    surname = 'Adams'
    age = 77
    print(f"{name} {surname}, {age}. say's function worked out!")


# my_say()
# print()


@table
@header  # my_say = table(header(my_say))
def my_say():
    name = 'John'
    surname = 'Adams'
    age = 77
    print(f"{name} {surname}, {age}. say's function worked out!")


# my_say()
# print()


@header
@table  # my_say = header(table(my_say))
def my_say():
    name = 'John'
    surname = 'Adams'
    age = 77
    print(f"{name} {surname}, {age}. say's function worked out!")


# my_say()
# print()


@header
@header
@header  # my_say = header(header(header(my_say)))
def my_say():
    name = 'John'
    surname = 'Adams'
    age = 77
    print(f"{name} {surname}, {age}. say's function worked out!")


# my_say()


# _____________________________________________________________________
# _____________________________________________________________________
# _____________________________________________________________________
# |||||||||||||||||||||||||| second lesson ||||||||||||||||||||||||||
# Now we will try to solve a problem when we lose tha name of the function which we decor to
# 1-st way: manually
# creating decorator
def my_regular_header(any_func):
    def inner(*args, **kwargs):
        print('<h1>')
        any_func(*args, **kwargs)
        print('</h1>')

    inner.__name__ = any_func.__name__  # we write this so as
    inner.__doc__ = any_func.__doc__  # not to lose the documentation of the any_func

    return inner  # without()


@my_regular_header
def my_regular_say():
    print('Hello, world')


# my_regular_say()
# print(my_regular_say.__name__)  # inner


def sqr(x):
    """
    math function
    """
    print(x ** 2)


# sqr(14)
# print(sqr.__doc__)  # here we still have documentation for sqr


@my_regular_header
def sqr2(x):
    """
    math function
    """
    print(x ** 2)


# sqr2(14)
# print(sqr2.__doc__)  # we would have lost documentation of sqr2 if we don't
# # write
# #     inner.__name__ = any_func.__name__
# #     inner.__doc__ = any_func.__doc__
# # while creating decorator my_regular_header

# _____________________________________________________________________
# 2-st way: using @wraps
from functools import wraps


# creating decorator
def my_regular_header2(any_func):
    @wraps(any_func)
    def inner(*args, **kwargs):
        print('<h1>')
        any_func(*args, **kwargs)
        print('</h1>')

    return inner  # without()


@my_regular_header2
def sqr3(x):
    """
    math function
    """
    print(x ** 2)


# sqr3(14)
# print(sqr3.__doc__)  # we don't lose documentation of sqr3
