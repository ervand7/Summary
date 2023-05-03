from accessify import protected
"""
Отличие декоратора @private от @protected в том, что методы под декоратором 
@private не могут быть унаследованны дочерними классами, в то время 
как методы под декоратором @protected могут быть унаследованны дочерними классами.
Но все равно, что, ни к первому, ни ко второму не будет доступа вне класса.
"""


class Car:

    @protected
    def start_engine(self):
        return 'Engine sound.'


class Tesla(Car):

    def run(self):
        return self.start_engine()


if __name__ == '__main__':
    tesla = Tesla()

    assert 'Engine sound.' == tesla.run()
    print(tesla.start_engine())  # наследоваться может, но доступа вне класса все равно нет
