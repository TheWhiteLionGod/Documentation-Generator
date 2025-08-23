from . import parser, datatypes
import os
import jast


def main():
    os.makedirs("docs", exist_ok=True)
    directory: str = "src"
    files: dict[str, jast.Module] = parser.parseDirectory(directory)
    
    print("="*50)
    for filename, tree in files.items():
        functions: list[datatypes.Function] = parser.parseFunctionFromTree(tree)
        for f in functions:
            print(filename, f.name, f.result)
