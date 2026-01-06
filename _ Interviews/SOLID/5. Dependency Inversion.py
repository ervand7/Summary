from abc import ABC, abstractmethod

"""
High-level modules should not depend on low-level modules.
Both should depend on abstractions.

Abstractions should not depend on details.
Details should depend on abstractions.

Computer is a high-level class.
SaveToFile / SaveToDB are low-level details.
Computer depends only on Saver (abstraction), not on concrete classes.
"""


class Saver(ABC):
    @abstractmethod
    def save(self) -> None:
        pass


# Low-level modules (details)
class FileSaver(Saver):
    def save(self) -> None:
        print("Saving to file")


class DatabaseSaver(Saver):
    def save(self) -> None:
        print("Saving to database")


# High-level module
class Computer:
    def __init__(self, saver: Saver) -> None:
        self._saver = saver

    def save(self) -> None:
        self._saver.save()


# Usage
Computer(FileSaver()).save()
Computer(DatabaseSaver()).save()
