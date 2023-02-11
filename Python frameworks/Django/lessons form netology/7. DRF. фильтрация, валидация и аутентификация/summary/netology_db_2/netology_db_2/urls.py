from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app import api_view

router = DefaultRouter()
# router.register('cars', api_view.CarViewSetVariant3, basename='cars')
router.register(r'cars', api_view.CarViewSet, basename='cars')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls), name='cars'),
    path('api/v1/login/', api_view.LoginView.as_view()),
]
