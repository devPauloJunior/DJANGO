from django.shortcuts import render
from .forms import ContatoForm, ProdutoModelForm
from django.contrib import messages

def index(request):
    return render(request, 'home/index.html')

def contato(request):
    form = ContatoForm(request.POST)

    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar seu e-mail!')

    context = {
        'form': form
    }

    return render(request, 'home/contato.html', context)

def produto(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            prod = form.save(commit=False)

            print(f'Nome: {prod.nome_produto}')
            print(f'Preco: {prod.preco}')
            print(f'Imagem: {prod.imagem_produto}')
            print(f'Descricao: {prod.descricao}')

            messages.success(request, 'Produto cadastrado com sucesso')
            form = ProdutoModelForm()
        else:
            messages.error(request, 'Erro ao cadastra produto')
    else:
        form = ProdutoModelForm()

    context = {
        'form': form
    }
    return render(request, 'home/produto.html', context)


