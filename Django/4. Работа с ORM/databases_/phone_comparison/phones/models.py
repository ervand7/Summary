from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    name = models.TextField(null=True)
    image = models.TextField(null=True)
    brand = models.TextField(null=True)
    weight = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    release_date = models.DateField(null=True)
    additional_info = models.TextField(null=True)
    slug = models.TextField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(' '.join((str(self.name), str(self.release_date))))
        super(Phone, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class PhoneApple(Phone):
    video_acc = models.TextField()


class PhoneSamsung(Phone):
    max_card_size = models.IntegerField()


class PhoneNokia(Phone):
    fm_radio = models.BooleanField()
