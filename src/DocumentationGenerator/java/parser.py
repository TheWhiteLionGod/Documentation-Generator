"""This Module Parses The Java Files"""
from . import datatypes
import pathlib
import jast
import antlr4
import os


def parseFromFile(filename: pathlib.Path) -> jast.Module:
    """Parses a Single File"""
    with open(filename, 'r') as f:
        data: str = f.read()
    data: jast.Module = jast.parse(data)
    return data


def parseDirectory(directory: pathlib.Path) -> dict[str, jast.Module]:
    """Parses Multiple Files stored in a Directory and its Subdirectories"""
    data: dict[str, jast.Module] = {}
    for root, _, files in os.walk(directory):
        for filename in files:
            if not filename.endswith(".java"):
                continue
            
            try:
                data.update({
                    pathlib.Path(root) / pathlib.Path(filename): parseFromFile(pathlib.Path(root) / pathlib.Path(filename))
                })
            except antlr4.error.Errors.ParseCancellationException as e:
                print(f"Failed to parse file: {filename} | Exception: {e}")
                continue

    return data


def jast_walk(node):
    if isinstance(node, list):
        for item in node:
            yield from jast_walk(item)
        return

    if not hasattr(node, "__dict__"):
        return

    yield node

    for field_value in vars(node).values():
        yield from jast_walk(field_value)


def parseFunctionFromTree(tree: jast.Module) -> list[datatypes.Function]:
    """Gets all the Functions from a Module"""
    result: list[datatypes.Function] = []
    functions = [f for f in jast_walk(tree) if isinstance(f, jast._jast.Method)]

    for f in functions:
        function = datatypes.Function(f.modifiers, f.id, f.parameters, f.return_type)
        result.append(function)
    return result


def parseInterfacesFromTree(tree: jast.Module) -> list[datatypes.Interface]:
    """Gets all the Interfaces from a Module"""
    result: list[datatypes.Interface] = []
    interfaces = [f for f in jast_walk(tree) if isinstance(f, jast._jast.Interface)]

    for i in interfaces:
        functions: list[datatypes.Function] = [
            datatypes.Function(f.modifiers, f.id, f.parameters, f.return_type)
            for f in i.body 
            if isinstance(f, jast._jast.Method)
        ]

        interface = datatypes.Interface(i.modifiers, i.id, i.extends, functions)
        result.append(interface)
    return result


def parseClassesFromTree(tree: jast.Module) -> list[datatypes.Class]:
    """Gets all the Classes from a Module"""
    result: list[datatypes.Class] = []
    classes = [f for f in jast_walk(tree) if isinstance(f, jast._jast.Class)]

    for cls in classes:
        functions: list[datatypes.Function] = [
            datatypes.Function(f.modifiers, f.id, f.parameters, f.return_type)
            for f in cls.body 
            if isinstance(f, jast._jast.Method)
        ]
        
        interfaces: list[str] = [
            interface.id
            for interface in cls.implements
            if isinstance(interface, jast._jast.Coit)
        ]
        class_ = datatypes.Class(cls.modifiers, cls.id, cls.extends, interfaces, cls.permits, functions)
        result.append(class_)
    return result
