import pytest

from src.decorators import log


# with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
#     log_file_path = tmp_file.name

def test_log():
    @log("log.txt")
    def add_numbers(a, b):
        """Функция сложения двух чисел"""
        return a + b

    result = add_numbers(3, 5)
    assert result == 8
