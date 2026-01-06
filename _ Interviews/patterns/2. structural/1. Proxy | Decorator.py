# These 2 patterns can have the same implementation but different aims:
# proxy - more control
# decorator - more functionality

# Common interface
class Service:
    def request(self) -> str:
        pass


# Real object
class RealService(Service):
    def request(self) -> str:
        return "real data"


# Proxy controls access to the real object
class Proxy(Service):
    def __init__(self, real: RealService, allowed: bool):
        self.real = real
        self.allowed = allowed

    def request(self) -> str:
        if not self.allowed:
            return "access denied"
        return self.real.request()


def client_code(service: Service):
    print(service.request())


# Usage
real = RealService()
proxy = Proxy(real, allowed=True)
client_code(proxy)
