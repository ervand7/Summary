from time import sleep
"""
С помощью обычных функций мы бы никогда не добились такого поведения.
Генераторы нам возвращают контроль выполнения, поэтому асинхронность и получается.
"""

queue = []


def counter():
    count = 0
    while True:
        print(count)
        count += 1
        yield


def printer():
    count = 0
    while True:
        if count % 3 == 0:
            print('Bang!')
        count += 1
        yield


def main():
    """Событийный цикл"""
    while True:
        generator = queue.pop(0)
        next(generator)
        queue.append(generator)
        sleep(0.5)


if __name__ == '__main__':
    gen1 = counter()
    queue.append(gen1)
    gen2 = printer()
    queue.append(gen2)
    main()
