from django.shortcuts import render
from django.http import HttpResponse

def meu_home(request):
    return HttpResponse('<h1>MEU PRIMEIRO WEB APP</h1>')

