from abc import ABCMeta, abstractmethod


class Beer(metaclass=ABCMeta):
    pass


class Snack(metaclass=ABCMeta):
    @abstractmethod
    def interact(self, beer: Beer) -> None:
        raise NotImplemented


class Shop(metaclass=ABCMeta):
    @abstractmethod
    def buy_beer(self) -> Beer:
        raise NotImplemented

    @abstractmethod
    def buy_snack(self) -> Snack:
        raise NotImplemented


class Tuborg(Beer):
    pass


class Staropramen(Beer):
    pass


class Peanuts(Snack):
    def interact(self, beer: Beer) -> None:
        print('Мы выпили по бутылке пива {} и закусили его арахисом'.format(
            beer.__class__.__name__))


class Chips(Snack):
    def interact(self, beer: Beer) -> None:
        print('Мы выпили несколько банок пива {} и съели пачку чипсов'.format(
            beer.__class__.__name__))


class ExpensiveShop(Shop):
    def buy_beer(self) -> Beer:
        return Tuborg()

    def buy_snack(self) -> Snack:
        return Peanuts()


class CheapShop(Shop):
    def buy_beer(self) -> Beer:
        return Staropramen()

    def buy_snack(self) -> Snack:
        return Chips()


if __name__ == '__main__':
    expensive_shop = ExpensiveShop()
    cheap_shop = CheapShop()
    print('OUTPUT:')
    beer = expensive_shop.buy_beer()
    snack = cheap_shop.buy_snack()
    snack.interact(beer)

    beer = cheap_shop.buy_beer()
    snack = expensive_shop.buy_snack()
    snack.interact(beer)

'''
OUTPUT:
Мы выпили несколько банок пива Tuborg и съели пачку чипсов
Мы выпили по бутылке пива Staropramen и закусили его арахисом
'''
