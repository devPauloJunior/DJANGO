from django.shortcuts import render
from .models import Home

def home(request):
    my_cad = Home.objects.all()

    context = {
        'pessoas': my_cad,
    }
    return render(request, 'home/index.html', context)
