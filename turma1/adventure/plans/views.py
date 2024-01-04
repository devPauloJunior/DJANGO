from django.shortcuts import render
from django.http import HttpResponse
from .models import Plans

def plans(request):
    my_plans = Plans.objects.all()

    context = {
        'planos': my_plans,
    }

    return render(request, 'plans/index.html', context)
