from django.contrib import admin
from django.urls import path

from .views import inflation_view


urlpatterns = [
    path('', inflation_view, name='main'),
    path('admin/', admin.site.urls),
]
