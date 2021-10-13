from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

ORDER_STATUS_CHOICES = (
    ("NEW", "Новый"),
    ("IN_PROGRESS", "В процессе формирования"),
    ("DONE", "Завершен"),
)


class Product(models.Model):
    """
    Модель продукта.
    /api/v1/products/
    """
    name = models.CharField(verbose_name='Название продукта', max_length=124)
    description = models.TextField(
        max_length=1000, verbose_name='Описание продукта'
    )
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f'id: {self.id}. Название: "{self.name}"'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Order(models.Model):
    """
    Модель заказа.
    /api/v1/orders/
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        verbose_name='Заказчик', related_name='orders'
    )
    status = models.TextField(
        choices=ORDER_STATUS_CHOICES, default=ORDER_STATUS_CHOICES[0][0]
    )
    total_sum = models.DecimalField(
        max_digits=9, decimal_places=2,
        verbose_name='Итоговая стоимость заказа', blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f'Заказ №{self.id}. Покупатель: {self.user} (id:{self.user.id})'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderPositions(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="positions")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="positions")
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f"{self.order}"


class ProductReview(models.Model):
    """
    Модель отзыва.
    /api/v1/product-reviews/
    """
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000, blank=True, verbose_name='Текст')
    grade = models.SmallIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ],
        verbose_name='Оценка'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f"""
        Отзыв №{self.id}. Продукт: {self.product.name} 
        (id: {self.product.id}). Автор: {self.creator}
        """

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class ProductCollections(models.Model):
    """
    Модель подборки.
    /api/v1/product-collections/
    """
    header = models.CharField(verbose_name='Название подборки', max_length=124)
    text = models.TextField(max_length=1000, blank=True, verbose_name='Текст')
    products = models.ManyToManyField(Product, related_name='product_collections')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f'id: {self.id}. Название подборки: "{self.header}"'

    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'
