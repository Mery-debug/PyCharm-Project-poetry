from typing import Any

from functools import wraps

# from typing import


def log(filename=None) -> Any:
    """Декоратор логирующий функции"""
    def wrapper(func) -> Any:
        @wraps(func)
        def inner(*args, **kwargs) -> Any:
            if filename:
                try:
                    with open("log.txt", "r+", encoding='utf-8') as file:
                        file.write(f"Начало работы функции")
                        file.write(f"Документация функции: {func.__doc__}")
                        start = func(*args, **kwargs)
                        file.write(f"Результат работы функции: {start}")
                        file.write(f"Конец работы функции")
                except TypeError:
                    print("Ошибка типа данных")
            elif not filename:
                print(f"\nНачало работы функции")
                print(f" \nДокументация функции: {func.__doc__}")
                start = func(*args, **kwargs)
                print(f"\nРезультат работы функции: {start}")
                print(f"\nКонец работы функции")
            return start
        return inner
    return wrapper
