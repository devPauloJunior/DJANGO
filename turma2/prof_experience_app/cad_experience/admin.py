from django.contrib import admin
from .models import CadExperience

class ListCadExperience(admin.ModelAdmin):
    list_display = ('cadexperience_id', 'cadexperience_first_name', 'cadexperience_last_name', 'cadexperience_degree')

admin.site.register(CadExperience, ListCadExperience)
