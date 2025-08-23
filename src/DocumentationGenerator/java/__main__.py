from . import parser
import os
import jast


def main():
    os.makedirs("docs", exist_ok=True)
    directory: str = "src"
    files: dict[jast.Module] = parser.parseDirectory(directory)
    print(files)
