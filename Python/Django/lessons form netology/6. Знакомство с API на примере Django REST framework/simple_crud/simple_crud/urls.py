import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from measurements import api_views

router = DefaultRouter()
router.register('projects', api_views.ProjectViewSet, basename='projects')
router.register('measurements', api_views.MeasurementViewSet, basename='measurements')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls), name='experiment'),
    path('__debug__/', include(debug_toolbar.urls))
]
