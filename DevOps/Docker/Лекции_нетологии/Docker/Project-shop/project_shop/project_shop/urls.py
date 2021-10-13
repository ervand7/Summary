import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.api_views import (
    ProductViewSet, OrderViewSet, ProductReviewViewSet, ProductCollectionsViewSet
)

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('orders', OrderViewSet, basename='orders')
router.register('product-reviews', ProductReviewViewSet, basename='product-reviews')
router.register('product-collections', ProductCollectionsViewSet, basename='product-collections')


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls))
]
