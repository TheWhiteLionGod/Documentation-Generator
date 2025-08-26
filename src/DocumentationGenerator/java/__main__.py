from . import parser, datatypes
import os
import jast


def main():
    os.makedirs("docs", exist_ok=True)
    directory: str = "src"
    files: dict[str, jast.Module] = parser.parseDirectory(directory)
    
    print("="*50)
    for filename, tree in files.items():
        interfaces: list[datatypes.Interface] = parser.parseInterfacesFromTree(tree)
        for interface in interfaces:
            print(filename, interface.name, interface.modifiers, interface.parent)
