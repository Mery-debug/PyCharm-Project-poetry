from typing import Any

from src.transaction_mod import find_description, transaction_search


def test_transaction_search_1(trial: list[dict], search_str: str, search_result: list[dict]) -> None:
    assert transaction_search(trial, search_str) == search_result


def test_find_description_1(trial: list[dict], description: list, counter_result: Any) -> None:
    assert find_description(trial, description) == counter_result
