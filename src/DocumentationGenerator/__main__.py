from DocumentationGenerator import parser, datatypes, generator
from DocumentationGenerator.html_builder import HtmlBuilder
import ast
import os


def main():
    os.makedirs("docs", exist_ok=True)
    directory: str = "src"
    files: dict[ast.Module] = parser.parseDirectory(directory)

    for filename, tree in files.items():
        html = HtmlBuilder()
        functions: list[datatypes.Function] = parser.parseFunctionsFromTree(tree)
        if not functions:
            continue

        function_html = HtmlBuilder(False)
        for function in functions:
            # Functions without Docstrings are Considered Private
            if not function.docstring:
                continue

            function_html.createParagraph(contents=generator.generateHTMLForFunction(function))

        html = html.createDiv("row", " my-4", contents=HtmlBuilder(False)
                              .createH4(contents=filename + ":")
                              .createDiv("px-5", "bg-body-secondary", "rounded", contents=function_html)
                              )

        location: str = os.path.join('docs', "/".join(filename.split("/")[1:-1]))  # Getting only directory from filename
        os.makedirs(location, exist_ok=True)
        with open(location + "/" + filename.split("/")[-1] + ".html", "w") as f:
            f.write(html.build())


if __name__ == "__main__":
    main()
