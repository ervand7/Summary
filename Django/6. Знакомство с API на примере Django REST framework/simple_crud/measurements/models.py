from django.db import models


class TimestampFields(models.Model):
    """
    Объявляем этот класс абстрактным, его невозможно инстанцировать и он не имеет своей таблицы, все наследники
    от него становятся реальными классами, пока у них также не будет объявлено abstract = True
    https://docs.djangoproject.com/en/3.1/topics/db/models/#abstract-base-classes
    """
    created_at = models.DateTimeField(
        auto_now_add=True  # автоматическое проставление даты при создании
    )
    updated_at = models.DateTimeField(
        auto_now=True  # автоматическое проставление даты при обновлении
    )

    class Meta:
        abstract = True


class Project(TimestampFields):
    """Объект на котором проводят измерения."""
    name = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Объект на карте'
        verbose_name_plural = 'Объекты на карте'


class Measurement(TimestampFields):
    """Измерение температуры на объекте."""
    value = models.FloatField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    photo = models.ImageField(  # этот класс провалидирует, чтобы файл был именно изображением
        verbose_name='Фото',
        # говорим, что это поле необязательно к заполнению
        null=True,
        blank=True

    )

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = 'Результат измерения'
        verbose_name_plural = 'Результаты измерения'
