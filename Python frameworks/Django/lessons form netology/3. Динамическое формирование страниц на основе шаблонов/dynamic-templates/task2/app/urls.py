from django.contrib import admin
from django.urls import path

from .views import home_view, about_view, contacts_view, \
    examples_view


urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contacts/', contacts_view, name='contacts'),
    path('examples/', examples_view, name='examples'),
    path('admin/', admin.site.urls),
]
