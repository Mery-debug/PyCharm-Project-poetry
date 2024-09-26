from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: Union[str]) -> str:
    """Function for masking cart or bank account"""

    if "Счет" in data:
        return f"{data[0:-20]} {get_mask_account(data[-20:])}"
    else:
        return f"{data[0:-16]} {get_mask_card_number(data[-16:])}"


def get_date(date: Union[str]) -> str:
    """Function for restructuring date"""

    return f"{date[8:10]}.{date[5:7]}.{date[0:5]}"
