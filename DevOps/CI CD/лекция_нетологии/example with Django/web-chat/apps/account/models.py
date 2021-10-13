from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    avatar = models.ImageField(
        upload_to='images/user/avatars', null=True, blank=True,
    )

    def save(self, *args, **kwargs):
        if not self.email:
            raise ValueError('email is required')
        super().save(*args, **kwargs)
