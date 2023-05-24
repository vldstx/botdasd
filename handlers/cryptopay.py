from datetime import datetime, timedelta
from aiogram import types, Dispatcher
from other.states import *
from handlers.callbackhandler import *
from other.keyboards import *
import requests
import time



current_invoice_id = None
def create_invoice(api_token, asset, amount, description):
    url = "https://pay.crypt.bot/api/createInvoice"
    headers = {"Crypto-Pay-API-Token": api_token}
    payload = {
        "asset": asset,
        "amount": amount,
        "description": description,
        "allow_anonymous": True
    }
    payload_updated = dict(payload, allow_anonymous=False)
    response = requests.post(url, headers=headers, json=payload_updated)
    data = response.json()
    if data.get("ok"):
        invoice_id = data["result"]["invoice_id"]
        pay_url = data["result"]["pay_url"]
        return invoice_id, pay_url
    else:
        return None, None







api_token = ""
