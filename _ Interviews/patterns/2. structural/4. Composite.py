# Composite — treat single objects and groups the same
# ❓ The problem:
# You want to work with:
# - one object
# - a group of objects
# in the same way, without if checks.

# Common interface
class Item:
    def price(self) -> int:
        pass


# Leaf
class Product(Item):
    def __init__(self, price: int):
        self._price = price

    def price(self) -> int:
        return self._price


# Composite
class Box(Item):
    def __init__(self):
        self.items: list[Item] = []

    def add(self, item: Item):
        self.items.append(item)

    def price(self) -> int:
        return sum(item.price() for item in self.items)


# Client
def client_code(item: Item):
    print(item.price())


# Usage
product1 = Product(10)
product2 = Product(20)

box = Box()
box.add(product1)
box.add(product2)

client_code(product1)  # 10
client_code(box)       # 30
