import os
from typing import Any

from src.financialcsvxlsx import csv_reader, xlsx_reader
from src.processing import filter_by_state, sort_by_date
from src.utils import load_transactions
from src.widget import get_date, mask_account_card


def number() -> list[dict]:
    """Функция выбора файла"""
    modul = [{}]
    while True:
        user = input(
                '''Программа: Привет! Добро пожаловать в программу работы \nс банковскими транзакциями. 
                Выберите необходимый пункт меню:
                1. Получить информацию о транзакциях из JSON-файла
                2. Получить информацию о транзакциях из CSV-файла
                3. Получить информацию о транзакциях из XLSX-файла\n''').lower()
        if user == "1":
            print("Для обработки выбран JSON-файл.")
            modul = load_transactions(os.path.join(os.path.abspath(__file__), "../../data/operations.json"))
            break
        elif user == "2":
            print("Для обработки выбран CSV-файл.")
            modul = csv_reader(os.path.join(os.path.abspath(__file__), "../../data/transactions.csv"))
            break
        elif user == "3":
            print("Для обработки выбран XLSX-файл.")
            modul = xlsx_reader(os.path.join(os.path.abspath(__file__), "../../data/transactions_excel.xlsx"))
            break
        else:
            print("Такого варианта не предусмотренно, попробуйте выбрать еще раз.")
            continue
    return modul


def status(modul: list[dict]) -> list[dict]:
    """Функция выбора статуса"""
    a = 1
    while a > 0:
        user_2 = input("Выбери статус: EXECUTED, CANCELED, PENDING\n").upper()
        if user_2.upper() == "EXECUTED":
            print("Операции отфильтрованы по статусу: EXECUTED")
            a -= 1
            modul_transaction = filter_by_state(modul, state="EXECUTED")
            return modul_transaction
        elif user_2.upper() == "CANCELED":
            print("Операции отфильтрованы по статусу: CANCELED")
            a -= 1
            modul_transaction = filter_by_state(modul, state="CANCELED")
            return modul_transaction
        elif user_2.upper() == "PENDING":
            print("Операции отфильтрованы по статусу: PENDING")
            a -= 1
            modul_transaction = filter_by_state(modul, state="PENDING")
            return modul_transaction
        else:
            print(f"Статус операции {user_2} недоступен")
            a += 1
            continue


def ad_questions(modul_transaction: list[dict]) -> list[dict]:
    """Функция, задающая дополнительные вопросы"""
    final = [{}]
    user_3 = input("Отсортировать операции по дате? Да/Нет").lower()
    user_4 = input("Отсортировать по возрастанию или по убыванию?").lower()
    user_5 = input("Выводить только рублевые транзакции? Да/Нет").lower()
    user_6 = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет").lower()
    if user_3 == "да":
        if user_4 == "по возрастанию":
            sort_to_date = []
            sort = sort_by_date(modul_transaction, sorte=False)
            print(sort)
            for sor in sort:
                sort_to_date.append(sor)
                if user_5 == "да":
                    sort_to_rub = []
                    for sort in sort_to_date:
                        if sort["operationAmount"]["currency"]["code"] == "RUB":
                            sort_to_rub.append(sort)
                    if user_6 == "да":
                        final = sort_to_rub
                    elif user_6 == "нет":
                        final = sort_to_rub
                elif user_5 == "нет":
                    sort_to_rub = sort_to_date
                    if user_6 == "да":
                        final = sort_to_rub
                    elif user_6 == "нет":
                        final = sort_to_rub
        elif user_4 == "по убыванию":
            sort_to_date = []
            sort = sort_by_date(modul_transaction, sorte=True)
            for sor in sort:
                sort_to_date.append(sor)
                if user_5 == "да":
                    sort_to_rub = []
                    for sort in sort_to_date:
                        if sort["operationAmount"]["currency"]["code"] == "RUB":
                            sort_to_rub.append(sort)
                            if user_6 == "да":
                                final = sort_to_rub
                            elif user_6 == "нет":
                                final = sort_to_rub
                elif user_5 == "нет":
                    sort_to_rub = sort_to_date
                    if user_6 == "да":
                        final = sort_to_rub
                    elif user_6 == "нет":
                        final = sort_to_rub
    elif user_3 == "нет":
        if user_5 == "да":
            sort_to_rub = modul_transaction
            for sor in sort_to_rub:
                if sor["operationAmount"]["currency"]["code"] == "RUB":
                    sort_to_rub.append(sor)
                    if user_6 == "да":
                        final = sort_to_rub
                    elif user_6 == "нет":
                        final = sort_to_rub
        elif user_5 == "нет":
            sort_to_rub = modul_transaction
            if user_6 == "да":
                final = sort_to_rub
            elif user_6 == "нет":
                final = sort_to_rub
    return final
