from DocumentationGenerator import parser, datatypes, generator
from DocumentationGenerator.html_builder import HtmlBuilder
import ast
import os


def main():
    os.makedirs("docs", exist_ok=True)
    directory: str = "src"
    files: dict[ast.Module] = parser.parseDirectory(directory)

    for filename, tree in files.items():
        file_docstring: str | None = parser.parseDocstringFromModule(tree)
        
        # Checking if file is "private"
        if file_docstring is None:
            continue

        html = HtmlBuilder().createH4("mt-4", contents=filename + ":")
        classes: list[datatypes.Class] = parser.parseClassesFromTree(tree)
        functions: list[datatypes.Function] = parser.parseFunctionsFromTree(tree)
        
        class_html = HtmlBuilder(False)
        for cls in classes:
            if cls.docstring is None:
                continue

            class_html.createDiv("my-4", contents=generator.generateHTMLForClass(cls))
        
        html = html.createDiv("row", "my-4", "px-5", "bg-body-secondary", "rounded", contents=class_html)
        
        function_html = HtmlBuilder(False)
        for function in functions:
            # Functions without Docstrings are Considered Private
            if function.docstring is None:
                continue

            function_html.createDiv("my-4", contents=generator.generateHTMLForFunction(function))

        html = html.createDiv("row", "my-4", "px-5", "bg-body-secondary", "rounded", contents=function_html)

        location: str = os.path.join('docs', "/".join(filename.split("/")[1:-1]))  # Getting only directory from filename
        os.makedirs(location, exist_ok=True)
        with open(location + "/" + filename.split("/")[-1] + ".html", "w") as f:
            f.write(html.build())


if __name__ == "__main__":
    main()
