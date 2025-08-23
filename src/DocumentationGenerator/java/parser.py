"""This Module Parses The Java Files"""
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
            print(filename)
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

