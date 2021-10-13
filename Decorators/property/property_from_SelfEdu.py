class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @staticmethod
    def __check_value(input_data):
        if isinstance(input_data, (int, float)):
            return True
        return False

    # def __get_coord_x(self):
    #     print('Вызов __get_coord_x')
    #     return self.__x
    # это мы заменили на
    @property
    def coord_x(self):
        print('Вызов __get_coord_x')
        return self.__x

    # def __set_coord_x(self, x):
    #     if Point.__check_value(x):
    #         print('Вызов __set_coord_x')
    #         self.__x = x
    #     else:
    #         raise ValueError('Неверный формат данных')
    # это мы заменили на
    @coord_x.setter
    def coord_x(self, x):
        if Point.__check_value(x):
            print('Вызов __set_coord_x')
            self.__x = x
        else:
            raise ValueError('Неверный формат данных')

    # def __del_coord_x(self):
    #     print('Удаление свойства')
    #     del self.__x
    # это мы заменили на
    @coord_x.deleter
    def coord_x(self):
        print('Удаление свойства')
        del self.__x

    # coord_x = property(__get_coord_x, __set_coord_x, __del_coord_x)


a = Point(1, 2)
a.coord_x = 100  # запись значения
new = a.coord_x  # чтение значения
print(new)
del a.coord_x

