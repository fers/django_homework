import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    page_number = int(request.GET.get('page', 1))

    bus_station_list = []

    with open('data-398-2018-08-30.csv', 'r', encoding='UTF-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for x in csv_reader:
            bus_station_list.append({'Name': x['Name'], 'Street': x['Street'], 'District': x['District']})

    paginator = Paginator(bus_station_list, 10)

    page = paginator.get_page(page_number)

    context = {
         'bus_stations': paginator.get_page(page_number),
         'page': page
    }
    return render(request, 'stations/index.html', context)
