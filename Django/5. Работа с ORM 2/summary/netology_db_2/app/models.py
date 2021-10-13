from django.db import models


# Это 1й вариант реализации m2m, через ManyToManyField
class CarShop(models.Model):
    """
    Модель Салон
    """
    name = models.CharField(verbose_name='Наименование магазина', max_length=254)
    # благодаря следующему полю у на с БД появится таблица app_carshop_car (m2m).
    # Аргумент related_name нужен для обратной связи. Тут в значении этого аргумента мы можем прописать любое слово,
    # главное, потом это слово прописать во view-функции, когда нам нужно будет получить данные через
    # обратную связь. Например: x = Car.objects.first().это_слово.all()
    # Аргумент related_name должен быть прописан всегда.
    # Через through='CarInShop' мы говорим, что m2m у нас будет уже не через эту модель, в через CarInShop
    car = models.ManyToManyField('Car', related_name='shops', through='CarInShop')

    def __str__(self):
        return f'{self.id} - {self.name}'


class Car(models.Model):
    """
    Модель Машины
    """
    name = models.CharField(verbose_name='Наименование машины', max_length=254)

    def __str__(self):
        return f'{self.id} - {self.name}'


# Это 2й вариант реализации m2m, через ForeignKey
class CarInShop(models.Model):
    shop = models.ForeignKey(CarShop, verbose_name='Shop', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, verbose_name='Car', on_delete=models.CASCADE)
    is_custom = models.BooleanField(verbose_name='Кастомная машина', default=False)  # default=False означает,
    # что по умолчанию все машины у нас будут не кастомные

    def __str__(self):
        return f'{self.id} - {self.shop} | {self.car}'
