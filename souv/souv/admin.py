from django_countries.fields import CountryField
from django_select2.forms import Select2Widget
from django.contrib import admin
from .models import Country, Gift

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        CountryField: {'widget': Select2Widget},
    }

@admin.register(Gift)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', ]