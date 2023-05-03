"""
Вывод: если в генераторе используется ключевое слово return, и происходит возврат
некоторых значений, то эти значения мы можем получить только перехватив исключение
StopIteration и обратившись к атрибуту value
"""


def coroutine(func):
    def inner(*args, **kwargs):
        generator_func = func(*args, **kwargs)
        generator_func.send(None)
        return generator_func

    return inner


@coroutine
def average():
    count = 0
    summa = 0
    avr = None

    while True:
        try:
            x = yield avr
        except StopIteration:
            print(StopIteration.__name__)
            break
        else:
            count += 1
            summa += x
            avr = round(summa / count, 2)
    return avr


my_generator = average()
print(my_generator.send(4))  # 4.0
print(my_generator.send(5))  # 4.5
print(my_generator.send(10))  # 6.33
try:
    my_generator.throw(StopIteration)
except StopIteration as e:
    print('Average', e.value)
