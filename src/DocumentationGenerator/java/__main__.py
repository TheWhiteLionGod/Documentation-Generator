from . import parser, datatypes
from ..html_builder import HtmlBuilder
from dotenv import dotenv_values
from pathlib import Path
import os
import jast


def main():
    os.makedirs("docs", exist_ok=True)
    directory: str = "src"
    files: dict[str, jast.Module] = parser.parseDirectory(directory)
    
    # Getting project config from .env.shared
    config: dict[str, str] = dotenv_values(".env.shared")
    
    html = HtmlBuilder() \
        .createH4("mt-4", contents=config["PROJECT_NAME"])\
        .createParagraph(contents="v" + config["PROJECT_VERSION"])

    table_of_contents_html = HtmlBuilder(False).createH4("px-3", "pt-2", contents="Table of Contents")
    for filename in files.keys():
        parts = list(filename.parts)
        parts.pop(0)
        link = Path(*parts).with_suffix(".py.html")
        table_of_contents_html.createDiv("py-2", contents=HtmlBuilder(False)
                                         .createLink("mx-4", contents=filename.name, link=link)
                                         .createLinebreak()
                                         )

    with open('docs/index.html', 'w') as f:
        f.write(html.createDiv("my-4", "bg-body-secondary", "rounded", contents=table_of_contents_html).build())

    for filename, tree in files.items():
        html = HtmlBuilder() \
            .createH4("mt-4", contents=str(filename) + ":")

        classes: list[datatypes.Class] = parser.parseClassesFromTree(tree)
        interfaces: list[datatypes.Interface] = parser.parseInterfacesFromTree(tree)

        class_html = HtmlBuilder(False)
        for cls in classes:
            class_html.createDiv("my-4", contents=generator.generateHTMLForClass(cls))

        html = html.createDiv("row", "my-4", "px-5", "bg-body-secondary", "rounded", contents=class_html)

        interface_html = HtmlBuilder(False)
        for interface in interfaces:
            # Interfaces without Docstrings are Considered Private
            interface_html.createDiv("my-4", contents=generator.generateHTMLForInterface(interface))

        html = html.createDiv("row", "my-4", "px-5", "bg-body-secondary", "rounded", contents=interface_html)
