from inspect import getgeneratorstate


def coroutine(func):
    """
    Создаем этот декоратор чтобы каждый раз не посылать None при
    первом вызове генератора.
    """
    def inner(*args, **kwargs):
        generator_func = func(*args, **kwargs)
        generator_func.send(None)
        return generator_func

    return inner


class BlaBlaException(Exception):
    pass


@coroutine
def average():
    count = 0
    summa = 0
    avr = None

    while True:
        try:
            x = yield avr
        except BlaBlaException:
            print(BlaBlaException.__name__)
        else:
            count += 1
            summa += x
            avr = round(summa / count, 2)


my_generator = average()
# видим, что он у нас сразу GEN_SUSPENDED
print(getgeneratorstate(my_generator))  # GEN_SUSPENDED
print(my_generator.send(4))  # 4.0
print(my_generator.send(5))  # 4.5
print(my_generator.send(10))  # 6.33
print(my_generator.throw(BlaBlaException))  # Done 6.33
