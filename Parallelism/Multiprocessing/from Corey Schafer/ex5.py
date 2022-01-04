"""
Попробуем теперь не с multiprocessing, а используем concurrent.
Здесь также мы можем передавать в нашу функцию аргументы.
"""
import time
import concurrent.futures


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)')
    time.sleep(seconds)
    return f'Done Sleeping {seconds}'


if __name__ == '__main__':
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        seconds_list = [5, 4, 3, 2, 1]
        results = [executor.submit(do_something, sec) for sec in seconds_list]
        for f in concurrent.futures.as_completed(results):
            print(f.result())

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')
