from src.Users import number, status, ad_questions,
from src.utils import load_transactions
import os
from src.transaction_mod import transaction_search
from src.processing import sort_by_date, filter_by_state
from src.widget import get_date
from src.external_api import return_cash

def main():
    sort_to_date = []
    return_rub = []
    modul_number = number()
    if 'json'.upper() in modul_number:
        modul_json = load_transactions(os.path.join(os.path.abspath(__file__), "/data/operations.json"))
        modul_status = status()
        if 'EXECUTED' in modul_status:
            modul_transaction = filter_by_state(modul_json, 'EXECUTED')
            modul_ad_question = ad_questions()
            for modul in modul_ad_question:
                if modul[0] == 1:
                    for modul_tr in modul_transaction:
                        sort_to_date.append(get_date(modul_tr['date']))
                        print(sort_to_date)
                if modul[1] == 1:
                    sorte = sort_by_date(sort_to_date)
                    print(sorte)
                else:
                    sorted = sort_by_date(sort_to_date, sort=False)
                    print(sorted)
                if modul[2] == 1:
                    for modul_tr in modul_transaction:
                        return_rub.append(return_cash(modul_tr['amount'], modul_tr['operationAmount']['currency']['code']['RUB'])
                        print(return_rub)
                if modul[3] == 1:
                    search = transaction_search(modul_transaction, modul[4])
                    print(search)










if __name__ == '__main__':

    print(number())
    print(status())










