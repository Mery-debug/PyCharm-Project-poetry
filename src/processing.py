from typing import Union


def filter_by_state(list_data: [list], state="EXECUTED") -> list:
    """Function for search dictionary with some 'state'"""
    list_new_data = []
    for lis in list_data:
        if lis["state"] == state:
            list_new_data.append(lis)
    return list_new_data


