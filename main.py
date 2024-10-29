from src.Users import number, status, ad_questions
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
            if modul_ad_question[0] == 1:
                for modul_tr in modul_transaction:
                    sort_to_date.append(get_date(modul_tr['date']))
            if modul_ad_question[1] == 1:
                sorte = sort_by_date(sort_to_date)
            else:
                sorted = sort_by_date(sort_to_date, sort=False)
            if modul_ad_question[2] == 1:
                for modul_tr in modul_transaction:
                    return_rub.append(return_cash(modul_tr['amount'], modul_tr['operationAmount']['currency']['code']['RUB']))
            if modul_ad_question[3] == 1:
                search = transaction_search(modul_transaction, modul_ad_question[4])
            return f'{sort_to_date}'









if __name__ == '__main__':
    print(main())










