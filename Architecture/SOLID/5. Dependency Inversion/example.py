from abc import ABC, abstractmethod

"""
Classes must depend on interfaces, bt not on specific classes.
We could accept concrete SaveToFile or concrete SaveToDB in __init__.
But in this way we restrict class Computer to accept ather Saver classes.
"""


class Computer:
    def __init__(self, saver: 'Saver'):
        self.saver = saver


class Saver(ABC):
    @abstractmethod
    def save(self):
        raise NotImplementedError()


class SaveToFile(Saver):
    def save(self):
        print('I save to file')


class SaveToDB(Saver):
    def save(self):
        print('I save to db')
