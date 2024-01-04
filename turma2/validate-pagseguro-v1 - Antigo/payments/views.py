from django.shortcuts import render
from django.http import HttpResponse
from .controller import get_session_id

def payments(request):
    controller = get_session_id()

    context = {
        'data': controller
    }
    return render(request, 'checkout.html', context)
