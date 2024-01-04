from django.contrib import admin
from .models import Home

class ListHome(admin.ModelAdmin):
    list_display = ('nome', 'email')

admin.site.register(Home, ListHome)
