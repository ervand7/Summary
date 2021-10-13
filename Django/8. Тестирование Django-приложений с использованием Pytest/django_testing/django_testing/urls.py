from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from students.api_views import CoursesViewSet

router = DefaultRouter()
router.register("courses", CoursesViewSet, basename="courses")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include(router.urls)),
]
