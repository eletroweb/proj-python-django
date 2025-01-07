from django.contrib import admin

from .models import TravelPackages


@admin.register(TravelPackages)
class TravelPackagesAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "original_price",
        "discount",
        "final_price",
    )
