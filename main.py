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


def filter_by_currency(transactions: list[dict], val: Union[str] ="USD"):
    try:
        for i in range(0, len(transactions) + 1):
            try:
                if transactions[i]["operationAmount"]["currency"]["name"] == val:
                    yield transactions[i]
            except IndexError or StopIteration:
                print("Количество итераций закончилось")
    except KeyError:
        yield f"Вы пытаетесь обработать пустой словарь"


if __name__ == '__main__':
    o = filter_by_currency([{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount":
          {
              "amount": "9824.07",
              "currency":
              {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
            },
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount":
              {
                  "amount": "79114.93",
                  "currency":
                  {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
      }])
    print(next(o))
    print(next(o))
    print(next(o))
    # print(next(o))
    # print(next(o))
    # print(next(o))
    # print(next(o))
    # print(next(o))
    # print(next(o))
