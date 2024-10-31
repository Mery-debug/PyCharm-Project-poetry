from typing import Any

from src.Users import number, status, ad_questions
from src.widget import get_date, mask_account_card


def main() -> Any:
    """Главная функция проекта"""
    modul = number()
    print(modul)
    modul_transaction = status(modul)
    print(modul_transaction)
    final = ad_questions(modul_transaction)
    if not final:
        return 'Не найдено ни одной транзакции, подходящей под ваши условия фильтрации'
    else:
        print('Распечатываю итоговый список транзакций...')
        print(f'Всего банковских операций в выборке: {len(final)}')
        for fina in final:
            print(f'{get_date(fina.get("date"))} {fina.get("description")}')
            if fina.get("description") == "Открытие вклада":
                print(f'{mask_account_card(fina.get("to"))}')
                print(f'Сумма: {fina.get("operationAmount").get("amount")} {fina.get("operationAmount").get("currency").get("code")}\n')
            else:
                print(f'{mask_account_card(fina.get("from"))} -> {mask_account_card(fina.get("to"))}')
                print(f'Сумма: {fina.get("operationAmount").get("amount")} {fina.get("operationAmount").get("currency").get("code")}\n')
        return "конец"


if __name__ == '__main__':
    print(main())
