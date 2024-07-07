class Meta(type):

    # should be cls in __init__
    def __init__(cls, name: str, base: tuple, attrs: dict):
        """ Thanks to this logic we can guarantee that created class will have
            attrs MAX_COORD and MIN_COORD """
        print(hex(id(cls)))  # 0x7f9bf0026830

        super().__init__(name, base, attrs)
        cls.MAX_COORD = 100
        cls.MIN_COORD = 0


class Point(metaclass=Meta):
    def get_coords(self) -> tuple:
        return self.MAX_COORD, self.MIN_COORD


print(hex(id(Point)))  # 0x7f9bf0026830
p = Point()
print(p.get_coords())  # (100, 0)
