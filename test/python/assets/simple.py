"""TEST MODULE DOCSTRING"""
import json


class Test:
    """This is a Test class"""
    def __init__(self):
        """test  init"""
        pass


class Test2:
    """This is a test class 2"""
    pass


class Test3(Test2):
    """This is a test class 3"""
    pass


class Test4(Test):
    """This is a test class 4"""
    def __init__(self):
        """This is a init method"""
        pass


class Test5(Test, Test2):
    """This is a test class 5"""
    def __init__(self):
        pass


# Testing Position, Keyword, Default and Non Default, With and Without Type Annotation Arguments
def loadFromJson(filename: str, one: int = 1, *args, isBool: bool, isEmpty: str = "False", **kwargs) -> dict:
    """
    THIS IS A TEST DOC STRING IN SIMPLE.PY
    """
    with open(filename, "r") as f:
        data = json.load(f)
    return data
