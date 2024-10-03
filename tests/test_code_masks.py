from typing import Union

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "number, expect",
    [
        ("1234567891234567", "1234 56** **** 4567"),
        ("0987654321098765", "0987 65** **** 8765"),
        ("6574837462530293", "6574 83** **** 0293"),
    ],
)
def test_get_mask_card_number_1(number: Union[str], expect: Union[str]) -> None:
    """Function for testing 'good' numbers"""
    assert get_mask_card_number(number) == expect


def test_get_mask_card_number_2(lst: Union[str], short: Union[str], long: Union[str]) -> None:
    """Function for testing line errors"""
    assert get_mask_card_number(lst) == "Вы ничего не ввели"

    assert get_mask_card_number(short) == "Ошибка ввода, мало символов"

    assert get_mask_card_number(long) == "Ошибка ввода, много символов"


@pytest.mark.parametrize(
    "account_number, expect",
    [("12345678901234567890", "**7890"),
     ("12345123451234512345", "**2345"),
     ("12345678900987654321", "**4321")],
                        )
def test_mask_account_number(account_number: Union[str], expect: Union[str]) -> None:
    """Function for testing 'good' account_numbers"""
    assert get_mask_account(account_number) == expect


def test_mask_account_number_2(lst: Union[str], short: Union[str], long: Union[str]) -> None:
    """Function for testing line errors"""
    assert get_mask_account(lst) == "Вы ничего не ввели"

    assert get_mask_account(short) == "Ошибка ввода, мало символов"

    assert get_mask_account(long) == "Ошибка ввода, много символов"
