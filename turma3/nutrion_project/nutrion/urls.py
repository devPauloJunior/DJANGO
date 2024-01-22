from django.urls import path
from .views import index, delete_comida, adicionar_comida

urlpatterns = [
    path('', index, name='index'),
    path('delete/<int:id>', delete_comida, name='delete'),
    path('adicionar_comida', adicionar_comida, name='adicionar_comida'),
]
