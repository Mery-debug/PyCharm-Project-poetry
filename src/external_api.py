import requests
import os
from dotenv import load_dotenv
from typing import Union


load_dotenv('.env')
api_key = os.getenv('API_KEY')


def return_cash(transactions: dict) -> Union[float, str]:
    transaction = transactions['operationAmount']['currency']['code']
    url_1 = f"https://api.apilayer.com/exchangerates_data/latest?symbols=Rub&base={transaction}"
    response = requests.get(url_1, headers=api_key)
    if transaction == 'USD':
        status_code = response.status_code
        if status_code == 200:
            try:
                respo = response.json()
                return respo.loads()["rates"]["RUB"] * transaction
            except Exception:
                return f"Ошибка номер {status_code}"
    elif transaction == 'EUR':
        status_code = response.status_code
        if status_code == 200:
            try:
                respo = response.json()
                return respo.loads()["rates"]["RUB"] * transaction
            except Exception:
                return f"Ошибка номер {status_code}"
    else:
        return transactions['operationAmount']['amount']


print(return_cash({'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount':
    {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'EUR'}},
    'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}))
