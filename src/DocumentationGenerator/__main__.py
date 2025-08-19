from DocumentationGenerator import parser, datatypes, generator
import argparse
import ast


def main():
    arg_parser = argparse.ArgumentParser(description="Generates Documentation for Python Projects")
    arg_parser.add_argument('dir', metavar="dir", type=str, help='Enter source directory of python files')
    args = arg_parser.parse_args()

    directory: str = args.dir
    files: dict[ast.Module] = parser.parseDirectory(directory)
    with open("result.txt", "w") as f:
        for filename, tree in files.items():
            functions: list[datatypes.Function] = parser.parseFunctionsFromTree(tree)
            result = generator.generateFromFile(filename, functions)
            f.write(f"{result}\n")


if __name__ == "__main__":
    main()
