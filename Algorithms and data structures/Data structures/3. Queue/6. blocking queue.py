# article: https://www.educative.io/courses/python-concurrency-for-senior-engineering-interviews/blocking-queue--bounded-buffer--consumer-producer

import random
import time
from threading import Condition
from threading import Thread
from threading import current_thread


class BlockingQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.curr_size = 0
        self.cond = Condition()
        self.q = []

    def enqueue(self, item):
        self.cond.acquire()
        while self.curr_size == self.max_size:
            self.cond.wait()

        self.q.append(item)
        print(f"\n======== {self.q}")
        self.curr_size += 1

        self.cond.notifyAll()
        self.cond.release()

    def dequeue(self):
        self.cond.acquire()
        while self.curr_size == 0:
            self.cond.wait()

        item = self.q.pop(0)
        self.curr_size -= 1

        self.cond.notifyAll()
        self.cond.release()

        return item


def consumer_thread(q):
    while True:
        item = q.dequeue()
        print(f"{current_thread().getName()}: {item}")
        time.sleep(random.randint(1, 3))


def producer_thread(q, val):
    item = val
    while True:
        q.enqueue(item)
        print(f"{current_thread().getName()}: {item}")
        item += 1
        time.sleep(0.1)


if __name__ == "__main__":
    blocking_q = BlockingQueue(5)

    consumerThread1 = Thread(target=consumer_thread, name="consumer1", args=(blocking_q,), daemon=True)
    consumerThread2 = Thread(target=consumer_thread, name="consumer2", args=(blocking_q,), daemon=True)
    producerThread1 = Thread(target=producer_thread, name="producer1", args=(blocking_q, 0), daemon=True)
    producerThread2 = Thread(target=producer_thread, name="producer2", args=(blocking_q, 100), daemon=True)

    consumerThread1.start()
    consumerThread2.start()
    producerThread1.start()
    producerThread2.start()

    time.sleep(15)
    print("Main thread exiting")


# ======== [0]
# producer1: 0
# consumer1: 0
#
# ======== [100]
# producer2: 100
# consumer2: 100
#
# ======== [1]
# producer1: 1
#
# ======== [1, 101]
# producer2: 101
#
# ======== [1, 101, 2]
# producer1: 2
#
# ======== [1, 101, 2, 102]
# producer2: 102
#
# ======== [1, 101, 2, 102, 3]
# producer1: 3
# consumer2: 1
# ======== [101, 2, 102, 3, 103]
#
# producer2: 103
# consumer1: 101
# ======== [2, 102, 3, 103, 4]
# producer1: 4
#
# consumer2: 2
#
# ======== [102, 3, 103, 4, 104]
# producer2: 104
# consumer1: 102
# ======== [3, 103, 4, 104, 105]
# producer2: 105
#
# consumer2: 3
#
# ======== [103, 4, 104, 105, 5]
# producer1: 5
# consumer1: 103
# ======== [4, 104, 105, 5, 106]
# producer2: 106
#
# consumer2: 4
# ======== [104, 105, 5, 106, 6]
# producer1: 6
#
# consumer1: 104
#
# ======== [105, 5, 106, 6, 7]
# producer1: 7
# consumer2: 105
#
# ======== [5, 106, 6, 7, 107]
# producer2: 107
# consumer1: 5
#
# ======== [106, 6, 7, 107, 8]
# producer1: 8
# consumer1: 106
# ======== [6, 7, 107, 8, 108]
# producer2: 108
#
# consumer2: 6
# ======== [7, 107, 8, 108, 9]
# producer1: 9
#
# consumer1: 7
# ======== [107, 8, 108, 9, 109]
# producer2: 109
#
# consumer2: 107
# ======== [8, 108, 9, 109, 10]
# producer1: 10