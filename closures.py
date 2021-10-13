# main article https://devpractice.ru/closures-in-python/
# ||||||||||||||||||||| lesson 1 ||||||||||||||||||||||||

def main_func(value):
    def inner_func():
        print('hello, my friend', value)

    return inner_func  # the call shouldn't be


# b = main_func('Ivan')
# b()


# __________________________________________

def adder(value):
    def inner(n):
        return value + n

    return inner  # the call shouldn't be


# a = adder(100)  # 100 goes to adder(value)
# print(a(2))  # 2 goes to inner(n)
# print(a(1))  # 1 goes to inner(n)
# print(a(10))  # 10 goes to inner(n)

# __________________________________________

def counter():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner  # the call shouldn't be


# q = counter()
# print(q())
# print(q())
# print(q())
# print(q())


# __________________________________________

def mul(e):
    def helper(b):
        return e * b

    return helper  # the call shouldn't be


# print(mul(9))  # <function mul.<locals>.helper at 0x7fb2a0a944c0>

# print(mul(5)(2))  # where 5 goes to mul(e), 2 goes to helper(b)
#
# new_mul5 = mul(5)
# print(new_mul5(2))
# __________________________________________


def fun1(w):
    x = w * 3

    def fun2(b):
        nonlocal x
        return b + x

    return fun2  # the call shouldn't be


# test_fun = fun1(4)  # 4 goes to fun1(w)
# print(test_fun(7))  # 7 goes to fun2(b)

# __________________________________________
# __________________________________________
# __________________________________________
# ||||||||||||||||||||| lesson 2 ||||||||||||||||||||||||

def average_numbers():
    my_list = []

    def inner_numbers(value):
        my_list.append(value)
        print(my_list)
        return sum(my_list) / len(my_list)

    return inner_numbers  # the call shouldn't be


# r1 = average_numbers()
# print(r1(5))  # 5 first goes to inner_numbers(value), then to my_list
# # TAKE ATTENTION! HERE IF EVEN WE SHARE INT WITH INT, WE GET IN RESULT FLOAT TYPE
#
# print(r1(10))  # 10 first goes to inner_numbers(value), then to my_list
# print(r1(14))  # 14 first goes to inner_numbers(value), then to my_list
# __________________________________________

def my_average_numbers():
    summa = 0
    count = 0

    def inner(value):
        nonlocal summa  # declaration of non-local variable
        nonlocal count  # declaration of non-local variable
        summa += value
        count += 1  # common count of variables

        return summa / count

    return inner  # the call shouldn't be


# k = my_average_numbers()
# print(k(10))  # 10 goes to inner(value), remembered in nonlocal summa and nonlocal count
# print(k(20))  # 20 goes to inner(value), remembered in nonlocal summa and nonlocal count
# print(k(30))  # 30 goes to inner(value), remembered in nonlocal summa and nonlocal count
# __________________________________________
from datetime import datetime


def timer():
    start = datetime.now()

    def inner():
        return datetime.now() - start

    return inner  # the call shouldn't be


# # ATTENTION! THIS EXAMPLE MUST BE USED ONLY IN CONSOLE!!!!!!!!!!!!!
# r = timer()
# # then separately call r()
# __________________________________________

from time import perf_counter


def my_timer():
    start = perf_counter()

    def inner():
        return perf_counter() - start

    return inner  # the call shouldn't be


# ATTENTION! THIS EXAMPLE MUST BE USED ONLY IN CONSOLE!!!!!!!!!!!!!
# r = my_timer()
# # then separately call r()
# __________________________________________
# Now let's consider an example, where a function will be as argument
def add(a, b):
    return a + b


def multiplication(a, b, c):
    return a + b + c


def my_counter(above_written_func):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1  # keep in itself the count of calling function my_counter(above_written_func)
        print(f'function "{above_written_func.__name__}" was called {count} times')
        # magic method __name__ WITHOUT () shows us the name of any function. For
        # example: >>> print(abs.__name__) # 'abs'
        return above_written_func(*args, **kwargs)  # return add(a, b) or return multiplication(a, b, c)

    return inner  # the call shouldn't be


# q = my_counter(add)  # take attention, here we write function add() as argument and without ()
# print(q(10, 20))  # (10, 20) first go in inner(*args, **kwargs), then go in add(a, b)
# print(q(11, 22))  # (11, 22) first go in inner(*args, **kwargs), then go in add(a, b)

# q2 = my_counter(multiplication)
# print(q2(2, 4, 6))
# print(q2(22, 44, 66))
