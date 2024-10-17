import requests
import os
from dotenv import load_dotenv


def return_cash(transactions: dict) -> float:
    if transactions['code'] == 'USD' or transactions['code'] == 'EUR':
        load_dotenv()
        api_key = os.getenv('API_KEY')
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={'RUB'}&from={'USD'}&amount={transactions['amount']}"

    return transactions['amount']