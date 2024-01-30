from django.shortcuts import render
from django.contrib import messages
from .models import AtracaoTuristica
from .forms import AtracaoTuristicaForm

def index(request):
    atracoes_turisticas = AtracaoTuristica.objects.all()
    return render(request, 'atracoes_turisticas/index.html', {'atracoes_turisticas': atracoes_turisticas})

def register(request):
    if request.method == 'POST':
        form = AtracaoTuristicaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Atração Turística Cadastrado')
            form = AtracaoTuristicaForm()
        else:
            messages.error(request, 'Erro ao cadastrar')
    else:
        form = AtracaoTuristicaForm()

    return render(request, 'atracoes_turisticas/register.html', { 'form': form })