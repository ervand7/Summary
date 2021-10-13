"""
Дополнительное пояснение для generator_example8.py.
На самом деле делегирующий генератор получает то значение,
которое возвращает подгенератор с помощью ключевого слова return.

Конструкция yield from не только заменяет цикл в делегирующем генераторе,
yield from берет на себя передачу данных и исключений в подгенератор,
получает возвращаемый с помощью return результат.

yield from в других языках называется await. И смысл его в том, что вызывающий код
(делегатор) напрямую управляет работой подгенератора. И пока это происходит,
делегирующий генератор остается заблокированным. То есть он вынужден ожидать (await)
когда подгенератор закончит свою работу.
Важная деталь: подгенератор должен в себе содержать механизм завершающий его работу.
Потому что если этого не сделать, делегирующий генератор будет навечно заблокирован.
"""


def coroutine(func):
    def inner(*args, **kwargs):
        generator_func = func(*args, **kwargs)
        generator_func.send(None)
        return generator_func

    return inner


def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            print('ku-ku!!!')
            break
        else:
            print('.......', message)
    return 'Returned from subgen()'


@coroutine
def delegator(sub_generator):
    # в result попадет как раз возвращаемое через return значение функции subgen
    result = yield from sub_generator
    print(result)


sg = subgen()
g = delegator(sg)
g.send('Ok')  # ....... Ok
g.send('123')  # ....... 123
g.throw(StopIteration)  # Returned from subgen()
"""
Traceback (most recent call last):
    g.throw(StopIteration)
StopIteration
"""