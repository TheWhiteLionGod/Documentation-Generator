"""This Module Defines Classes To Group Parsed Data Together"""
from DocumentationGenerator.html_builder import HtmlBuilder
import ast


class Function:
    """This Class Stores A Functions Name, Docstring, Arguments, and Return Type"""
    def __init__(self, name: str, docstring: str | None, arg_struct, result):
        """Init Method"""
        self.name: str = name
        self.docstring: str | None = docstring

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

    def __eq__(self, other: 'Function') -> bool:
        if not isinstance(other, Function):
            raise TypeError(f"Tried to Compare a Function with a {type(other)}")

        return self.name == other.name \
            and self.docstring == other.docstring \
            and self.args_html == self.args_html \
            and self.result == self.result


class Class:
    """This Class Stores A Classes Name, Docstring, Parents(Parent Classes), and Methods"""
    def __init__(self, name: str, docstring: str | None, parents, functions: list[Function]):
        """Init Method"""
        self.name: str = name
        self.docstring: str | None = docstring
        self.parents: list[str] = [parent.id for parent in parents if isinstance(parent, ast.Name)]
        self.functions: list[Function] = functions
