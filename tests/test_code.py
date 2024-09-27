from src.masks import get_mask_card_number, get_mask_account
import pytest


def test_get_mask_card_number():
    assert get_mask_card_number('0000000000000000') == '0000 00** **** 0000'
    assert get_mask_card_number('') == 'Вы ничего не ввели'
    assert get_mask_card_number('000000000000') == 'Ошибка ввода, мало символов'
    assert get_mask_card_number('12345678912345678900') == 'Ошибка ввода, много символов'
