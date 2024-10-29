from src.masks import get_mask_account, get_mask_card_number
from typing import Union, Any

from src.processing import sort_by_date


def number() -> Union[str, int]:
    """Функция выбора файла"""
    n = 0
    while True:
        user = input('''Программа: Привет! Добро пожаловать в программу работы
            с банковскими транзакциями. 
            Выберите необходимый пункт меню:
            1. Получить информацию о транзакциях из JSON-файла
            2. Получить информацию о транзакциях из CSV-файла
            3. Получить информацию о транзакциях из XLSX-файла''')
        if user == '1':
            n = 'Для обработки выбран JSON-файл.'
            break
        elif user == '2':
            n = 'Для обработки выбран CSV-файл.'
            break
        elif user == '3':
            n = 'Для обработки выбран XLSX-файл.'
            break
        else:
            print('Такого варианта не предусмотренно, попробуйте выбрать еще раз.')
            continue
    return n


def status() -> str:
    """Функция выбора статуса"""
    a = 1
    while a > 0:
        user_2 = input('Выбери статус: EXECUTED, CANCELED, PENDING')
        if user_2.upper() == 'EXECUTED':
            s = 'Операции отфильтрованы по статусу: EXECUTED'
            a -= 1
        elif user_2.upper() == 'CANCELED':
            s = f'Операции отфильтрованы по статусу: CANCELED'
            a -= 1
        elif user_2.upper() == 'PENDING':
            s = f'Операции отфильтрованы по статусу: PENDING'
            a -= 1
        else:
            print(f'Статус операции {user_2} недоступен')
            a += 1
            continue
        return s


def ad_questions() -> list:
    """Функция, задающая дополнительные вопросы"""
    a = 0
    b = 0
    c = 0
    d = 0
    user_3 = input('Отсортировать операции по дате? Да/Нет')
    user_4 = input('Отсортировать по возрастанию или по убыванию?')
    user_5 = input('Выводить только рублевые транзакции? Да/Нет')
    user_6 = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет')
    if user_3.lower() == 'да':
        a = 1
    elif user_3.lower() == 'нет':
        a = 2
    if user_4.lower() == 'по возрастанию':
        b = 1
    elif user_4.lower() == 'по убыванию':
        b = 2
    if user_5.lower() == 'да':
        c = 1
    elif user_5.lower() == 'нет':
        c = 2
    if user_6.lower() == 'да':
        d = 1
        user_7 = input('Напишите слово для сортировки: ')
        return [a, b, c, d, user_7]
    elif user_6.lower() == 'нет':
        d = 2
    return [a, b, c, d]


def choice_of_sort(modul_transaction: list[dict], sorte=True) -> list[dict]:
    sort_to_date = []
    for modul_tr in modul_transaction:
        sort = sort_by_date(modul_tr['date'], sorte)
        for sor in sort:
            sort_to_date.append(sor)
    return sort_to_date


def choice_of_currency(sort_to_date: list[dict], currency: str) -> list[dict]:
    sort_to_rub = []
    for sort in sort_to_date:
        if sort['operationAmount']['currency']['code'] == currency:
            sort_to_rub.append(sort)
    return sort_to_rub

