from django.urls import path
from .views import home_view


urlpatterns = [
    path('', home_view, name='home'),  # пареметр name позволяет нам именовать урл для дальнейших целей
]
