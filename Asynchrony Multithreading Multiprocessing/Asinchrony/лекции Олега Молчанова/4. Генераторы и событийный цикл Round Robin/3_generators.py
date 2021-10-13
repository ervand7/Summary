from time import time
"""Смысл в получении контроля управления."""


def gen(s):
    for i in s:
        yield i


g = gen('oleg')


def gen_filename():
    while True:
        pattern = 'file-{}.jpeg'
        t = time() * 1000  # получаем кол-во милисекунд
        yield pattern.format(str(t))

        summa = 234 + 234
        print(summa)


g2 = gen_filename()


def gen_with_many_yield():
    yield 1
    print('yield 1 was')
    yield 2
    print('yield 2 was')
    yield 3
    print('yield 3 was')


g3 = gen_with_many_yield()


#  _____________________________________________________________
# Round Robin
def gen_robin1(s):
    for i in s:
        yield i


def gen_robin2(n):
    for i in range(n):
        yield i


robin1 = gen_robin1('oleg')
robin2 = gen_robin2(4)
# создадим очеред задач
tasks = [robin1, robin2]
while tasks:
    task = tasks.pop(0)
    try:
        i = next(task)
        print(i)
        # снова добавляем его в конец очереди
        tasks.append(task)
    except StopIteration:
        ...


