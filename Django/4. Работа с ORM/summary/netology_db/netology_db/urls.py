from django.contrib import admin
from django.urls import path

from players.views import list_players

urlpatterns = [
    path('players/', list_players, name='list-players'),
    path('admin/', admin.site.urls),
]
