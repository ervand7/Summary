import debug_toolbar
from django.urls import path, include

from school.views import students_list

urlpatterns = [
    path('', students_list, name='students'),
    path('__debug__/', include(debug_toolbar.urls))
]
