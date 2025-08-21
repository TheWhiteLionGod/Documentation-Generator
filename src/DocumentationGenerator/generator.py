from DocumentationGenerator import datatypes, html_builder


def generateHTMLForFunction(function: datatypes.Function) -> str:
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
