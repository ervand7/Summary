from datetime import datetime
from time import sleep


def timer():
    start = datetime.now()

    def inner():
        return datetime.now() - start

    return inner


tmr = timer()
print(tmr())
print(tmr())

sleep(2)
print(tmr())
