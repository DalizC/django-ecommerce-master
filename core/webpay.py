import requests
import json
import random
from django.conf import settings
from core.models import *
from django.views.decorators.csrf import csrf_protect


def create_transaction():
    buy_order = "ordenCompra12345678"
    session_id = "sesion1234557545"
    amount = 10000
    return_url = "http://localhost:8000/webpay_response"

    endpoint = "https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions"
    payload = {
        "buy_order": buy_order,
        "session_id": session_id,
        "amount": amount,
        "return_url": return_url,
    }
    headers = {
        'Content-Type': 'application/json',
        'Tbk-Api-Key-Id': '597055555532',
        'Tbk-Api-Key-Secret': '579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C'
    }

    response_ = requests.post(endpoint, json=payload, headers=headers)
    response = json.loads(response_.text)
    return response


@csrf_protect
def validate_transaction(token):
    # print(token.GET)
    str_ = json.dumps(token.GET)
    dic_ = json.loads(str_)
    token_string = '?token_ws=' + dic_['token_ws']
    # print(token_string)
    endpoint = f"{'https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions'}/{token_string}"
    #endpoint = "https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions/?token_ws=01ab2fd143dbd0d48cc6842a52090a6acf22fd6afb88ac1205f0e27ce089b447"
    # print(endpoint)
    headers = {
        'Content-Type': 'application/json',
        'Tbk-Api-Key-Id': '597055555532',
        'Tbk-Api-Key-Secret': '579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C'
    }
    response_ = requests.put(endpoint, headers=headers)
    response = json.loads(response_.text)
    # print(response)
    return response
