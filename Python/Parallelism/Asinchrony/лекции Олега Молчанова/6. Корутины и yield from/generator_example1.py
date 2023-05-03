from inspect import getgeneratorstate


def subgen():
    message = yield
    print('Subgen received:', message)


g = subgen()

# получаем ошибку, так как у только что созданного генератора не может
# быть передано в качестве аргумента ничего кроме None
# print(g.send('some argument'))

print(getgeneratorstate(g))  # 'GEN_CREATED'
# следующее действие по первоначальной инициации генератора корутины является обязательным!
g.send(None)  # вместо этого можно было использовать next(g). Результат одинаковый
# Тут мы неявно возвращаем None

# получаем состояние GEN_SUSPENDED так как после того как мы передали в методе send
# тип None, управление сдвинулось до < = yield> и процесс заморозился
print(getgeneratorstate(g))  # 'GEN_SUSPENDED'

print(g.send('ok'))  # Subgen received: ok
"""
Traceback (most recent call last):
    print(g.send('ok'))
StopIteration
"""

