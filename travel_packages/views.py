from django.shortcuts import render
from .models import TravelPackages


def home(request):
    travel_packages = TravelPackages.objects.all()
    return render(
        request, "travel_packages/home.html", {"travel_packages": travel_packages}
    )
