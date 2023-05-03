"""Так обе функции отрабатывают одновременно."""
import time
import multiprocessing

start = time.perf_counter()


def do_something():
    print('Sleeping 3 second')
    time.sleep(3)
    print('Done Sleeping')


p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

finish = time.perf_counter()

if __name__ == '__main__':
    p1.start()
    p2.start()
    print(f'Finished in {round(finish - start, 2)} second(s)')
