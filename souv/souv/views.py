from django.shortcuts import render
from .models import Country, Gift


def index_map(request):
    
    return render(request, "index.html")


def country_detail(request, country_name):
    gifts = Gift.objects.filter(country__country__name=country_name)
    print(gifts)

    context = {
        'country_name': country_name,
        'gifts': gifts,
    }
    return render(request, "detail.html", context)



