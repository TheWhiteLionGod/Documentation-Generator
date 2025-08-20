from DocumentationGenerator import parser, datatypes, generator, html
import argparse
import ast


def main():
    arg_parser = argparse.ArgumentParser(description="Generates Documentation for Python Projects")
    arg_parser.add_argument('dir', metavar="dir", type=str, help='Enter source directory of python files')
    args = arg_parser.parse_args()

    directory: str = args.dir
    files: dict[ast.Module] = parser.parseDirectory(directory)
    
    for filename, tree in files.items():
        functions: list[datatypes.Function] = parser.parseFunctionsFromTree(tree)
        if not functions:
            continue
        
        html.createDiv(
            "row",
            "my-4",
            contents=""
        )
        f.write(generator.createHeader(f"{filename}:"))
        f.write("<div class='px-5 bg-body-secondary rounded'>")
        for function in functions:
            result = generator.generateFunction(function)
            f.write(generator.createParagraph(result))
        f.write("</div></div>")
    f.write("</body><html>")


if __name__ == "__main__":
    main()
