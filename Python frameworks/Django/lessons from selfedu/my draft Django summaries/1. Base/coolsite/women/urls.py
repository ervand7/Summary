from django.urls import path, re_path

from women.views import (
    index, categories, archive, about, addpage, contact, login, show_post
)

urlpatterns = [
    path('', index, name='home'),  # чтобы можно было потом по аналогии с Flask url_for обращаться к урлу по имени
    path('cats/<slug:cat>/', categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),  # custom filter
    path('about/', about, name='about'),

    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', show_post, name='show_post'),
]
