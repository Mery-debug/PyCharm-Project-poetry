from typing import Union, Any

from functools import wraps


def log(filename: Union[str] = "file") -> Any:
    def wrapper(func: Any) -> Any:
        @wraps(func)
        def inner(*args, **kwargs) -> Any:
            if filename == "file":
                try:
                    with open("log.txt", "r+", encoding='utf-8') as file:
                        file.write(f"Начало работы функции")
                        file.write(f"Документация функции: {func.__doc__}")
                        start = func(*args, **kwargs)
                        file.write(f"Результат работы функции: {start}")
                        file.write(f"Конец работы функции")
                except TypeError:
                    print("Ошибка типа данных")
            elif filename == "log":
                print(f"Начало работы функции")
                print(f" Документация функции: {func.__doc__}")
                start = func(*args, **kwargs)
                print(f"Результат работы функции: {start}")
                print(f"Конец работы функции")
                return start
            return inner
        return wrapper
