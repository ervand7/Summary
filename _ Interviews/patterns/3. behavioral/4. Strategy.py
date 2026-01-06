# Strategies
class PaymentStrategy:
    def pay(self, amount: int):
        pass


class CardPayment(PaymentStrategy):
    def pay(self, amount: int):
        print(f"Pay {amount} by card")


class CryptoPayment(PaymentStrategy):
    def pay(self, amount: int):
        print(f"Pay {amount} by crypto")


# Context
class Checkout:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def process(self, amount: int):
        self.strategy.pay(amount)


# Usage
Checkout(CardPayment()).process(100)
Checkout(CryptoPayment()).process(100)
