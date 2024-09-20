from typing import Union


def get_mask_card_number(number: Union[str]) -> Union[str]:
    """Функция маскирующая номер карты принятый от пользователя"""

    if len(number) == 16:
        number_replace = "** ****"
        modify_number = f"{number[0:4]} {number[4:7]}{number_replace} {number[10:]}"
        return modify_number
    elif len(number) < 16:
        return "Ошибка ввода, мало символов"
    else:
        return "Ошибка ввода, много символов"


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Функция маскирования номера счета пользователя"""
    if len(account_number) == 20:
        return f"**{account_number[16:]}"
    elif len(account_number) < 20:
        return "Ошибка ввода, мало символов"
    else:
        return "Ошибка ввода, много символов"


def