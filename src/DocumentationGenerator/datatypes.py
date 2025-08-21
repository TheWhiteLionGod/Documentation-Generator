from DocumentationGenerator.html_builder import HtmlBuilder
import ast


class Function:
    def __init__(self, name: str, docstring: str, arg_struct, result):
        self.name: str = name
        self.docstring: str = docstring

        self.result: str = "None"
        if isinstance(result, ast.Name):
            self.result = result.id

        # Creating Argument Structure
        args: list[list[str | None]] = []
        # Positional Arguments
        for arg in arg_struct.args:
            param_type: str = arg.annotation.id.strip() if isinstance(arg.annotation, ast.Name) else 'any'
            args.append([arg.arg, param_type, None])

        # Positional Arguments with Default Value
        for i, default in enumerate(arg_struct.defaults):
            index = len(arg_struct.args) - len(arg_struct.defaults) + i
            args[index][2] = ast.unparse(default).strip()

        # Variable Positional Arguments
        if arg_struct.vararg:
            args.append(["*args", "any", None])

        # Key Word Only Arguments + Potential Default
        for i, kwarg in enumerate(arg_struct.kwonlyargs):
            param_type: str = kwarg.annotation.id.strip() if isinstance(kwarg.annotation, ast.Name) else 'any'
            default = None
            if arg_struct.kw_defaults[i]:
                default = ast.unparse(arg_struct.kw_defaults[i]).strip()

            args.append([kwarg.arg, param_type, default])

        # Variable Key Word Arguments
        if arg_struct.kwarg:
            args.append(["**kwargs", "any", None])

        self.args: list[str] = args
        self.args_html = self.createHtmlForArgs()

    def createHtmlForArgs(self) -> str:
        result = HtmlBuilder(False)
        for i, (arg_name, type, default) in enumerate(self.args):
            result = result.createSpan("text-primary", contents=arg_name)

            if type != "any":
                result = result \
                    .createSpan(contents=": ") \
                    .createSpan("text-success", contents=type)

            if default is not None:
                result = result \
                    .createSpan(contents=" = ") \
                    .createSpan("text-primary", contents=default)

            if (len(self.args) != i + 1):
                result = result.createSpan(contents=", ")
        return result.build()


class Class:
    def __init__(self, name: str, docstring: str):
        self.name = name
        self.docstring = docstring


class Module:
    def __init__(self, filename: str, docstring: str):
        self.filename = filename
        self.docstring = docstring
