# from src.processing import filter_by_state, sort_by_date
# from src.widget import get_date
from typing import Union

#
# print(filter_by_state([{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#                     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#                     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
#
# print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#                     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#                     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#                     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
#
# print(get_date('2024-03-11T02:26:18.671407'))


def transaction_descriptions(transactions: list[dict]) -> str:
    try:
        result = list((transaction["description"] for transaction in transactions if transaction != [{}]))
        for i in range(len(result)):
            yield result[i]
            i += 1
    except KeyError:
        yield f"Вы пытаетесь обработать пустой словарь"

if __name__ == '__main__':
    o = transaction_descriptions([{}])
    print(next(o))
    print(next(o))
    # print(next(o))
    # print(next(o))
    # print(next(o))
    # print(next(o))
    # print(next(o))
    # print(next(o))
    # print(next(o))
