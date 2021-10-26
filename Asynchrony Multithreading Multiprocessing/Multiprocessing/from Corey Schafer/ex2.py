"""
С помощью функции join мы может мыстроить правильный поток исполнения.
Без join у нас 'hello' и finish распечатается до того как запустятся процессы.
Получается, что без join у нас выполняется весь модуль и только в самом конце
наши процессы. А join как бы присоединяет наши процессы к оощему
поток исполнения
"""
import time
import multiprocessing


def do_something():
    print('Sleeping 3 second')
    time.sleep(3)
    print('Done Sleeping')


p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)


if __name__ == '__main__':
    start = time.perf_counter()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    finish = time.perf_counter()
    print('hello')
    print(f'Finished in {round(finish - start, 2)} second(s)')
