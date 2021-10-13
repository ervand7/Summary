"""
Поговорим о делегирующем генераторе и о подгенераторе.
Делегирующий генератор - это тот генератор, который вызывает какой-нибудь другой.
Соответственно подгенератор - это вызываемый генератор. Такая конструкция возможна
когда нам нужно разбить один генератор на несколько.
"""


def coroutine(func):
    def inner(*args, **kwargs):
        generator_func = func(*args, **kwargs)
        generator_func.send(None)
        return generator_func

    return inner


class BlaBlaException(Exception):
    pass


@coroutine
def subgen():
    """Это будет читающий генератор. Он может читать из файла, сокета и тд."""
    while True:
        try:
            message = yield
        except:
            pass
        else:
            print('.......', message)


@coroutine
def delegator(sub_generator):
    """
    Транслятор. Будет принимать другой генератор.
    Здесь мы перехватим отсылаемые с помощью send значения и передадим их в sub_generator.
    """
    while True:
        try:
            data = yield
            sub_generator.send(data)
        except:
            pass


sg = subgen()
g = delegator(sg)
print(g.send('Ok'))  # ....... Ok
