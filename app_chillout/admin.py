from django.contrib import admin
from .models import  Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'descrtiption', 'created_date', 'acution']
    list_filter = ['created_at', 'acution']

admin.site.register(Advertisement, AdvertisementAdmin)

# Register your models here.
