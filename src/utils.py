from typing import Union
import os
import json
import logging

logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('../logs/utils.log', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_transactions(file_path: str) -> Union[dict, list]:
    """Function take json return list or dict with transaction"""
    if not os.path.exists(file_path):
        logger.error("Такой файл или путь не существует")
        return []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as json_file:
        try:
            logger.info(f"Открываем файл по пути {file_path} как json файл для записи в него")
            data = json.load(json_file)
            if type(data) == list:
                logger.info(f"Записываем {data} в файл, т.к. полученный объект имеет тип list")
                return data
            else:
                logger.error("Полученный тип не list")
                return []
        except json.JSONDecodeError as ex:
            logger.error(f"Ошибка {ex}")
            return []


if __name__ == "__main__":
    print(load_transactions(os.path.join(os.path.abspath(__file__), "../../data/operations.json")))
