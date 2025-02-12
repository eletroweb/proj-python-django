from django.contrib import admin

from .models import TravelPackages

from django.db import models

from tinymce.widgets import TinyMCE


@admin.register(TravelPackages)
class TravelPackagesAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "original_price",
        "discount",
        "final_price",
    )

    formfield_overrides = {models.TextField: {"widget": TinyMCE()}}
