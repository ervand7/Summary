class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def balance(self):
        print('getter called')
        return self.__balance

    @balance.setter
    def balance(self, value):
        print('setter called')
        if not isinstance(value, (int, float)):
            raise ValueError('The balance must de a number')
        self.__balance = value

    @balance.deleter
    def balance(self):
        print('deleter called')
        del self.__balance


d = BankAccount('Masha', 400)
print(d.balance)  # getter called 400

d.balance = 789
# setter called

del d.balance
# deleter called
