class MyPoint:
    def __init__(self, x=0, y=0):
        """В ООП это называется конструктором класса."""
        self.x = x
        self.y = y
        print(f'Инициализация {self.__str__()}')

    def __del__(self):
        """
        В ООП это называется деструктором класса.
        Этот метод срабатывает также автоматически, как и __init__.
        """
        print('Удаление экземпляра: ' + self.__str__())


pt = MyPoint()
# Инициализация <__main__.MyPoint object at 0x7fa902236430>
# Удаление экземпляра: <__main__.MyPoint object at 0x7fa902236430>
