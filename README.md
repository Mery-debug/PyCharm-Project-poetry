# PyCharm project poetry

## Описание:

Проект PyCharm project poetry - создан для освоения работы с github,
работы с домашним заданием по созданию банковского приложения для работы
с номерами счетов или банковских карт, а так же их маскирования.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/Mery-debug/PyCharm-Project-poetry.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```

## Использование:

1. Откройте проект в среде программирования PyCharm или в VsCode.
2. В вызове функций в файле `main.py`, в скобках после названия функций, введите необходимые для проверки данные.
3. Закончив проверку необходимых функций, закройте программу.

## Тестирование:

* Все функции проекта покрыты тестами с процентом покрытия не меньше 80% (100%).
* Для тестов использовался фреймворк pytest и фикстуры @pytest.fixture и @pytest.mark.parametrize.
* Для каждого модуля с функциями был создан отдельный файл с соответствующим пакету названием и префиксом test_.
* Файл для просмотра покрытия тестами функций index.html.
* Файлы с фикстурой @pytest.fixture - conftest.py.

## Документация:

Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).