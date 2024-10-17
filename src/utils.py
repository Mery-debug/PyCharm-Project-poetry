from typing import Any
import os
import json


# path_1 = "data/operations.json"

def load_transactions(file_path):
    if not os.path.exists(file_path):
        return []

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as json_file:
        try:
            data = json.load(json_file)
            if isinstance(data, list):
                return data
            else:
                return []
        except json.JSONDecodeError:
            return []


print(load_transactions("../data/operations.json"))
