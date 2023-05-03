class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def balance(self):
        print(f'get balance, {self.__balance}')
        return self.__balance

    @balance.setter
    def balance(self, value):
        print(f'set balance, {value}')
        if not isinstance(value, (int, float)):
            raise ValueError('The balance must de a number')
        self.__balance = value

    @balance.deleter
    def balance(self):
        print('delete balance')
        del self.__balance
