import pytest


@pytest.fixture
def lst() -> str:
    return ""


@pytest.fixture
def short() -> str:
    return "123456789"


@pytest.fixture
def long() -> str:
    return "123456789123456789000000"


@pytest.fixture
def list_date() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
    ]


@pytest.fixture
def expectation() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
    ]


@pytest.fixture
def list_date_2() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:3"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-0912T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018--14T08:21:33.419441"},
    ]


@pytest.fixture
def list_dat() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def result() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def result_2() -> list[dict]:
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def stat() -> str:
    return "EXECUTED"


@pytest.fixture
def stat_2() -> str:
    return "CANCELED"


@pytest.fixture
def transaction_1() -> list[dict]:
    return [{
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
      }]


@pytest.fixture
def transaction_11() -> list[dict]:
    return [{
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
      }, {}]


@pytest.fixture
def exp_3() -> str:
    """Ожидаемое значение при попытке обработать пустой словарь"""
    return "Вы пытаетесь обработать пустой словарь"


@pytest.fixture
def val() -> str:
    """Необязательный параметр state, краткое название валюты в которой производится операция"""
    return "USD"


@pytest.fixture
def val_2() -> str:
    """ Необязательный параметр state, краткое название валюты в которой производится операция"""
    return "EUR"


@pytest.fixture
def exp() -> dict:
    """Ожидаемое значение после выполнения функции в виде словаря"""
    return {
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
            }


@pytest.fixture
def exp_2() -> dict:
    """Ожидаемое значение после выполнения функции в виде словаря"""
    return {
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
            }


@pytest.fixture
def expectati() -> str:

    return "Перевод организации"


@pytest.fixture
def expectation_2() -> str:
    return "Перевод со счета на счет"


@pytest.fixture
def expec_2() -> str:
    return "0000 0000 0000 0002"


@pytest.fixture
def start() -> int:
    return 2


@pytest.fixture
def stop() -> int:
    return 3


@pytest.fixture
def lst_null() -> list[dict]:
    return [{}]

@pytest.fixture
def start_min() -> int:
    return 0


@pytest.fixture
def stop_max() -> int:
    return 10000000000000000


