from src.generators import filter_by_currency, transaction_descriptions

import pytest


def test_filter_by_currency(transaction: list[dict], val: str, exp: dict, exp_2: dict) -> None:
    n = filter_by_currency(transaction, val)
    assert next(n) == exp
    assert next(n) == exp_2


def test_transaction_descriptions(transaction: list[dict], expectati: str, expectation_2: str) -> None:
    i = transaction_descriptions(transaction)
    assert next(i) == expectati
    assert next(i) == expectation_2
