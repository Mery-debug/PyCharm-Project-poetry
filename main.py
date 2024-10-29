from src.Users import number, status, ad_questions, choice_of_sort, choice_of_currency
from src.transaction_mod import transaction_search, find_description
from src.utils import load_transactions
import os
from src.processing import filter_by_state
from src.widget import get_date, mask_account_card


def main():
    sort_to_date = []
    sort_to_rub = []
    modul_number = number()
    if 'json'.upper() in modul_number:
        modul_json = load_transactions(os.path.join(os.path.abspath(__file__), "/data/operations.json"))
        modul_status = status()
        if 'EXECUTED' in modul_status:
            modul_transaction = filter_by_state(modul_json, 'EXECUTED')
            modul_ad_question = ad_questions()
            if modul_ad_question[0] == 1 and modul_ad_question[1] == 1:
                choice = choice_of_sort(modul_transaction)
                if modul_ad_question[2] == 1:
                    lst_currency = choice_of_currency(choice, 'RUB')
                    for lst in lst_currency:
                        if modul_ad_question[3] == 1:
                            transaction = transaction_search(lst_currency, modul_ad_question[4])
                        elif modul_ad_question[3] == 2:
                            print('Распечатываю итоговый список транзакций...')
                            print(f'Всего банковских операций в выборке: {len(lst_currency)}')
                            return f'{get_date(lst["date"])} {lst["description"]} \n {mask_account_card(lst["to"])}\nСумма{lst["amount"]}'
                elif modul_ad_question[2] == 2:
                    lst_currency = choice
            elif modul_ad_question[0] == 1 and modul_ad_question[1] == 2:
                choice = choice_of_sort(modul_transaction, sorte=False)
                if modul_ad_question[2] == 1:
                    lst_currency = choice_of_currency(choice, 'RUB')
                elif modul_ad_question[2] == 2:
                    lst_currency = choice

        elif 'CANCELED' in modul_status:
            pass
    elif 'CSV'.upper() in modul_number:
        pass
    elif 'XLSX'.upper() in modul_number:
        pass






if __name__ == '__main__':
    print(main())










