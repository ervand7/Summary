import debug_toolbar
from django.urls import path, include

from .views import articles_list_view

urlpatterns = [
    path('', articles_list_view, name='articles'),
    path('__debug__/', include(debug_toolbar.urls))
]
