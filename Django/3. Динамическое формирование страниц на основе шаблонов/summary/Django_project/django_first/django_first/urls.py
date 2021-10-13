from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))  # таким образом мы из файла урлов какого-то
    # конкретного приложения импортируем эти урлы
]
