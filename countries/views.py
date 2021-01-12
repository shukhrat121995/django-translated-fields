from django.shortcuts import render
from .models import Country


def home(request):
    countries = Country.objects.all()
    context = {
        'countries': countries
    }
    return render(request, 'home.html', context)
