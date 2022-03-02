from django.http import HttpResponse
from django.shortcuts import render, redirect

import phones
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone_objects = Phone.objects.all()
    phones = [p for p in phone_objects]
    print(phones)
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = (Phone.objects.filter(slug=slug))[0]
    context = {
        'phone': phone
    }
    return render(request, template, context)
