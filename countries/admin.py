from django.contrib import admin
from .models import Country
from translated_fields import TranslatedFieldAdmin


@admin.register(Country)
class CountryAdmin(TranslatedFieldAdmin, admin.ModelAdmin):
    list_display = ['name_en', 'name_ru', 'name_uz']


