import debug_toolbar
from django.contrib import admin
from django.urls import path, include

from app.views import create_shops_view, create_cars_view, add_cars_to_shop_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shops/', create_shops_view, name='shops'),
    path('cars/', create_cars_view, name='cars'),
    path('car-in-shops/', add_cars_to_shop_view, name='shops'),
    path('__debug__/', include(debug_toolbar.urls)),
]
