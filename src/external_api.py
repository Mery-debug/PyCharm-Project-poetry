import requests
import os
from dotenv import load_dotenv
from typing import Union


def return_cash(amount: Union[int, str], from_currency: str, to_currency: str) -> Union[float, str]:
    """Function take dict transaction and return amount in RUB only"""
    load_dotenv()
    # amount_tr = transactions['operationAmount']['amount']
    # transaction = transactions['operationAmount']['currency']['code']
    api_key = os.getenv("API_KEY")
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"
    headers = {
        "apikey": f"{api_key}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        if from_currency in ['EUR', 'USD']:
            return round(response.json()["result"], 2)
        else:
            return amount
    else:
        return f"Возможная причина {response.reason}"


# print(return_cash())


