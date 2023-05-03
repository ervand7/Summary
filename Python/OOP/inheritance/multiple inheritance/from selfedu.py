class Goods:
    def __init__(self, name, weight, price):
        super().__init__()  # __init__ вызовется у MixinLog из-за __mro__
        print("init MixinLog")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinLog:
    ID = 0

    def __init__(self):
        print("init MixinLog")
        self.ID += 1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f"{self.id}: товар продан в 00:00 часов")


class NoteBook(Goods, MixinLog):
    pass


n = NoteBook("Acer", 1.5, 30000)
n.save_sell_log()
