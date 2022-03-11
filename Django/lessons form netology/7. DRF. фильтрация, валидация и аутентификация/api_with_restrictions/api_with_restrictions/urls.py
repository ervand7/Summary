from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from advertisements.api_views import AdvertisementViewSet

router = DefaultRouter()
router.register(
    'api/v1/advertisements', AdvertisementViewSet, basename='advertisements'
)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
