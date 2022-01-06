# _____________________________________________________________________
# @property
# let's before start we remember the lesson about property in OOP
class BankAccount2:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print('get balance method')
        return self.__balance

    def set_balance(self, value):
        print('set balance method')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    def delete_balance(self):
        print('delete balance method')
        del self.__balance

    balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)


# now we can use decorator property
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property  # it is the default value of getter
    def my_balance(self):  # The name of all three functions must be the same!!!
        print(f'get balance, {self.__balance}')
        return self.__balance

    @my_balance.setter
    def my_balance(self, value):  # The name of all three functions must be the same!!!
        print(f'set balance, {value}')
        if not isinstance(value, (int, float)):
            raise ValueError('The balance must de a number')
        self.__balance = value

    @my_balance.deleter
    def my_balance(self):  # The name of all three functions must be the same!!!
        print('delete balance')
        del self.__balance


m = BankAccount('Bob', 133)


# m.my_balance
# m.my_balance = 144
# del m.my_balance
# # m.my_balance  # 'BankAccount' object has no attribute '_BankAccount__balance'
# m.my_balance = 12

# _____________________________________________________________________
# calculated properties
class Square:
    def __init__(self, s):
        self.__side = s
        self.__area = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None
        print('side.setter decorator is called')

    @property
    def area(self):
        if self.__area is None:
            print('calculate area')
            self.__area = self.__side ** 2
        return print(self.__area)


# xx = Square(7)
# xx.area
# xx.side = 3
# xx.area

# _____________________________________________________________________
# practice with property
from string import digits


class NewUser:
    def __init__(self, login, password):
        self.login = login
        self.password = password  # TAKE ATTENTION!! password in self.password is a property! Not an attribute!
    # if here will be __password in self.password, we can not check incoming data in z = NewUser('qwerty', '12k3')

    @property  # it is the default value of getter
    def password(self):
        print('getter called')
        return print(self.__password)

    @staticmethod
    def is_include_number(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @password.setter
    def password(self, value):
        print('setter called')
        if not isinstance(value, str):
            raise TypeError('The password must be string')
        if len(value) < 4:
            raise ValueError("Minimum length is 4")
        if len(value) > 12:
            raise ValueError("Maximum length is 12")
        if not NewUser.is_include_number(value):
            raise ValueError("The password must contain minimum one number")
        self.__password = value

# z = NewUser('qwerty', '12k3')
# z.password
# z.password = '22222'
# z.password
# # z.password = 'asdafsgd'
# z.password = '12w'
