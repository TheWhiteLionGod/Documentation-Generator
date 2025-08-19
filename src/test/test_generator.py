from DocumentationGenerator import parser, datatypes, generator
import ast


def test_generateFromFile1():
    filename: str = "src/test/assets/simple.py"
    tree: ast.Module = parser.parseFromFile(filename)
    functions: list[datatypes.Function] = parser.parseFunctionsFromTree(tree)
    result = generator.generateFromFile(filename, functions)

    expected_outcome = """src/test/assets/simple.py:
def loadFromJson(filename: str, one: int = 1, *args, isBool: bool, isEmpty: str = 'False', **kwargs) -> dict:
    \"\"\"THIS IS A TEST DOC STRING IN SIMPLE.PY\"\"\"
    ...
"""
    assert result == expected_outcome


def test_generateFromFile2():
    filename: str = "src/test/assets/simple.py"
    result = generator.generateFromFile(filename, [])

    expected_outcome = ""
    assert result == expected_outcome
