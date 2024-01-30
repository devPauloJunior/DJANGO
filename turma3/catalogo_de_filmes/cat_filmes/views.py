from django.shortcuts import render, redirect
from .models import Filme
from django.contrib import messages
from .forms import FilmeForm

def index(request):
    filmes = Filme.objects.all()
    context = {
        'filmes': filmes, 
    }
    return render(request, 'cat_filmes/index.html', context)

def cadastro(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Filme cadastrado com Sucesso!')
            form = FilmeForm()
        else:
            messages.error(request, 'Erro ao salva o Filme!')
    else:
        form = FilmeForm()
    
    return render(request, 'cat_filmes/cadastro.html', { 'form': form})

def deletar(request, id):
    deleteme = Filme.objects.get(id=id)
    if request.method == 'POST':
        deleteme.delete()
        return redirect('/')
    return render(request, 'cat_filmes/deletar.html')