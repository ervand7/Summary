from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class Car(AbstractBaseUser):
    """
    Модель Машины
    """
    name = models.CharField(verbose_name='Наименование машины', max_length=100)
    amount = models.IntegerField(verbose_name='Кол-во в ниличии')
    username = models.EmailField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    password = models.CharField(
        # null=True означает, что данное поле может быть null в БД
        # blank=True означает, что это поле может не заполняться в админке
        verbose_name='Пароль от машины', max_length=10, null=True, blank=True
    )
    password_confirm = models.CharField(
        verbose_name='Подтверждение пароля от машины', max_length=10, null=True, blank=True
    )

    def __str__(self):
        return f'{self.id} - {self.name}'

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
