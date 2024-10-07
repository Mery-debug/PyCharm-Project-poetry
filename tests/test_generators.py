import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transaction_11: list[dict], val: str, exp: dict, exp_2: dict, exp_3: str) -> None:
    n = filter_by_currency(transaction_11, val)
    assert next(n) == exp
    assert next(n) == exp_2
    assert next(n) == exp_3


def test_filter_by_currency_3(transaction_11: list[dict], val_2: str, exp: dict, exp_2: dict, exp_3: str) -> None:
    n = filter_by_currency(transaction_11, val_2)
    assert next(n) == "Нет информации по операциям с этой валютой"


def test_transaction_descriptions(transaction_1: list[dict], expectati: str, expectation_2: str) -> None:
    i_1 = transaction_descriptions(transaction_1)
    assert next(i_1) == expectati
    assert next(i_1) == expectation_2


def test_transaction_descriptions_2(lst_null: list) -> None:
    ii = transaction_descriptions(lst_null)
    assert next(ii) == "Вы пытаетесь обработать пустой словарь"


@pytest.mark.parametrize("start, stop, expec", [(1, 6, "0000 0000 0000 0001")])
def test_card_number_generation(start: int, stop: int, expec: str) -> None:
    o = card_number_generator(start, stop)
    assert next(o) == expec


def test_card_number_generation_2(start_min: int, stop_max: int) -> None:
    o_2 = card_number_generator(start_min, stop_max)
    assert next(o_2) == "Ошибка ввода, недопустимый диапазон"
