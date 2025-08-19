import json

def loadFromJson(filename: str) -> dict:
    """
    THIS IS A TEST DOC STRING IN SIMPLE.PY
    """
    with open(filename, "r") as f:
        data = json.load(f)
    return data