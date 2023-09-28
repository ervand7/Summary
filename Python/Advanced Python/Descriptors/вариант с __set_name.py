from typing import Type


class Descriptor:
    """Создаем дескриптор с __set_name__ согласно API документации."""

    def __set_name__(self, owner: Type["Point"], name: str):
        """
        Какое отличие от создания дескриптора через __init__:
        1) при присваивании нам уже ничего не нужно передавать в
        класс-дескриптор: param=Descriptor()
        дескриптор автоматически определит name
        2) он также автоматически вызывается при присваивании
        """
        print('__set_name__ called')
        self.__name = name

    def __get__(self, instance: "Point", owner: Type["Point"]):
        print('getter called')
        # instance - это экземпляр, в данном случае `p`
        # owner - это сам класс, в данном случае `Point`
        return instance.__dict__.get(self.__name)

    def __set__(self, instance: "Point", value: int):
        print('setter called')
        # instance - это экземпляр, в данном случае `p`
        instance.__dict__[self.__name] = value * value

    def __delete__(self, obj: Type['Point']):
        print('deleter called')
        # obj - это экземпляр, в данном случае `p`
        del obj.__dict__[self.__name]


class Point:
    coord_x = Descriptor()
    coord_y = Descriptor()
    coord_n = Descriptor()


p = Point()
# __set_name__ called
# __set_name__ called
# __set_name__ called

p.coord_x = 1
# setter called

print(p.coord_x)
# getter called
# 1

p.coord_y = 2
# setter called

print(p.coord_y)
# getter called
# 4

p.coord_n = 3
# setter called

print(p.coord_n)
# getter called
# 9

print(p.__dict__)  # {'coord_x': 1, 'coord_y': 4, 'coord_n': 9}

del p.coord_n
# deleter called

print(p.__dict__)  # {'coord_x': 1, 'coord_y': 4}
