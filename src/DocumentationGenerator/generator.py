from DocumentationGenerator import datatypes, html_builder


def generateHTMLForFunction(function: datatypes.Function) -> str:
    html = html_builder.HtmlBuilder(False) \
        .createSpan('text-primary', contents="def") \
        .createSpan('text-warning', contents=function.name + "(") \
        .createSpan(contents=function.args_html) \
        .createSpan("text-warning", contents=")") \
        .createSpan(contents=" -> ") \
        .createSpan("text-success", contents=function.result)
    
    if function.docstring:
        html.createSpan(contents=html_builder.HtmlBuilder(False) \
            .createLinebreak()
            .createSpan(contents=f"\"\"\"{function.docstring}\"\"\"")
        )
    
    return html.createSpan(contents=" ...").build()