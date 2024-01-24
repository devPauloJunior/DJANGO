from django.shortcuts import render
from django.contrib import messages
from .models import PontoTuristico
from .forms import PontoTuristicoForm

def index(request):
    pontos_turisticos = PontoTuristico.objects.all()
    return render(request, 'pontos_turisticos/index.html', {'pontos_turisticos': pontos_turisticos})

def register(request):
    if request.method == 'POST':
        form = PontoTuristicoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ponto Turístico Cadastrado')
            form = PontoTuristicoForm()
        else:
            messages.error(request, 'Erro ao cadastrar')
    else:
        form = PontoTuristicoForm()

    return render(request, 'pontos_turisticos/register.html', { 'form': form })