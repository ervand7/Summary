from django.urls import path

from .views import landing, stats, index


urlpatterns = [
    path('', index, name='index'),
    path('landing/', landing, name='landing'),
    path('stats/', stats, name='stats'),
]
