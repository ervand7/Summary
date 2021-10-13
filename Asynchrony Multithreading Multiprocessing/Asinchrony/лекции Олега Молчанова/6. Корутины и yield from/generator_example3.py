class BlaBlaException(Exception):
    pass


def average():
    """Создаем корутину, передаем в нее значения, она нам отдает их среднее арифметическое."""
    count = 0
    summa = 0
    avr = None

    while True:
        try:
            x = yield avr
        # этот блок мы сюда вписали чтобы показать что внутри генератора мы можем работать с исключениями
        except BlaBlaException:
            print(BlaBlaException.__name__)
        else:
            count += 1
            summa += x
            avr = round(summa / count, 2)


g = average()
g.send(None)
print(g.send(4))  # 4.0
print(g.send(5))  # 4.5
print(g.send(10))  # 6.33
print(g.throw(BlaBlaException))  # Done 6.33
