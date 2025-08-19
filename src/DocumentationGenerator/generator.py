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
