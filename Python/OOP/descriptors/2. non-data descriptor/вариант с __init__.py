from typing import Type


class Descriptor:
    def __init__(self, name: str):
        self.__name = name

    def __get__(self, instance: "Point", owner: Type['Point']):
        print("getter called")
        return instance.__dict__.get(self.__name)


class Point:
    coord_x = Descriptor('descriptor for coord_x')
    coord_y = Descriptor('descriptor for coord_y')
    coord_n = Descriptor('descriptor for coord_n')


p = Point()

print(p.coord_x)
# getter called
# None

p.coord_x = 1
print(p.__dict__)  # {'coord_x': 1} <- как обычный атрибут
