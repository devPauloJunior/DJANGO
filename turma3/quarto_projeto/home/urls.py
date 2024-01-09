from django.urls import path
from . import views
from .views import meu_home

urlpatterns = [
    path('', meu_home ),
]


