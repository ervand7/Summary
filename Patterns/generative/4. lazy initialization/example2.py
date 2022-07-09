class Fruit:
    def __init__(self, item: str) -> None:
        self.item = item


class Fruits:
    def __init__(self) -> None:
        self.items = {}

    def get_fruit(self, item: str) -> Fruit:
        if item not in self.items:
            self.items[item] = Fruit(item)

        return self.items[item]


if __name__ == "__main__":
    fruits = Fruits()
    print(fruits.get_fruit("Apple"))
    print(fruits.get_fruit("Lime"))
