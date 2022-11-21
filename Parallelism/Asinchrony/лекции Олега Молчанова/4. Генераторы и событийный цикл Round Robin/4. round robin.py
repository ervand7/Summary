# Round Robin
def gen_robin1(s):
    yield from s


def gen_robin2(n):
    yield from range(n)


robin1 = gen_robin1('oleg')
robin2 = gen_robin2(4)

# создадим очередь задач
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

# o
# 0
# l
# 1
# e
# 2
# g
# 3
