from DocumentationGenerator import datatypes, html


def generateHTMLForFunction(function: datatypes.Function) -> str:
    return  f"{html.setTextColor('def', 'text-primary')} " + \
            f"{html.setTextColor(function.name + "(", 'text-warning')}" + \
            f"{function.args}" + \
            f"{html.setTextColor(")", "text-warning")}" + \
             " -> " + \
            f"{html.setTextColor(function.result, "text-success")}" + \
            f"{html.createLineBreak()}\"\"\"{function.docstring}\"\"\"" if function.docstring else " ..."
