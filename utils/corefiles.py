import json
import os
from typing import Dict, List, Optional




def readJson(path)->Dict:
    try:
        with open(path, "r", encoding="utf-8") as cf:
            return json.load(cf)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def writeJson(path, data : Dict)->Dict:
    with open(path, "w", encoding="utf-8") as cf:
        json.dump(data, cf, indent=4)

def updateJson(path, data : Dict, keys: Optional[List[str]] = None) -> None:
    currentData = readJson()

    if not keys:
        currentData.update(data)
    else:
        current = currentData
        for key in keys[:-1]:
            current = current.setdefault(key, {})
        if keys:
            current.setdefault(keys[-1], {}).update(data)
    
    writeJson(currentData)

def deleteJson(path: List[str])->bool:
    data = readJson()
    if not data:
        return False
    
    current = data
    for key in path[:-1]:
        if key not in current:
            return False
        current = current[key]
    
    if path and path[-1] in current:
        del current[path[-1]]
        writeJson(data)
        return True
    return False

def initializeJson(initialStructure:Dict)->None:
    if not os.path.isfile(DB_FILE):
        writeJson(initialStructure)
    else:
        currentData = readJson()
        for key, value in initialStructure.items():
            if key not in currentData:
                currentData[key] = value
        writeJson(currentData)