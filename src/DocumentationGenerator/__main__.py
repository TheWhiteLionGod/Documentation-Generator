from DocumentationGenerator import parser, datatypes, generator
import argparse
import ast


def main():
    arg_parser = argparse.ArgumentParser(description="Generates Documentation for Python Projects")
    arg_parser.add_argument('dir', metavar="dir", type=str, help='Enter source directory of python files')
    args = arg_parser.parse_args()

    directory: str = args.dir
    files: dict[ast.Module] = parser.parseDirectory(directory)
    
    with open("index.html", "w") as f:
        f.write("""<!DOCTYPE html>
<html lang="en" data-bs-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Documentation</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-LN+7fdVzj6u52u30Kp6M/trliBMCMKTyK833zpbD+pXdCLuTusPj697FH4R/5mcr" crossorigin="anonymous">
</head>
<body class="container-fluid">
""")

        for filename, tree in files.items():
            functions: list[datatypes.Function] = parser.parseFunctionsFromTree(tree)
            if not functions:
                continue
            
            f.write("<div class='row my-4'>")
            f.write(generator.createHeader(f"{filename}:"))
            f.write("<div class='px-5 bg-body-secondary rounded'>")
            for function in functions:
                result = generator.generateFunction(function)
                f.write(generator.createParagraph(result))
            f.write("</div></div>")
        f.write("</body><html>")


if __name__ == "__main__":
    main()
