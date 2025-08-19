from DocumentationGenerator import parser, datatypes
import argparse
import ast


def main():
    arg_parser = argparse.ArgumentParser(description="Generates Documentation for Python Projects")
    arg_parser.add_argument('dir', metavar="dir", type=str, help='Enter source directory of python files')
    args = arg_parser.parse_args()

    directory: str = args.dir
    files: dict[ast.Module] = parser.parseDirectory(directory)
    for filename, tree in files.items():
        functions = parser.parseFunctionsFromTree(tree)
        for f in functions:
            print(filename, f.name)


if __name__ == "__main__":
    main()
