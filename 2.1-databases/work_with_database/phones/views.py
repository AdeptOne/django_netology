from django.db.models.functions import Lower
from django.http import HttpResponse
from django.shortcuts import render, redirect

import phones
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    template = 'catalog.html'
    if sort == 'name':
        phone_objects = Phone.objects.order_by(Lower('name'))
    elif sort =='max_price':
        phone_objects = Phone.objects.order_by('price').reverse()

    elif sort =='min_price':
        phone_objects = Phone.objects.order_by('price')
    else: phone_objects = Phone.objects.all()
    # phone_objects = Phone.objects.all()
    phones = [p for p in phone_objects]
    print(phone_objects[0])
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
