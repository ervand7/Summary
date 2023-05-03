from pprint import pprint

"""
Инкапсуляция - это сокрытие.
Public, protected and private attr and methods.
"""


class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_private_attrs(self):
        print(self.__name, self.__balance, self.__passport)

    def print_public_data(self):
        self.__print_private_data()

    def __print_private_data(self):
        print(self.__name, self.__balance, self.__passport)


account1 = BankAccount('Bob', 10000, 4545454545)

# Получаем доступ к приватным атрибутам и методам вне класса (через публичный метод)
account1.print_public_data()  # Bob 10000 4545454545
account1.print_private_attrs()  # Bob 10000 4545454545

# Доступ к приватным атрибутам и методам вне класса запрещен
account1.__print_private_data()  # ERROR
print(account1.__name)  # ERROR
print(account1.__balance)  # ERROR
print(account1.__passport)  # ERROR

# Проверив с помощью dir возможные доступные методы, мы видим способы доступа к приватным данным
pprint(dir(account1))
"""
['_BankAccount__balance',
 '_BankAccount__name',
 '_BankAccount__passport',
 '_BankAccount__print_private_data',
 ...
 ...
"""

account1._BankAccount__print_private_data()  # Bob 10000 4545454545
print(account1._BankAccount__balance)  # 10000
