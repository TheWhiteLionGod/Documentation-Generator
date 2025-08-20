from DocumentationGenerator import parser
from DocumentationGenerator import datatypes
import ast


def test_parseFromFile():
    filename: str = "src/test/assets/simple.py"
    with open(filename) as f:
        expected_output: ast.Module = ast.parse(f.read())

    result: ast.Module = parser.parseFromFile(filename)
    assert ast.dump(result) == ast.dump(expected_output)


def test_parseDirectory():
    directory: str = "src/test"
    expected_output: list[str] = ["src/test/test_html_builder.py", "src/test/test_generator.py", "src/test/test_parser.py", "src/test/assets/simple.py"]  # Answers are Hardcoded
    expected_output.sort()

    result: dict[str, ast.Module] = parser.parseDirectory(directory)
    result: list[str] = list(result.keys())
    result.sort()

    assert result == expected_output


def test_parseFunctionsFromTree():
    filename: str = "src/test/assets/simple.py"
    with open(filename) as f:
        tree: ast.Module = ast.parse(f.read())

    result: list[datatypes.Function] = parser.parseFunctionsFromTree(tree)
    print(result[0].name, result[0].docstring, result[0].args, result[0].result)

    assert len(result) == 1  # One Function
    assert result[0].name == "loadFromJson"
    assert result[0].docstring == "THIS IS A TEST DOC STRING IN SIMPLE.PY"
    assert result[0].args == [["filename", "str", None],
                              ["one", "int", "1"],
                              ["*args", "any", None],
                              ["isBool", "bool", None],
                              ["isEmpty", "str", "'False'"],
                              ["**kwargs", "any", None]]
    assert result[0].result == 'dict'
