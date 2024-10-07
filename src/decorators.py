from typing import Any

from functools import wraps

# from typing import


def log(filename=None) -> Any:
    """Декоратор логирующий функции"""
    def wrapper(func) -> Any:
        @wraps(func)
        def inner(*args, **kwargs) -> Any:
            if filename:
                with open("log.txt", "a", encoding='utf-8') as file:
                    try:
                        file.write(f"\nНачало работы функции {func.__name__}")
                        file.write(f"\nДокументация функции: {func.__doc__}")
                        start = func(*args, **kwargs)
                        file.write(f"\nРезультат работы функции: {start}")
                        file.write(f"\nКонец работы функции")
                    except TypeError:
                        return f"Данные об ошибке: TypeError, неверный формат параметров\nКонец работы функции"
            elif not filename:
                try:
                    print(f"\nНачало работы функции")
                    print(f"\nДокументация функции: {func.__doc__}")
                    start = func(*args, **kwargs)
                    print(f"\nРезультат работы функции: {start}")
                    print(f"\nКонец работы функции")
                except TypeError:
                    return "Данные об ошибке: TypeError, неверный формат параметров"
                return start
        return inner
    return wrapper
