from django.shortcuts import render, redirect
from .models import Food, Consumed
from .forms import FoodModelForm
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        comida_consumida = request.POST['comida_consumida']
        print(comida_consumida)
        consumo = Food.objects.get(nome=comida_consumida)
        user = request.user
        consumo = Consumed(user=user, comida_consumida=consumo)
        consumo.save()

        foods = Food.objects.all()
    else:
        foods = Food.objects.all()

    consumida_comida = Consumed.objects.filter(user=request.user)

    print(consumida_comida)

    return render(request, 'nutrion/index.html', {'foods': foods, 'consumida_comida': consumida_comida,})

def delete_comida(request, id):
    comida_consumida = Consumed.objects.get(id=id)
    if request.method == 'POST':
        comida_consumida.delete()
        return redirect('/')
    return render(request, 'nutrion/delete.html')

def adicionar_comida(request):
    if str(request.method) == 'POST':
        form = FoodModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comida adicionada com SUCESSO!')
            form = FoodModelForm()
        else:
            messages.error(request, 'Comida NÃO cadastrada!')
    else:
        form = FoodModelForm()

    return render(request, 'nutrion/adicionar_comida.html', { 'form': form })