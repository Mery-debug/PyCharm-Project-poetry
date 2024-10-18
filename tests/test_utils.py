from unittest.mock import Mock
from typing import Any
from src.utils import load_transactions
import json



def test_load_transactions(final_path: str) -> None:
    """Тест с mock для utils, если файл не существует"""
    assert load_transactions(final_path) == []


def test_load_trans(final_p: str) -> None:
    """Тест при правильной работе функции"""
    with open(final_p, 'r', encoding='utf-8', errors='ignore') as json_file:
        data = json.load(json_file)
    assert load_transactions(final_p) == data


def test_load() -> None:
