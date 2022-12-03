from django.contrib import admin
from .models import *


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'founding_date', 'country')
    list_display_links = ('id', 'name')


admin.site.register(Country, CountryAdmin)
admin.site.register(Brand, BrandAdmin)
