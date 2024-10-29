from src.Users import number, status, ad_questions,
from src.utils import load_transactions
import os
from src.transaction_mod import transaction_search
from src.processing import sort_by_date, filter_by_state


def main():
    modul_number = number()
    if 'json'.upper() in modul_number:
        modul_json = load_transactions(os.path.join(os.path.abspath(__file__), "/data/operations.json"))
        modul_status = status()
        if 'EXECUTED' in modul_status:
            modul_transaction = filter_by_state(modul_json, 'EXECUTED')
            modul_ad_question = ad_questions()
            for modul in modul_ad_question:
                if a == 1:







if __name__ == '__main__':

    print(number())
    print(status())










