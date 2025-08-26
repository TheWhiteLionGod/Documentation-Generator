"""This Module Parses The Python Files"""
from . import datatypes
import pathlib
import ast
import os


def parseFromFile(filename: pathlib.Path) -> ast.Module:
    """Parses a Single File"""
    with open(filename, 'r') as f:
        data: str = f.read()
    data: ast.Module = ast.parse(data)
    return data


def parseDirectory(directory: pathlib.Path) -> dict[str, ast.Module]:
    """Parses Multiple Files stored in a Directory and its Subdirectories"""
    data: dict[str, ast.Module] = {}
    for root, _, files in os.walk(directory):
        for filename in files:
            if not filename.endswith(".py"):
                continue

            data.update({
                pathlib.Path(root).joinpath(pathlib.Path(filename)): parseFromFile(pathlib.Path(root).joinpath(pathlib.Path(filename)))
            })

    return data


def parseFunctionsFromTree(tree: ast.Module) -> list[datatypes.Function]:
    """Gets all the Functions from a File"""
    result: list[datatypes.Function] = []
    functions = [f for f in ast.walk(tree) if isinstance(f, ast.FunctionDef)]

    for f in functions:
        function = datatypes.Function(f.name, ast.get_docstring(f), f.args, f.returns)
        result.append(function)
    return result


def parseClassesFromTree(tree: ast.Module) -> list[datatypes.Class]:
    """Gets all the Classes from a File"""
    result: list[datatypes.Class] = []
    classes = [cls for cls in ast.walk(tree) if isinstance(cls, ast.ClassDef)]

    for cls in classes:
        functions: list[datatypes.Function] = parseFunctionsFromTree(cls)
        class_ = datatypes.Class(cls.name, ast.get_docstring(cls), cls.bases, functions)
        result.append(class_)
    return result


def parseDocstringFromModule(tree: ast.Module) -> str | None:
    """Returns the Docstring of a Module"""
    return ast.get_docstring(tree)
