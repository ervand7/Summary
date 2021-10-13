# вопрос на stackoverflow: https://stackoverflow.com/questions/10525185/python-threading-how-do-i-lock-a-thread
import threading
import time
import inspect


class Thread(threading.Thread):
    def __init__(self, t, *args):
        threading.Thread.__init__(self, target=t, args=args)
        self.start()


count = 0
lock = threading.Lock()


def increase():
    global count
    caller = inspect.getouterframes(inspect.currentframe())[1][3]
    print("Inside %s()" % caller)
    print("Acquiring lock")
    with lock:
        print("Lock Acquired\n")
        count += 1
        time.sleep(1)


def bye():
    while count <= 4:
        increase()


def hello_there():
    while count <= 4:
        increase()


def main():
    Thread(hello_there)
    Thread(bye)


if __name__ == '__main__':
    main()
