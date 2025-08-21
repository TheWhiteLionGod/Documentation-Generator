import json


# Testing Position, Keyword, Default and Non Default, With and Without Type Annotation Arguments
def loadFromJson(filename: str, one: int = 1, *args, isBool: bool, isEmpty: str = "False", **kwargs) -> dict:
    """
    THIS IS A TEST DOC STRING IN SIMPLE.PY
    """
    with open(filename, "r") as f:
        data = json.load(f)
    return data
