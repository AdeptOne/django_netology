import csv
from pprint import pprint

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open('data-398-2018-08-30.csv',newline='', encoding='UTF-8') as f:
        reader = list(csv.reader(f))
        bus_stations = []
        for count, element in enumerate(reader):
            bus_stations.append({'Name': element[1], 'Street': element[4], 'District': element[6]})

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(bus_stations, 10)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
