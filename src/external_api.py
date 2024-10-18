import requests
import os
from dotenv import load_dotenv
from typing import Union


load_dotenv('.env')
api_key = os.getenv('API_KEY')


def return_cash(transactions: dict) -> Union[float, str]:
    url_1 = f"https://api.apilayer.com/exchangerates_data/latest?symbols=Rub&base={transactions['code']}"
    response = requests.get(url_1, headers=api_key)
    if transactions['code'] == 'USD':
        status_code = response.status_code
        if status_code == 200:
            try:
                respo = response.json()
                return respo.loads()["rates"]["RUB"] * transactions['code']
            except Exception:
                return f"Ошибка номер {status_code}"
    elif transactions['code'] == 'EUR':
        status_code = response.status_code
        if status_code == 200:
            try:
                respo = response.json()
                return respo.loads()["rates"]["RUB"] * transactions['code']
            except Exception:
                return f"Ошибка номер {status_code}"
    return transactions['amount']


