import csv
import pandas as df


def csv_reader(file_name: [str] = "../data/transactions.csv") -> list[dict]:
    transactions = []
    with open(file_name, encoding='utf-8') as csv_file:
        reader_dicts = csv.DictReader(csv_file, delimiter=';')
        for reader_dict in reader_dicts:
            transactions.append(reader_dict)
        return transactions


def xlsx_reader(file_name: [str] = "../data/transactions_excel.xlsx") -> list[dict]:
    transactions = []
    pd = df.read_excel(file_name)
    return pd







