from src.utils import load_transactions
from unittest.mock import Mock


def test_load_transactions(final_path: str) -> None:
    """Тест с mock для utils, если файл не существует"""
    assert load_transactions(final_path) == []


def test_load_trans(final_p: str, trial: list) -> None:
    """Тест при правильной работе функции"""
    assert load_transactions(final_p) == trial


def test_load(final: str) -> None:
    """Отлов ошибки JSONDecodeError"""
    assert load_transactions(final) == []
