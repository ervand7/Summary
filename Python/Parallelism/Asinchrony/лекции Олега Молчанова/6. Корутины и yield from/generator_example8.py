"""
Использование конструкции yield from.
Избавляемся от большой писанины.
"""


def coroutine(func):
    def inner(*args, **kwargs):
        generator_func = func(*args, **kwargs)
        generator_func.send(None)
        return generator_func

    return inner


# поскольку в делегаторе мы используем конструкцию yield from
# то нам уже на подгенератре не нужен декоратор coroutine так как
# <yield from> содержит в себе инициализацию подгенератора
def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            print('ku-ku!!!')
        else:
            print('.......', message)


@coroutine
def delegator(sub_generator):
    # всю эту писанину можно заменить одной строкой
    # while True:
    #     try:
    #         data = yield
    #         sub_generator.send(data)
    #     except BlaBlaException as e:
    #         sub_generator.throw(e)
    yield from sub_generator


sg = subgen()
g = delegator(sg)
g.send('Ok')  # ....... Ok
g.send('123')  # ....... 123
g.throw(StopIteration)
