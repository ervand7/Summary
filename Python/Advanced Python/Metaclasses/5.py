class Meta(type):
    def __init__(cls, name: str, base: tuple, attrs: dict):
        super().__init__(name, base, attrs)
        cls.MAX_COORD = 100
        cls.MIN_COORD = 0


class Point(metaclass=Meta):
    def get_coords(self) -> tuple:
        return self.MAX_COORD, self.MIN_COORD


p = Point()
print(p.get_coords())  # (100, 0)
