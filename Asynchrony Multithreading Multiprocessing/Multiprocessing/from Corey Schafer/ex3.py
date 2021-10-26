"""
Попробуем запустить 10 процессов с использованием цикла.
"""
import time
import multiprocessing


def do_something():
    print('Sleeping 3 second')
    time.sleep(3)
    print('Done Sleeping')


processes = []


if __name__ == '__main__':
    start = time.perf_counter()
    for _ in range(10):
        p = multiprocessing.Process(target=do_something)
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 2)} second(s)')
