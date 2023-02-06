# creating Singleton. This class can create only one exemplar
class Singleton:
    __count = 0
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Singleton, cls).__new__(cls)
        else:
            print('Экземпляр класса Singleton уже создан')
        return cls.__instance

    def __init__(self, x=0, y=0):
        self.__count += 1
        self.x = x
        self.y = y

    @staticmethod
    def get_count():
        return self.__count


s1 = Singleton()
s2 = Singleton()  # Экземпляр класса Singleton уже создан
s3 = Singleton()  # Экземпляр класса Singleton уже создан
s4 = Singleton()  # Экземпляр класса Singleton уже создан
print(id(s1), id(s2), id(s3), id(s4))
