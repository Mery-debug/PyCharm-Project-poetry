import requests
import os
from dotenv import load_dotenv
from typing import Union


def return_cash(transactions: dict) -> Union[float, str]:
    """Function take dict transaction and return amount in RUB only"""
    load_dotenv()
    amount_tr = transactions['operationAmount']['amount']
    transaction = transactions['operationAmount']['currency']['code']
    api_key = os.getenv("API_KEY")
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={transaction}&amount={amount_tr}"
    payload = {}
    headers = {
        "apikey": f"{api_key}"
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        if transaction in ['EUR', 'USD']:
            return round(response.json()["result"], 2)
        else:
            return amount_tr
    else:
        return f"Возможная причина {response.reason}"


# print(return_cash({'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'EUR'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}))



