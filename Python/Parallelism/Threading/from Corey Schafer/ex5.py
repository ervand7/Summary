import time
import concurrent.futures

t1 = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second()...')
    time.sleep(seconds)
    return f'Done sleeping...{seconds}'


with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]
    results = executor.map(do_something, seconds)

    for result in results:
        print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish - t1, 2)} second(s)')
