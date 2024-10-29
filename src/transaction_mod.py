import re
from collections import Counter


def transaction_search(transactions: list[dict], search_str: str) -> list[dict]:
    final_lst = []
    for transaction in transactions:
        re.findall(search_str, transaction.get('description'))
        final_lst.append(transaction)
    return final_lst


def find_description(transactions: list[dict], descriptions: [list]) -> dict:
    lst = []
    for transaction in transactions:
        for description in descriptions:
            if description == transaction["description"]:
                lst.append(transaction["description"])
    return Counter(lst)
