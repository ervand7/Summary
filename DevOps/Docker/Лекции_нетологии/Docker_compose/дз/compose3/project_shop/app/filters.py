from django_filters import rest_framework as filters
from django.contrib.auth.models import User
from app.models import Product, Order, ProductReview, ProductCollections, ORDER_STATUS_CHOICES


class ProductFilter(filters.FilterSet):
    """
    Фильтры для класса Product.
    Запрос без фильтров выглядит так: GET http://127.0.0.1:8000/api/v1/products/
    """

    id = filters.ModelMultipleChoiceFilter(
        to_field_name="id", queryset=Product.objects.all()
    )
    # http://127.0.0.1:8000/api/v1/products/?price_gte=200
    price_gte = filters.NumberFilter(field_name='price', lookup_expr='gte')
    # http://127.0.0.1:8000/api/v1/products/?price_lte=100
    price_lte = filters.NumberFilter(field_name='price', lookup_expr='lte')

    # GET http://127.0.0.1:8000/api/v1/products/?name=олоко
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    # GET http://127.0.0.1:8000/api/v1/products/?description=вес
    description = filters.CharFilter(field_name='description', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ("id", "price", "name", "description")


class ProductReviewFilter(filters.FilterSet):
    id = filters.ModelMultipleChoiceFilter(
        to_field_name="id", queryset=ProductReview.objects.all()
    )
    # DateFromToRangeFilter потом сам добавит (в урле) окончания _before и _after к нашему created_at
    # http://127.0.0.1:8000/api/v1/product-reviews/?created_at_before=2021-07-31
    # http://127.0.0.1:8000/api/v1/product-reviews/?created_at_after=2021-07-31
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = ProductReview
        fields = ("id", "creator", "product", "created_at")


class ProductCollectionsFilter(filters.FilterSet):
    class Meta:
        model = ProductCollections
        fields = ("id",)


class OrderFilter(filters.FilterSet):
    """
    Фильтры для класса Order.
    Запрос без фильтров выглядит так: GET http://127.0.0.1:8000/api/v1/orders/
    """
    # http://127.0.0.1:8000/api/v1/orders/?id=148
    id = filters.ModelMultipleChoiceFilter(
        to_field_name="id", queryset=Order.objects.all()
    )

    # http://127.0.0.1:8000/api/v1/orders/?user_id=2
    user_id = filters.ModelMultipleChoiceFilter(
        to_field_name='id', queryset=User.objects.all())

    # http://127.0.0.1:8000/api/v1/orders/?status=DONE
    status = filters.ChoiceFilter(choices=ORDER_STATUS_CHOICES)

    # http://127.0.0.1:8000/api/v1/orders/?total_sum_gte=700
    total_sum_gte = filters.NumberFilter(field_name='total_sum', lookup_expr='gte')
    # http://127.0.0.1:8000/api/v1/orders/?total_sum_lte=650
    total_sum_lte = filters.NumberFilter(field_name='total_sum', lookup_expr='lte')

    # http://127.0.0.1:8000/api/v1/orders/?created_at_before=2021-08-02
    # http://127.0.0.1:8000/api/v1/orders/?created_at_after=2021-08-03
    created_at = filters.DateFromToRangeFilter()

    # http://127.0.0.1:8000/api/v1/orders/?updated_at_before=2021-08-02
    # http://127.0.0.1:8000/api/v1/orders/?updated_at_after=2021-08-03
    updated_at = filters.DateFromToRangeFilter()

    # http://127.0.0.1:8000/api/v1/orders/?product_name=Potato
    product_name = filters.CharFilter(
        field_name="positions__product__name",
        lookup_expr="icontains"
    )

    class Meta:
        model = Order
        fields = (
            "id", "user_id", "status", "total_sum",
            "created_at", "updated_at", "product_name"
        )
