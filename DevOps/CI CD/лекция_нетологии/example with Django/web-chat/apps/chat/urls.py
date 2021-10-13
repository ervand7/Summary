from django.urls import path

from apps.chat.views import SectionView, index_view

urlpatterns = [
    path('', index_view, name='index'),
    path('chat/<int:section_id>/', SectionView.as_view(), name='section'),
]
