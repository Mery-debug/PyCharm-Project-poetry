from typing import Union

from src.processing import sort_by_date


def test_sort_by_date(list_date: Union[list[dict]], expectation: Union[list[dict]]) -> None:
    """Function for testing sort_by_date"""
    assert sort_by_date(list_date) == expectation


def test_sort_by_date_2(list_date_2: Union[list[dict]], expectation: Union[list[dict]]) -> None:
    assert sort_by_date(list_date_2) == 'Некорректное значение'
