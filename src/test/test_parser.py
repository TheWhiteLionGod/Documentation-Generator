from DocumentationGenerator import parser
import ast

def test_parseFromFile():
    filename: str = "src/test/assets/simple.py"
    with open(filename) as f:
        expected_output: ast.Module = ast.parse(f.read())

    result: ast.Module = parser.parseFromFile(filename)
    assert ast.dump(result) == ast.dump(expected_output)
    
def test_parseDirectory():
    directory: str = "src/test"
    expected_output: list[str] = ["test_parser.py", "simple.py"]  # Answers are Hardcoded

    result: dict[str, ast.Module] = parser.parseDirectory(directory)
    result: list[str] = list(result.keys())
    assert result == expected_output