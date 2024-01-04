import requests
import xmltodict
from dateutil.parser import parse
from checkouts.config import (
    PAGSEGURO_EMAIL,
    PAGSEGURO_TOKEN,
    CHECKOUT_URL,
    PAYMENT_URL,
    NOTIFICATION_URL,
    TRANSACTION_URL,
    SESSION_URL,
)
import logging
from dateutil.parser import parse
from django.utils import timezone
from decouple import config

from checkouts.forms import PagSeguroItemForm

from checkouts.signals import (
    checkout_realizado,
    checkout_realizado_com_erro,
    checkout_realizado_com_sucesso,
    notificacao_recebida,
    NOTIFICATION_STATUS,
)

logger = logging.getLogger(__name__)

class PagSeguroApiTransparent(object):
    def __init__(self, checkout_url=None, session_url=None, redirect_url=None, notification_url=None, transaction_url=None, pagseguro_email=None, pagseguro_token=None, currency="BRL", **kwargs,):
        self.checkout_url = CHECKOUT_URL
        self.session_url = SESSION_URL
        self.redirect_url = PAYMENT_URL
        self.notification_url = NOTIFICATION_URL
        self.transaction_url = TRANSACTION_URL
        self.pagseguro_email = config('PAGSEGURO_EMAIL')
        self.pagseguro_token = config('PAGSEGURO_TOKEN')
        self.currency = currency
        self.base_params = {
            "email": self.pagseguro_email,
            "token": self.pagseguro_token,
            "currency": self.currency,
        }
        self.base_params.update(kwargs)
        self.params = {}

    def set_sender_hash(self, hash_code):
        self.params["senderHash"] = hash_code

    def set_receiver_email(self, email):
        self.params["receiverEmail"] = email

    def set_payment_method(self, method):
        self.params["paymentMethod"] = method

    def set_extra_amount(self, amount):
        self.params["extraAmount"] = amount

    def set_notification_url(self, url):
        self.params["notificationURL"] = url

    def set_bank_name(self, name):
        self.params["bankName"] = name

    def set_itemCount(self, itemCount=1):
        self.params["itemCount"] = itemCount

    def set_item(self, id, description, amount, quantity, shipping_cost=None, weight=None):
        self.params["itemId1"] = id
        self.params["itemDescription1"] = description
        self.params["itemAmount1"] = amount
        self.params["itemQuantity1"] = quantity
        self.params["itemShippingCost1"] = shipping_cost
        self.params["itemWeight1"] = weight

    def set_sender(self, name, area_code, phone, email, cpf, cnpj=None, born_date=None):
        self.params["senderName"] = name
        self.params["senderAreaCode"] = area_code
        self.params["senderPhone"] = phone
        self.params["senderEmail"] = email
        self.params["senderCPF"] = cpf
        self.params["senderCNPJ"] = cnpj
        self.params["senderBornDate"] = born_date

    def set_shipping(self, street, number, complement, district, postal_code, city, state, country, cost=None, shipping_type=None,):
        self.params["shippingAddressStreet"] = street
        self.params["shippingAddressNumber"] = number
        self.params["shippingAddressComplement"] = complement
        self.params["shippingAddressDistrict"] = district
        self.params["shippingAddressPostalCode"] = postal_code
        self.params["shippingAddressCity"] = city
        self.params["shippingAddressState"] = state
        self.params["shippingAddressCountry"] = country
        self.params["shippingCost"] = cost
        self.params["shippingType"] = shipping_type

    def build_params(self):
        self.params.update(self.base_params)

    def checkout(self):
        self.build_params()
        headers = {"content-type": "application/x-www-form-urlencoded; charset=UTF-8"}
        response = requests.post(self.transaction_url, self.params, headers=headers)

        if response.status_code == 200:
            root = xmltodict.parse(response.text)
            transaction = root["transaction"]
            data = {
                "transaction": transaction,
                "status_code": response.status_code,
                "success": True,
                "date": parse(transaction["date"]),
                "code": transaction["code"],
                "paymentLink": transaction["paymentLink"],
            }
            checkout_realizado_com_sucesso.send(sender=self, data=data)
        else:
            data = {
                "status_code": response.status_code,
                "message": response.text,
                "success": False,
                "date": timezone.now(),
            }
            checkout_realizado_com_erro.send(sender=self, data=data)

        checkout_realizado.send(sender=self, data=data)

        logger.debug("operation=transparent_api_checkout, " "data={!r}".format(data))
        return data

    def get_session_id(self):
        response = requests.post(
            self.session_url,
            params={"email": self.base_params["email"], "token": self.base_params["token"]},
        )

        if response.status_code == 200:
            root = xmltodict.parse(response.text)
            session_id = root["session"]["id"]
            data = {
                "session_id": session_id,
                "status_code": response.status_code,
                "success": True,
                "date": timezone.now(),
            }
        else:
            data = {
                "status_code": response.status_code,
                "message": response.text,
                "success": False,
                "date": timezone.now(),
            }

        logger.debug("operation=transparent_api_get_session_id, " "data={!r}".format(data))
        return data

    def get_notification(self, notification_id):
        response = requests.get(
            self.notification_url + "/{}".format(notification_id),
            params={"email": self.base_params["email"], "token": self.base_params["token"]},
        )

        if response.status_code == 200:
            root = xmltodict.parse(response.text)
            transaction = root["transaction"]
            notificacao_recebida.send(sender=self, transaction=transaction)

            status = transaction["status"]
            if status in NOTIFICATION_STATUS:
                signal = NOTIFICATION_STATUS[status]
                signal.send(sender=self, transaction=transaction)

        logger.debug(
            "operation=api_get_notification, "
            "notification_id={}, "
            "response_body={}, "
            "response_status={}".format(notification_id, response.text, response.status_code)
        )
        return response

    def get_transaction(self, transaction_id):
        response = requests.get(
            self.transaction_url + "/{}".format(transaction_id),
            params={"email": self.base_params["email"], "token": self.base_params["token"]},
        )

        if response.status_code == 200:
            root = xmltodict.parse(response.text)
            transaction = root["transaction"]

            data = {
                "transaction": transaction,
                "status_code": response.status_code,
                "success": True,
                "date": timezone.now(),
            }
        else:
            data = {
                "status_code": response.status_code,
                "message": response.text,
                "success": False,
                "date": timezone.now(),
            }

        logger.debug(
            "operation=api_get_transaction, "
            "transaction_id={}, "
            "data={!r}, "
            "response_status={}".format(transaction_id, data, response.status_code)
        )
        return data