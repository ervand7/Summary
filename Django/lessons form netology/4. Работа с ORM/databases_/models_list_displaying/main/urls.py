from django.conf import settings
from django.contrib import admin
from django.urls import path, register_converter, include
from books.views import books_view, book_view
from books.converters import DateConverter

register_converter(DateConverter, 'date')

urlpatterns = [
    path('', books_view, name='books'),
    path('books/', books_view, name='books'),
    path('books/<date:dt>/', book_view, name='book_date'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
