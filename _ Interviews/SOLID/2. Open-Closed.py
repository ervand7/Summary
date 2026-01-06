from abc import ABC, abstractmethod

"""
Classes should be:
- open for extension (new behavior can be added)
- closed for modification (existing code is not changed)

We do NOT put all save logic into one class with if/else.
Instead, we define a stable abstraction (Saver) and extend it
by adding new classes.
"""


class Saver(ABC):
    @abstractmethod
    def save(self) -> None:
        pass


class FileSaver(Saver):
    def save(self) -> None:
        print("Saving to file")


class DatabaseSaver(Saver):
    def save(self) -> None:
        print("Saving to database")


# Client code depends only on the abstraction
def persist(saver: Saver) -> None:
    saver.save()


# Usage
persist(FileSaver())
persist(DatabaseSaver())


# To add a new saving method (e.g. memory),
# we create a new class instead of modifying existing ones.
class MemorySaver(Saver):
    def save(self) -> None:
        print("Saving to memory")


persist(MemorySaver())
