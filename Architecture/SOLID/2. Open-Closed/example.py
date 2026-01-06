from abc import ABC, abstractmethod

"""
Classes must be open for extending but not for modification.
We could just make only one class Saver, which implements methods save_to_file
and save_to_db. But so we need to modify Saver every time we need to add
a new method, fo example save_to_memory. 
And now we can just extend abstract class Saver with inherit classes.
"""


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
