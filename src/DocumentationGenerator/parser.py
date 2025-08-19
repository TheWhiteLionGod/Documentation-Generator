from . import datatypes
import ast
import os


def parseFromFile(filename: str) -> ast.Module:
    with open(filename, 'r') as f:
        data: str = f.read()
    data: ast.Module = ast.parse(data)
    return data


def parseDirectory(directory: str) -> dict[str, ast.Module]:
    data: dict[str, ast.Module] = {}
    for root, _, files in os.walk(directory):
        for filename in files:
            if not filename.endswith(".py"):
                continue

            data.update({
                filename: parseFromFile(os.path.join(root, filename))
            })

    return data


def parseFunctionsFromTree(tree: ast.Module) -> list[datatypes.Function]:
    result: list[datatypes.Function] = []
    functions = [f for f in ast.walk(tree) if isinstance(f, ast.FunctionDef)]

    for f in functions:
        function = datatypes.Function(f.name, ast.get_docstring(f), f.args, f.returns)
        result.append(function)
    return result
