# Facade provides a simple, unified interface to a complex subsystem.

# Subsystem (complex)
class AuthService:
    def authenticate(self) -> bool:
        return True


class PaymentService:
    def charge(self) -> str:
        return "payment charged"


class NotificationService:
    def notify(self) -> None:
        print("user notified")


# Facade
class CheckoutFacade:
    def checkout(self) -> str:
        auth = AuthService()
        if not auth.authenticate():
            return "auth failed"

        payment = PaymentService()
        result = payment.charge()

        NotificationService().notify()
        return result


# Client
def client_code():
    checkout = CheckoutFacade()
    print(checkout.checkout())


client_code()
