from django.urls import path, re_path

from women.views import index, categories, archive

urlpatterns = [
    path('', index, name='home'),  # чтобы можно было потом по аналогии с Flask url_for вызывать урл по имени
    path('cats/<slug:cat>/', categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]
