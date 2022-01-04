"""
Обработка исключений.
Задача заключается в том, чтобы передать объект исключения в подгенератор.
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
        except BlaBlaException:
            print('ku-ku!!!')
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
        except BlaBlaException as e:
            sub_generator.throw(e)


sg = subgen()
g = delegator(sg)
g.send('Ok')  # ....... Ok
g.throw(BlaBlaException)  # ku-ku!!!
