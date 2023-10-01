class Meta(type):
    def __new__(mcs, name: str, base: tuple, attrs: dict) -> type:
        """ Thanks to this logic we can guarantee that created class will have
            attrs MAX_COORD and MIN_COORD """

        print(hex(id(Meta)))  # 0x7fc0d7f1b5f0
        print(hex(id(mcs)))  # 0x7fc0d7f1b5f0

        attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
        return type.__new__(mcs, name, base, attrs)


class Point(metaclass=Meta):
    def get_coords(self) -> tuple:
        return self.MAX_COORD, self.MIN_COORD


p = Point()
print(p.get_coords())  # (100, 0)
