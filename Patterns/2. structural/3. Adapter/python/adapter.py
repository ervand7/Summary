"""
Адаптер — это структурный паттерн, который позволяет подружить
несовместимые объекты.
"""


class Target:
    """
    Целевой класс объявляет интерфейс, с которым может работать клиентский код.
    """

    def request(self) -> str:
        return "Target: The default target's behavior."


class AdaptableClass:
    """
    Адаптируемый класс содержит некоторое полезное поведение, но его интерфейс
    несовместим с существующим клиентским кодом. Адаптируемый класс нуждается в
    некоторой доработке, прежде чем клиентский код сможет его использовать.
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, AdaptableClass):
    """
    Адаптер делает интерфейс Адаптируемого класса совместимым с целевым
    интерфейсом благодаря множественному наследованию.
    """

    def request(self) -> str:
        """Именно тут мы адаптируем метод."""
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: Target) -> None:
    """
    Клиентский код поддерживает все классы, использующие интерфейс Target.
    """
    a = target.request()
    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    adaptable = AdaptableClass()
    print("Client: The Adaptable class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adaptable: {adaptable.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter()
    client_code(adapter)
