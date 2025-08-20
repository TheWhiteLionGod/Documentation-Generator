from DocumentationGenerator import parser, datatypes, generator
from DocumentationGenerator.html_builder import HtmlBuilder
import argparse
import ast


def main():
    arg_parser = argparse.ArgumentParser(description="Generates Documentation for Python Projects")
    arg_parser.add_argument('dir', metavar="dir", type=str, help='Enter source directory of python files')
    args = arg_parser.parse_args()

    directory: str = args.dir
    files: dict[ast.Module] = parser.parseDirectory(directory)
    
    html = HtmlBuilder()
    for filename, tree in files.items():
        functions: list[datatypes.Function] = parser.parseFunctionsFromTree(tree)
        if not functions:
            continue 
        
        function_html = HtmlBuilder(False)
        for function in functions:
            function_html.createParagraph(contents=generator.generateHTMLForFunction(function))
 
        html = html.createDiv("row", " my-4", contents=HtmlBuilder(False)
                        .createH4(contents=filename + ":")
                        .createDiv("px-5", "bg-body-secondary", "rounded", contents=function_html)
                    )

    with open('test.html', "w") as f:
        f.write(html.build())

if __name__ == "__main__":
    main()
