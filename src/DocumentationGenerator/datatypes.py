import ast


class Function:
    def __init__(self, name: str, docstring: str, arg_struct, result):
        self.name: str = name
        self.docstring: str = docstring
        self.result: str | None = None
        if result:
            if isinstance(result, ast.Name):
                self.result = result.id

        # Creating Argument Structure
        args: list[list[str | None]] = []
        # Positional Arguments
        for arg in arg_struct.args:
            param_type: str = 'any'
            if isinstance(arg.annotation, ast.Name):
                param_type = arg.annotation.id.strip()
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
            param_type: str = kwarg.annotation.id.strip() if kwarg.annotation else 'any'
            default = None
            if arg_struct.kw_defaults[i]:
                default = ast.unparse(arg_struct.kw_defaults[i]).strip()

            args.append([kwarg.arg, param_type, default])

        # Variable Key Word Arguments
        if arg_struct.kwarg:
            args.append(["**kwargs", "any", None])

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
