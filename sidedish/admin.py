# -*- coding: utf-8 -*
from django.contrib import admin
from django import forms

from .models import Dish


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        widgets = {
            'visibility': forms.RadioSelect(),
        } 


class DishAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'side', 'weight']
    search_fields = ['title', 'side', 'weight']
    list_filter = ['side',]
    list_editable = ['weight', 'side',]
    form = DishForm
    fieldsets = (
        (None, {
            'fields': (('title', 'show_title'), 'slug', 'weight', 'content',)
        }),
        ('Publication', {
            'classes': ('collapse',),
            'fields': ('publish_date', 'expiry_date', 'status', 'side', 'visibility', 'pages',)
        }),
    )

admin.site.register(Dish, DishAdmin)
