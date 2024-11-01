import csv
from typing import Any, Collection

import pandas as pd

# file_name = (os.path.abspath(__name__), '../../data/transactions.csv')


def csv_reader(file_name: str = "../data/transactions.csv") -> list[dict[str, dict[str, Collection[str]] | str | Any]]:
    """function, which read csv files with lib csv"""
    transactions = []
    with open(file_name, encoding="utf-8") as csv_file:
        reader_dicts = csv.DictReader(csv_file, delimiter=";")
        for row in reader_dicts:
            transactions.append(
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
        return transactions


def xlsx_reader(file_name: str = "../data/transactions_excel.xlsx") -> list[dict[str, Any]]:
    """function which read xlsx files with lib pandas"""
    transactions = []
    transaction = pd.read_excel(file_name)
    for index, row in transaction.iterrows():
        transactions.append(
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
    return transactions


# print(xlsx_reader("../data/transactions_excel.xlsx"))
# print(csv_reader("../data/transactions.csv"))
