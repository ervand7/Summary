from django.contrib import admin
from django.urls import path, register_converter
from app import views
from app.convertor import DateConverter


register_converter(converter=DateConverter, type_name='dtc')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-email/', views.admin_email_view, name='email'),
    path('user/', views.name_info_view, name='user'),
    path('old_date/<int:year>-<int:month>-<int:day>', views.old_date_view, name='old_date'),
    path('date/<dtc:value>/', views.date_view, name='date_1'),
    path('old_pagi/', views.old_pagi_view, name='old_pagi'),
    path('pagi/', views.pagi_view, name='pagi'),
    path('add_pagi/', views.add_pagi_view, name='add_pagi'),
]
