from django.db import models


class Car(models.Model):
    """
    Модель Машины
    """
    name = models.CharField(verbose_name='Наименование машины', max_length=100)

    def __str__(self):
        return f'{self.id} - {self.name}'

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
