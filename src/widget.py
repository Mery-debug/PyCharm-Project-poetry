from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: [str]) -> str:
    """Function for masking cart or bank account"""
    if data == '':
        return "Ошибка ввода, мало символов"
    elif ' ' not in data:
        return "Не верный формат ввода"
    else:
        if "Счет" in data:
            return f"{data[0:-20]}{get_mask_account(data[-20:])}"
        else:
            return f"{data[0:-16]}{get_mask_card_number(data[-16:])}"


def get_date(date: [str]) -> str:
    """Function for restructuring date"""
    if int(date[5:7]) > 12:
        return "Некорректная дата"
    elif int(date[8:10]) > 31:
        return "Некорректная дата"
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
