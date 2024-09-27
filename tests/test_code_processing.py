from typing import Union

from src.processing import sort_by_date


def test_sort_by_date(list_date: Union[list[dict[str, int]]], expectation: Union[list[dict]]) -> None:
    assert sort_by_date(list_date) == expectation
