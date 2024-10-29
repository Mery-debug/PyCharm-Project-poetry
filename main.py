from src.Users import number, status, ad_questions,
from src.utils import load_transactions
import os
from src.transaction_mod import transaction_search

def main():
    m = number()
    s = status()
    if 'json'.upper() in m:
        i = load_transactions(os.path.join(os.path.abspath(__file__), "/data/operations.json")
        if 'EXECUTED' in i:
            o = transaction_search(i, 'EXECUTED')






if __name__ == '__main__':

    print(number())
    print(status())










