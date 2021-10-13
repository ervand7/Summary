from django.conf import settings
from django.db import models

STATUS_CHOICES = (
    ("OPEN", "Открыто"),
    ("CLOSED", "Закрыто"),
)


class Advertisement(models.Model):
    """Объявление."""

    title = models.TextField()
    description = models.TextField(default='')
    status = models.TextField(
        choices=STATUS_CHOICES, default=STATUS_CHOICES[0]
    )
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id} - {self.title}'

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
