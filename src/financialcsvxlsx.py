import csv
import pandas as pd


def csv_reader(file_name: [str] = "../data/transactions.csv") -> list[dict]:
    """function, which read csv files with lib csv"""
    transactions = []
    with open(file_name, encoding='utf-8') as csv_file:
        reader_dicts = csv.DictReader(csv_file, delimiter=';')
        for reader_dict in reader_dicts:
            transactions.append(reader_dict)
        return transactions


def xlsx_reader(file_name: [str] = "../data/transactions_excel.xlsx") -> list[dict]:
    """function which read xlsx files with lib pandas"""
    transactions = []
    transaction = pd.read_excel(file_name)
    some = pd.columns.todict()
    for index, row in transaction.iterrows():
        dct = some[i]: row[some[i]] for i in range()
        transactions.append({




print(xlsx_reader("../data/transactions_excel.xlsx"))
# transactions_excel.xlsx






def reader_file_transaction_excel(excel_path):
    """Функция принимает путь до excel-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        transaction_df = pd.read_excel(excel_path)
        transaction_list = []
        for index, row in transaction_df.iterrows():
            transaction_list.append(
                {
                    "id": str(row["id"]),
                    "state": row["state"],
                    "date": row["date"],
                    "operationAmount": {
                        "amount": str(row["amount"]),
                        "currency": {
                            "name": row["currency_name"],
                            "code": row["currency_code"],
                        },
                    },
                    "description": row["description"],
                    "from": row["from"],
                    "to": row["to"],
                }
            )
    except Exception as e:
        print(f"Error reading Excel: {e}")
        return []
    return transaction_list


