# pip install accessify
from accessify import private


class Car:

    @private
    def start_engine(self):
        return 'Engine sound.'

    def run(self):
        return self.start_engine()

    # прописываем, чтобы потом нечестным путем получить к этому доступ
    # и сравнить неэффективность встроенной инкапсуляции с @private
    def __private_method(self):
        print('private_method')


car = Car()
car.run()
print(dir(Car))
car._Car__private_method()  # получение нечестным путем инкапсулированного метода

assert 'Engine sound.' == car.run()  # а так мы не можем ничего получить
car.start_engine()  # InaccessibleDueToItsProtectionLevelException

# ________________________________________________________________________________
"""
Child classes cannot access parent private members.
In this example, the Car class contains a private member named start_engine. 
As a private member, they cannot be accessed from the child classes, Tesla in our case. 
So overridden method run by Tesla class cannot use the parent's start_engine member.
"""


class Car:

    @private
    def start_engine(self):
        return 'Engine sound.'


class Tesla(Car):

    def run(self):
        return self.start_engine()


tesla = Tesla()
tesla.run()
