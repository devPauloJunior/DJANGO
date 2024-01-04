from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('retorno/pagseguro/', views.checkout, name='receive_notification'),
]
