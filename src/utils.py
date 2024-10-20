from typing import Union
import os
import json


def load_transactions(file_path: str) -> Union[dict, list]:
    """Function take json return list or dict with transaction"""
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as json_file:
        try:
            data = json.load(json_file)
            if type(data) == list:
                return data
            else:
                return []
        except json.JSONDecodeError:
            return []


print(load_transactions(os.path.join(os.path.abspath(__file__), "../../data/operations.json")))
