from typing import Union

from src.processing import filter_by_state, sort_by_date


def test_sort_by_date(list_date: Union[list[dict]], expectation: Union[list[dict]]) -> None:
    """Function for testing sort_by_date"""
    assert sort_by_date(list_date) == expectation


def test_filter_by_state(list_dat: Union[list[dict]], stat: Union[str], result: Union[list[dict]]) -> None:
    assert filter_by_state(list_dat, stat) == result


def test_fil_by_st(list_dat: Union[list[dict]], stat_2: Union[str], result_2: Union[list[dict]]) -> None:
    assert filter_by_state(list_dat, stat_2) == result_2
