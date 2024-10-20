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


def test_lo(triang: str) -> None:
    """Проверка, что тип не list"""
    with open(triang, "w", encoding='utf-8') as json_file:
        json_file.write('{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041", "operationAmount": { "amount": "31957.58", "currency": { "name": "руб.", "code": "RUB" }')
        assert load_transactions(triang) == []
