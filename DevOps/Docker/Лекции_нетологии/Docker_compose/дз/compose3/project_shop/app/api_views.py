from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from app.models import Order

from app.custom_permissions import (
    ProductCreatePermission,
    OrderCreatePermission,
    OrderRetrieveDestroyPermission,
    OrderListPermission,
    OrderUpdatePartialUpdatePermission,
    ProductReviewCreatePermission,
    ProductReviewUpdatePartialUpdateDestroyPermission,
    ProductCollectionsPermission,
)
from app.filters import (
    ProductFilter,
    OrderFilter,
    ProductReviewFilter,
    ProductCollectionsFilter
)
from app.models import Product, Order, ProductReview, ProductCollections
from .serializers.order_serializer import OrderSerializer
from .serializers.product_collection_serializer import ProductCollectionsSerializer
from .serializers.product_review_serializer import ProductReviewSerializer
from .serializers.product_serializer import ProductSerializer


class ProductViewSet(ModelViewSet):
    """
    ViewSet для класса Product.
    Поскольку наш вью-класс наследуется от ModelViewSet, мы должны заполнить
    4 обязательных поля: queryset, serializer_class, filter_backends и filterset_class.
    Далее, уже под капотом, ModelViewSet распарсит эти поля.
    """
    # следующие 3 аттрибута оверрайдятся из GenericApiView
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def get_permissions(self):
        """
        Функция определения прав для действий.
        Внимание! Здесь мы оверрайдим родительский метод get_permissions
        """
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [ProductCreatePermission()]
        return []


class OrderViewSet(ModelViewSet):
    """
    ViewSet для класса Order.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilter

    def get_permissions(self):
        if self.action in ["create"]:
            return [OrderCreatePermission()]
        elif self.action in ["list"]:
            return [OrderListPermission()]
        elif self.action in ["retrieve", "destroy"]:
            return [OrderRetrieveDestroyPermission()]
        elif self.action in ["update", "partial_update"]:
            return [OrderUpdatePartialUpdatePermission()]
        return []

    def get_queryset(self):
        """
        В этом заоверрайденном методе мы можем определить, какие объекты будут
        отдаваться из БД в зависимости от токена пользователя. Далее
        уже данные пойдут на фильтрацию.
        """
        user = self.request.user
        if user.is_superuser:
            return Order.objects.prefetch_related("positions").all()
        # user будет иметь поле orders благодаря related_name
        return user.orders.prefetch_related("positions").all()


class ProductReviewViewSet(ModelViewSet):
    """
    ViewSet для класса ProductReview.
    """
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductReviewFilter

    def get_permissions(self):
        if self.action in ["create"]:
            return [ProductReviewCreatePermission()]
        elif self.action in ["update", "partial_update", "destroy"]:
            return [ProductReviewUpdatePartialUpdateDestroyPermission()]
        return []


class ProductCollectionsViewSet(ModelViewSet):
    """
    ViewSet для класса ProductCollections.
    """
    queryset = ProductCollections.objects.all()
    serializer_class = ProductCollectionsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductCollectionsFilter

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [ProductCollectionsPermission()]
        return []
