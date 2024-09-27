from typing import Union


def get_mask_card_number(number: Union[str]) -> Union[str]:
    """Function for masking cart number"""

    if number != "":
        if len(number) == 16:
            number_replace = "** ****"
            modify_number = f"{number[0:4]} {number[4:6]}{number_replace} {number[12:]}"
            return modify_number
        elif len(number) < 16:
            return "Ошибка ввода, мало символов"
        else:
            return "Ошибка ввода, много символов"
    return 'Вы ничего не ввели'


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Function for masking bank account"""
    if account_number != '':
        if len(account_number) == 20:
            return f"**{account_number[16:]}"
        elif len(account_number) < 20:
            return "Ошибка ввода, мало символов"
        else:
            return "Ошибка ввода, много символов"
    else:
        return "Вы ничего не ввели"
