from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from decouple import config
from checkouts.controller import PagSeguroApiTransparent
import requests
import xmltodict

from checkouts.forms import *
from checkouts.config import SESSION_URL

#Curl
def get_session_id():
    url = SESSION_URL
    payload = {
        'email': config('PAGSEGURO_EMAIL'), 
        'token': config('PAGSEGURO_TOKEN'),
    }
    
    headers = { 'Content-Type': 'application/x-www-form-urlencoded', 'charset': 'UTF-8' }
    result = requests.post(url, params=payload, headers=headers )
    
    if result.status_code == 200:
            root = xmltodict.parse(result.text)
            root = xmltodict.parse(result.text)
            data = {
                "id": root["session"]["id"],
                "status_code": result.status_code,
           }
            # print(result.url)
            # print(result.text)
            # print(data['id'])
    
    return data

def checkout(request):
    session_id = get_session_id()
    context = {
        'session_id': session_id,
    }
    return render(request, 'checkouts/checkout.html', context)

@csrf_exempt
@require_http_methods(["POST"])
def receive_notification(request):
    notification_code = request.POST.get("notificationCode", None)
    notification_type = request.POST.get("notificationType", None)

    if notification_code and notification_type == "transaction":
        pagseguro_api = PagSeguroApiTransparent()
        response = pagseguro_api.get_notification(notification_code)

        if response.status_code == 200:
            return HttpResponse("Notificação recebida com sucesso.")

    return HttpResponse("Notificação inválida.", status=400)