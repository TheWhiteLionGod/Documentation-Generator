"""This Module Provides Functions to Generate HTML For Functions and Classes"""
from DocumentationGenerator import datatypes, html_builder


def generateHTMLForFunction(function: datatypes.Function) -> str:
    """Takes in A Function and Returns The HTML For It"""
    return html_builder.HtmlBuilder(False) \
        .createSpan('text-primary', contents="def") \
        .createSpan('text-warning', contents=function.name + "(") \
        .createSpan(contents=function.args_html) \
        .createSpan("text-warning", contents=")") \
        .createSpan(contents=" -> ") \
        .createSpan("text-success", contents=function.result) \
        .createSpan(contents=html_builder.HtmlBuilder(False)
                    .createLinebreak()
                    .createSpan(contents=f"\"\"\"{function.docstring}\"\"\"")
                    ) \
        .createSpan(contents=" ...") \
        .build()


def generateHTMLForClass(cls: datatypes.Class) -> str:
    """Takes in a Class and Generates the HTML for the Class and its Methods"""
    html = html_builder.HtmlBuilder(False) \
        .createSpan('text-primary', contents="class") \
        .createSpan('text-success', contents=cls.name)

    if cls.parents:
        html = html.createSpan("text-warning", contents="(")

        for i, parent in enumerate(cls.parents):
            html = html.createSpan("text-success", contents=parent)

            if len(cls.parents) != i + 1:
                html = html.createSpan(contents=", ")

        html = html.createSpan("text-warning", contents=")")

    html = html \
        .createSpan(contents=": ") \
        .createLinebreak() \
        .createSpan(contents=f"\"\"\"{cls.docstring}\"\"\"")

    if not cls.functions:
        html = html \
            .createLinebreak() \
            .createSpan(contents="...")
    else:
        functions_html = html_builder.HtmlBuilder(False)
        for function in cls.functions:
            if function.docstring is None:
                continue

            functions_html = functions_html.createParagraph("my-2", contents=generateHTMLForFunction(function))

        html.createDiv("mx-4", contents=functions_html)

    return html.build()
