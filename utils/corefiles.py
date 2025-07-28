import json
import os
from typing import Dict, List, Optional, Union


def read_json(path: str) -> Union[Dict, List]:
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {} if path.endswith(".json") else []

def write_json(path: str, data: Union[Dict, List]) -> None:
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def update_json(path: str, new_data: Dict, keys: Optional[List[str]] = None) -> None:
    data = read_json(path)

    if not isinstance(data, dict):
        raise ValueError("Solo se puede actualizar archivos JSON")

    if not keys:
        data.update(new_data)
    else:
        current = data
        for key in keys[:-1]:
            current = current.setdefault(key, {})
        current.setdefault(keys[-1], {}).update(new_data)

    write_json(path, data)


def delete_json_key(path: str, keys: List[str]) -> bool:
    data = read_json(path)
    if not data:
        return False

    current = data
    for key in keys[:-1]:
        if key not in current:
            return False
        current = current[key]

    if keys[-1] in current:
        del current[keys[-1]]
        write_json(path, data)
        return True

    return False

def initialize_json(path: str, initial_structure: Union[Dict, List]) -> None:
    if not os.path.isfile(path):
        write_json(path, initial_structure)
    else:
        current_data = read_json(path)
        if isinstance(current_data, dict) and isinstance(initial_structure, dict):
            for key, value in initial_structure.items():
                if key not in current_data:
                    current_data[key] = value
            write_json(path, current_data)
