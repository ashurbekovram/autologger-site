from django.contrib import admin
from vehicles.models import *


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'founding_date', 'country')
    list_display_links = ('id', 'name')


class SeriesAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__')
    list_display_links = ('id', '__str__',)
    ordering = ('brand', 'name')


class GenerationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'series', 'start_year', 'end_year')
    list_display_links = ('id', 'name')
    list_filter = ('series',)
    ordering = ('series', 'start_year')


admin.site.register(Country, CountryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Generation, GenerationAdmin)
