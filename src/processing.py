
def filter_by_state(list_data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Function for search dictionary with some 'state'"""
    list_new_data = []
    for lis in list_data:
        if lis.get('state') == state:
            list_new_data.append(lis)
    return list_new_data


def sort_by_date(list_date: list[dict], sorte: bool = True) -> list[dict]:
    """Function for sorting date"""
    list_date.sort(key=lambda x: x.get("date"), reverse=sorte)
    return list_date
