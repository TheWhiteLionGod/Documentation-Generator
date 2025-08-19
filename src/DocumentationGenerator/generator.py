from DocumentationGenerator import datatypes


def generateFromFile(filename: str, functions: list[datatypes.Function]) -> str:
    if not functions:
        return ""

    buffer = f"{filename}:\n"
    for f in functions:
        buffer += f"def {f.name}({f.args}) -> {f.result}:\n"
        buffer += f"    \"\"\"{f.docstring}\"\"\"\n" if f.docstring else ""
        buffer += "    ...\n"
    return buffer


def generateFunction(function: datatypes.Function) -> str:
    buffer  = f"<span class='text-primary'>def</span> <span class='text-warning'>{function.name}(</span>{function.args}<span class='text-warning'>)</span> -> <span class='text-success'>{function.result}</span>:\n"
    buffer += f"{createLineBreak()}    \"\"\"{function.docstring}\"\"\"\n" if function.docstring else ""
    buffer += "    ...\n"
    return buffer


def createHeader(string: str) -> str:
    return f"<h4>{string}</h4>"


def createParagraph(string: str) -> str:
    return f"<p class='mt-1'>{string}</p>"


def createLineBreak() -> str:
    return "<br>"
