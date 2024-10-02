from typing import Union


def filter_by_currency(transactions: list[dict], val: Union[str] ="USD") -> dict:
    for i in range(0, len(transactions) + 1):
        if transactions[i]["operationAmount"]["currency"]["name"] == val:
            yield transactions[i]

