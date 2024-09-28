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
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def expectation() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def list_date_2() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:3"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-0912T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018--14T08:21:33.419441"},
    ]
