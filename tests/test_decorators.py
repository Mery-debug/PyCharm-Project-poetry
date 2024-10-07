from typing import Any
import tempfile
from src.decorators import log


def test_log_1() -> Any:
    """Тестируется запись в файл"""
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log("log.txt")
    def add(a: int, b: int) -> int:
        return a + b

    res = add(3, 6)
    with open("log.txt", "r", encoding='utf-8') as file:
        logs = file.read()
    assert "Начало работы функции" in logs


@log()
def add_numbers(a: int, b: int) -> int:
    """Тест декоратора с записью в консоль на функции сложения двух чисел"""
    return a + b


result = add_numbers(3, 5)
assert result == 8


def test_log_by_exception():
    """Тестирование при ошибке с записью в файл"""
    @log("log.txt")
    def v_1(a, b):
        return a - b

    res_1 = v_1(4, "1")
    assert res_1 == "Данные об ошибке: TypeError, неверный формат параметров\nКонец работы функции"


def test_log_by_exception_2():
    """Тестирование при ошибке с выводом в консоль"""
    @log()
    def v_2(a: int, b: int) -> int:
        return a - b
    res_2 = v_2(3, "1")
    assert res_2 == "Данные об ошибке: TypeError, неверный формат параметров"
