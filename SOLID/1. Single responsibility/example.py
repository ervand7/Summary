from abc import ABC, abstractmethod

"""
Class should only do one job. Otherwise class becomes dependent.
We could just write the save methods in Computer. But so we load Computer excess
responsibility.
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
