from time import perf_counter


class Timer:
    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        print(f'Вызывается функция {self.fn.__name__}')
        start = perf_counter()
        result = self.fn(*args, **kwargs)
        finish = perf_counter()
        print(f'Функция отработала за {finish - start}')
        return result


@Timer
def fact(number):
    pr = 1
    for i in range(1, number + 1):
        pr *= i
    return pr


print(fact(4))
