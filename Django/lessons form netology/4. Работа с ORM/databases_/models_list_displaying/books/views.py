from django.conf import settings
from django.http import HttpResponseNotFound
from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.order_by('pub_date').all()
    context = {'books': books}
    return render(request, template, context)


def book_view(request, dt):
    template = 'books/book.html'
    books = [*Book.objects.filter(pub_date=dt).order_by('pub_date').all()]
    if not books:
        return HttpResponseNotFound(settings.BOOK_NOT_FOUND_MSG)
    dates = Book.objects.values('pub_date').order_by('pub_date').distinct()
    dates = [item['pub_date'] for item in dates]
    pos = dates.index(dt)
    prev_page_url = dates[pos-1] if pos > 0 else ''
    next_page_url = dates[pos+1] if pos < len(dates)-1 else ''
    context = {'books': books, 'prev_page_url': prev_page_url, 'next_page_url': next_page_url}
    return render(request, template, context)
