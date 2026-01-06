"""
Factory method is a method of class which sets some behavior
fore some entity (e.g. class attribute) during itself call.
"""


class Culture:
    def __repr__(self):
        return self.__str__()


class Democracy(Culture):
    def __str__(self):
        return 'Democracy'


class Dictatorship(Culture):
    def __str__(self):
        return 'Dictatorship'


class Government:
    """Само правительство"""
    culture = ''

    def __str__(self):
        return self.culture.__str__()

    def __repr__(self):
        return self.culture.__repr__()

    def set_culture(self):
        """Задать строй правительству: это и есть наш Фабричный Метод"""
        raise AttributeError('Not Implemented Culture')


class GovernmentA(Government):
    def set_culture(self):
        self.culture = Democracy()


class GovernmentB(Government):
    def set_culture(self):
        self.culture = Dictatorship()


g1 = GovernmentA()
g1.set_culture()
print(str(g1))  # Democracy

g2 = GovernmentB()
g2.set_culture()
print(str(g2))  # Dictatorship
