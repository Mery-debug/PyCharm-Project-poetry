def filter_by_state(list_data: [list[dict]], state="EXECUTED") -> list:
    """Function for search dictionary with some 'state'"""
    list_new_data = []
    for lis in list_data:
        if lis["state"] == state:
            list_new_data.append(lis)
    return list_new_data


def sort_by_date(list_date: [list[dict]], sort=True) -> list:
    """Function for sorting date"""
    for lis in list_date:
        list_date.sort(key=lambda x: x["date"], reverse=sort)
    return list_date
