class House:
    def __init__(self, floors, garage, pool):
        self.floors = floors
        self.garage = garage
        self.pool = pool


class HouseBuilder:
    def __init__(self):
        self.floors = 1
        self.garage = False
        self.pool = False

    def add_garage(self):
        self.garage = True
        return self

    def add_pool(self):
        self.pool = True
        return self

    def build(self) -> House:
        return House(self.floors, self.garage, self.pool)


# Client
house = (
    HouseBuilder()
    .add_garage()
    .add_pool()
    .build()
)
