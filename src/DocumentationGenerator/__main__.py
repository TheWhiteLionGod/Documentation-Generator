from DocumentationGenerator import parser, datatypes, generator
from DocumentationGenerator.html_builder import HtmlBuilder
import ast
import os
import tomllib


def main():
    os.makedirs("docs", exist_ok=True)
    directory: str = "src"
    files: dict[ast.Module] = parser.parseDirectory(directory)

    with open('pyproject.toml', 'rb') as f:
        data: dict[str, any] = tomllib.load(f)
    
    if data.get('project') is None:
        data = {'project': {'name': "{PROJECT NAME}", "version": "1.0.0"}}
    
    html = HtmlBuilder() \
        .createH4("mt-4", contents=data['project']["name"]) \
        .createParagraph(contents="v" + data["project"]["version"])

    table_of_contents_html = HtmlBuilder(False).createH4("px-3", "pt-2", contents="Table of Contents")
    for filename, tree in files.items():
        file_docstring: str | None = parser.parseDocstringFromModule(tree)
        if file_docstring is None:
            continue

        table_of_contents_html.createDiv("py-2", contents=HtmlBuilder(False)
                                         .createLink("mx-4", contents=filename.split("/")[-1], link=filename.replace("src/", "") + ".html")
                                         .createLinebreak()
                                         )

    with open('docs/index.html', 'w') as f:
        f.write(html.createDiv("my-4", "bg-body-secondary", "rounded", contents=table_of_contents_html).build())

    for filename, tree in files.items():
        file_docstring: str | None = parser.parseDocstringFromModule(tree)

        # Checking if file is "private"
        if file_docstring is None:
            continue

        html = HtmlBuilder() \
            .createH4("mt-4", contents=filename + ":") \
            .createParagraph("mt-4", contents=f"\"\"\"{file_docstring}\"\"\"")

        classes: list[datatypes.Class] = parser.parseClassesFromTree(tree)
        functions: list[datatypes.Function] = parser.parseFunctionsFromTree(tree)

        # Removing Functions that are Class Methods
        class_methods: list[datatypes.Function] = [function for cls in classes for function in cls.functions]
        functions: list[datatypes.Function] = [function for function in functions if function not in class_methods]

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
