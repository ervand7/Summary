from django.contrib import admin

from .models import Product, Order, ProductReview, ProductCollections, OrderPositions


class OrderInline(admin.TabularInline):
    model = OrderPositions
    extra = 1  # кол-во предлягаемых вариантов, которые выводятся по умолчанию


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderInline
    ]


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductCollections)
class ProductCollectionsAdmin(admin.ModelAdmin):
    pass
