from src.generators import filter_by_currency

import pytest


def test_filter_by_currency(transaction: list[dict], val: str, exp: dict, exp_2: dict) -> None:
    n = filter_by_currency(transaction, val)
    assert next(n) == exp
    assert next(n) == exp_2


