from django.urls import path
from .views import home_view, time_view, home_view2, home_view3, time_view2, home_view4, home_view5, detail_view

urlpatterns = [
    path('', home_view, name='home'),
    path('2', home_view2, name='home2'),
    path('3', home_view3, name='home3'),
    path('4', home_view4, name='home4'),
    path('5', home_view5, name='home5'),
    path('time/', time_view, name='time-page'),
    path('time2/', time_view2, name='time-page2'),
    path('cart/<str:car_name>/', detail_view, name='detail-page')

]
