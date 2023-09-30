# while multiple inheritance you should use __init__ without params in
# auxiliary classes (second, third etc.)

from datetime import datetime
from uuid import uuid4


class Goods:
    def __init__(self, name, weight, price):
        print("init Goods")
        super().__init__()  # __init__ вызовется у MixinLog из-за __mro__
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinLog:
    def __init__(self):
        print("init MixinLog")
        self.id = uuid4()

    def save_sell_log(self):
        print(f'{self.id}: товар продан в {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')


class NoteBook(Goods, MixinLog):
    pass


n = NoteBook("Acer", 1.5, 30000)
n.save_sell_log()
# init Goods
# init MixinLog
# 54894bae-b919-417a-bd31-56687d9e76e5: товар продан в 2023-09-30 10:13:08

print(
    NoteBook.__mro__)  # (<class '__main__.NoteBook'>, <class '__main__.Goods'>, <class '__main__.MixinLog'>, <class 'object'>)
