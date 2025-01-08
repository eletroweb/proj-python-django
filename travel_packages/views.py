from django.shortcuts import render
from .models import TravelPackages


def home(request):
    packages = TravelPackages.objects.all()
    return render(request, "travel_packages/home.html", {"packages": packages})
