"""
С помощью функции map мы можем гарантировать последовательность исполнения функции
do_something в хаданном порядке.
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
        results = executor.map(do_something, seconds_list)

        for result in results:
            print(result)

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')
