def create_class(name: str, base: tuple, attrs: dict) -> type:
    attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
    return type(name, base, attrs)


class Point(metaclass=create_class):
    def get_coords(self) -> tuple:
        return self.MAX_COORD, self.MIN_COORD


p = Point()
print(p.get_coords())  # (100, 0)
