from django.db import models
from django.db.models import (
    PositiveIntegerField, URLField, DateField, BooleanField, SlugField
)
from django.utils.text import slugify


class Phone(models.Model):

    name = models.CharField(max_length=250, verbose_name='Наименование')
    image = URLField(max_length=400)
    price = PositiveIntegerField(default='цена не указана')
    release_date = DateField(blank=True)
    lte_exists = BooleanField()
    slug = SlugField(max_length=200, allow_unicode=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.name))
        super().save(*args, **kwargs)

    def __str__(self):
        """Это мы прописываем, чтобы в дебагере
        мы получали строковое представление объекта."""
        return self.name
