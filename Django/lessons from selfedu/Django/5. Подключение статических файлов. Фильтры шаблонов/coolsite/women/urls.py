from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
]
