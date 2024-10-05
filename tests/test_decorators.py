import pytest

from src.decorators import log


def test_log():
    @log("log")
    def add_numbers(a: int, b: int) -> int:
        """Функция сложения двух чисел"""
        return a + b

    result = add_numbers(3, 5)
    assert result == 8
