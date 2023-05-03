# источник: https://codecamp.ru/blog/python-abstract-base-classes-abc/
"""
Абстрактные классы - это классы, которые предназначены для наследования,
но избегают реализации конкретных методов, оставляя только сигнатуры методов,
которые должны реализовывать подклассы.
"""

from abc import ABCMeta, abstractmethod


class MontyPython(metaclass=ABCMeta):
    """
    Абстрактный класс с абстрактными методами дает своим наследникам
    информацию, что эти функции нужно обязательно заоверрайдить.
    """
    @abstractmethod
    def joke(self):
        pass

    @abstractmethod
    def punchline(self):
        pass


class ArgumentClinic(MontyPython):
    """
    Если хотя бы одна (навешанная декоратором abstractmethod) функция
    родительского класса не будет переопределена в этом дочернем классе,
    то при инициализации экземпляра этого дочернего класса мы получим:
    TypeError: Can't instantiate abstract class ArgumentClinic with abstract methods punchline
    """
    def joke(self):
        return "Hahahahahah"

    def punchline(self):
        return "Send in the constable!"


c = ArgumentClinic()
