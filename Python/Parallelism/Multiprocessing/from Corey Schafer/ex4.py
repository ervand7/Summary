"""
Попробуем запустить 10 процессов с передачей аргументов в функцию do_something
"""
import time
import multiprocessing


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)')
    time.sleep(seconds)
    print('Done Sleeping')


processes = []

if __name__ == '__main__':
    start = time.perf_counter()
    for _ in range(10):
        p = multiprocessing.Process(target=do_something, args=[1.5])
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 2)} second(s)')
