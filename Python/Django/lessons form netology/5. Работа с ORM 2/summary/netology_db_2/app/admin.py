from django.contrib import admin

from .models import Car, CarShop


class CarShopInline(admin.TabularInline):
    """
    Этот класс создается для того, чтобы потом в админке при создании машины
    можно было сразу прикрепить к ней магазин.
    """
    model = CarShop.car.through
    # где CarShop - модель, внутри которой реализовано m2m, car - поле, по которому идет связь, through - специальный менеджер
    extra = 1  # кол-во предлягаемых вариантов, которые выводятся по умолчанию


# теперь в наших моделях прописываем, что они инлайновые

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    inlines = [
        CarShopInline
    ]


@admin.register(CarShop)
class CarShopAdmin(admin.ModelAdmin):
    inlines = [
        CarShopInline
    ]

    exclude = ('car', )  # так мы исключаем старую (уже не нужную сущность) 'car'

