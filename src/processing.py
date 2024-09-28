from typing import Union, Any


def filter_by_state(list_data: Union[list[dict[str, int]]], state: Union[str] = "EXECUTED") -> list[dict]:
    """Function for search dictionary with some 'state'"""
    list_new_data = []
    for lis in list_data:
        if lis["state"] == state:
            list_new_data.append(lis)
    return list_new_data


def sort_by_date(list_date: Union[list[dict]], sort: Union[bool] = True) -> Any[list[dict], str]:
    """Function for sorting date"""
    for lis in list_date:
        if len(lis["date"]) != 26:
            return 'Некорректное значение'
        else:
            list_date.sort(key=lambda x: x["date"], reverse=sort)
            return list_date
