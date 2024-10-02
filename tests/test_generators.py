from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

import pytest


def test_filter_by_currency(transaction: list[dict], val: str, exp: dict, exp_2: dict) -> None:
    n = filter_by_currency(transaction, val)
    assert next(n) == exp
    assert next(n) == exp_2


def test_transaction_descriptions(transaction: list[dict], expectati: str, expectation_2: str) -> None:
    i = transaction_descriptions(transaction)
    assert next(i) == expectati
    assert next(i) == expectation_2


@pytest.mark.parametrize("start, stop, expec", [(1, 6, "0000 0000 0000 0001")])
def test_card_number_generation(start, stop, expec):
    o = card_number_generator(start, stop)
    assert next(o) == expec



