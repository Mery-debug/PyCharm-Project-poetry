from typing import Union

import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "data, expect",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro1596837868705199", "Не верный формат ввода"),
        ("", "Ошибка ввода, мало символов"),
    ],
)
def test_mask_account_card(data: Union[str], expect: Union[str]) -> None:
    """Function for testing mask_account_card"""
    assert mask_account_card(data) == expect


@pytest.mark.parametrize(
    "date, result",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2004-11-01T02:26:18.671407", "01.11.2004"),
        ("2022-05-30T02:26:18.671407", "30.05.2022"),
        ("2024-03-40T02:26:18.671407", "Некорректная дата"),
        ("2024-20-10T02:26:18.671407", "Некорректная дата"),
        ("2024-20-10T02:26:18.671", "Некорректная дата"),
        (" ", "Некорректная дата"),
        ("", "Некорректная дата"),
    ],
)
def test_get_date(date: Union[str], result: Union[str]) -> None:
    """Function for testing get_date"""
    assert get_date(date) == result
