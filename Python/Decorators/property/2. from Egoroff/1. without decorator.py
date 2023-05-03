class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print('get balance called')
        return self.__balance

    def set_balance(self, value):
        print('set balance called')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    def delete_balance(self):
        print('delete balance called')
        del self.__balance

    balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)


d = BankAccount('Masha', 400)
print(d.balance)  # 400

d.balance = 789
d.balance = 'qwe'  # ERROR
del d.balance
