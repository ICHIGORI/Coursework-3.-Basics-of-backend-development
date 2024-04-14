import json
import os
from pathlib import Path


def get_operations_data(name: str = "operations.json", path: str = None) -> list:
    """Извлекает и возвращает, данные из json файла
    по умолчанию открывает файл по имени в ~/data директории"""
    path = path if path else os.path.join(Path(__file__).parent.parent, f"data/{name}")
    with open(path, encoding="utf-8") as file:
        return json.load(file)
