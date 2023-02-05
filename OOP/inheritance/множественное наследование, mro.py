class Doctor:
    def can_cure(self):
        print('Я доктор, я умею лечить')

    def graduate(self):
        print('Ура! Я отучился на доктора')

    def can_build(self):
        print('Я доктор, я тоже умею строить, но не очень')


class Builder:
    def can_build(self):
        print('Я строитель, я умею строить')

    def graduate(self):
        print('Ура! Я отучился на строителя')


class Person(Doctor, Builder):
    def graduate(self):
        print('Посмотрим, кем я стал')
        super().graduate()

        # А это нужно в том лишь случае, если мы хотим, чтобы вывелся метод и
        # у второго записанного родителя:
        Builder.graduate(self)


p = Person()
p.can_build()  # Я доктор, я тоже умею строить, но не очень
p.can_cure()  # Я доктор, я умею лечить

p.graduate()
# Посмотрим, кем я стал
# Ура! Я отучился на доктора
# Ура! Я отучился на строителя

print(Person.__mro__)
# (<class '__main__.Person'>, <class '__main__.Doctor'>, <class '__main__.Builder'>, <class 'object'>)
