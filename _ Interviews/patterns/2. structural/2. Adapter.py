"""
Адаптер — это структурный паттерн, который позволяет подружить
несовместимые объекты.
"""


# What the client expects
class Target:
    def request(self) -> str:
        pass


# Existing class with incompatible interface
class Adaptee:
    def specific_request(self) -> str:
        return "data from adaptee"


# Adapter makes Adaptee look like Target
class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee

    def request(self) -> str:
        return self.adaptee.specific_request()


def client_code(target: Target):
    print(target.request())


# Usage
adaptee = Adaptee()
adapter = Adapter(adaptee)
client_code(adapter)
