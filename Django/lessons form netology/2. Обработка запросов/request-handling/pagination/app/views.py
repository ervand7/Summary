from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from urllib.parse import urlencode

from .work_with_csv import get_csv_file_content
from .consts import (
    DEFAULT_PAGE_NUMBER,
    ELEMENTS_PER_PAGE,
    PREVIOUS_PAGE,
    NEXT_PAGE,
    BASE_URI,
    PAGE_PARAMETER_KEY
)


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    """Here is written the logic of:
     paginator, working with all pages, content distribution, rendering."""

    # put down the default constants
    default_page_number = DEFAULT_PAGE_NUMBER
    elements_per_page = ELEMENTS_PER_PAGE
    previous_page, next_page = PREVIOUS_PAGE, NEXT_PAGE
    # declare the paginator
    paginator = Paginator(
        object_list=get_csv_file_content(), per_page=elements_per_page
    )
    # logic for calculating the page number
    number_of_page = int(request.GET.get(PAGE_PARAMETER_KEY, default_page_number))
    if number_of_page <= 0:
        number_of_page = default_page_number

    # logic for calculating current_page, next_page, previous_page
    current_page = paginator.get_page(number_of_page)
    if current_page.has_next():
        next_page = current_page.next_page_number()
    if current_page.has_previous():
        previous_page = current_page.previous_page_number()

    # content distribution logic
    current_page_content = current_page.object_list
    bus_stations_slice_on_page = []
    for i in range(elements_per_page):
        bus_station_data = {
            'Name': current_page_content[i]['Name'],
            'Street': current_page_content[i]['Street'],
            'District': current_page_content[i]['District']
        }
        bus_stations_slice_on_page.append(bus_station_data)
    # render logic
    next_page_url = '?'.join([BASE_URI, urlencode({PAGE_PARAMETER_KEY: next_page})])
    prev_page_url = '?'.join([BASE_URI, urlencode({PAGE_PARAMETER_KEY: previous_page})])
    context = {
        'bus_stations': bus_stations_slice_on_page,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    }
    return render(
        request=request,
        template_name='index.html',
        context=context
    )
