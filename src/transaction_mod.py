import re
from collections import Counter
from typing import Any


def transaction_search(transactions: list[dict], search_str: str) -> list[dict]:
    final_lst = []
    for transaction in transactions:
        re.findall(search_str, transaction.get("description"))
        final_lst.append(transaction)
    return final_lst


def find_description(transactions: list[dict], descriptions: [list]) -> Any:
    lst = []
    count = 0
    for transaction in transactions:
        for description in descriptions:
            if description == transaction["description"]:
                lst.append(transaction["description"])
                count = Counter(lst)
    return count
