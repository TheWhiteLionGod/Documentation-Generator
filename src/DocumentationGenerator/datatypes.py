from DocumentationGenerator import html
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
            param_type: str = 'any'
            if isinstance(arg.annotation, ast.Name):
                param_type = html.setTextColor(arg.annotation.id.strip(), 'text-success')
            args.append([html.setTextColor(arg.arg, 'text-primary'), param_type, None])

        # Positional Arguments with Default Value
        for i, default in enumerate(arg_struct.defaults):
            index = len(arg_struct.args) - len(arg_struct.defaults) + i
            args[index][2] = html.setTextColor(ast.unparse(default).strip(), 'text-success')

        # Variable Positional Arguments
        if arg_struct.vararg:
            args.append([html.setTextColor("*args", "text-primary"), "any", None])

        # Key Word Only Arguments + Potential Default
        for i, kwarg in enumerate(arg_struct.kwonlyargs):
            param_type: str = html.setTextColor(kwarg.annotation.id.strip(), 'text-success') if kwarg.annotation else 'any'
            default = None
            if arg_struct.kw_defaults[i]:
                default =  html.setTextColor(ast.unparse(arg_struct.kw_defaults[i].strip(), 'text-primary'))

            args.append([html.setTextColor(kwarg.arg, 'text-primary'), param_type, default])

        # Variable Key Word Arguments
        if arg_struct.kwarg:
            args.append([html.setTextColor("**kwargs", 'text-primary'), "any", None])

        string_arg = ""
        for arg in args:
            string_arg += arg[0]

            if arg[1] != "any":
                string_arg += f": {arg[1]}"

            if arg[2] is not None:
                string_arg += f" = {arg[2]}"

            string_arg += ", "
        string_arg = string_arg[:-2]

        self.args: str = string_arg
