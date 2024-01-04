from django.shortcuts import render
from django.http import HttpResponse

def about_us(request):
    return render(request, 'about_us/index.html')
