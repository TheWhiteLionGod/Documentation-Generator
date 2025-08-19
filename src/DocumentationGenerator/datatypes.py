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
                param_type = f"<span class='text-success'>{arg.annotation.id.strip()}</span>"
            args.append([f"<span class='text-primary'>{arg.arg}</span>", param_type, None])

        # Positional Arguments with Default Value
        for i, default in enumerate(arg_struct.defaults):
            index = len(arg_struct.args) - len(arg_struct.defaults) + i
            args[index][2] = f"<span class='text-success'>{ast.unparse(default).strip()}<span>"

        # Variable Positional Arguments
        if arg_struct.vararg:
            args.append(["<span class='text-primary'>*args</span>", "any", None])

        # Key Word Only Arguments + Potential Default
        for i, kwarg in enumerate(arg_struct.kwonlyargs):
            param_type: str = f"<span class='text-success'>{kwarg.annotation.id.strip() if kwarg.annotation else 'any'}</span>"
            default = None
            if arg_struct.kw_defaults[i]:
                default = f"<span class='text-primary'>{ast.unparse(arg_struct.kw_defaults[i]).strip()}</span>"

            args.append([f"<span class='text-primary'>{kwarg.arg}</span>", param_type, default])

        # Variable Key Word Arguments
        if arg_struct.kwarg:
            args.append(["<span class='text-primary'>**kwargs</span>", "any", None])

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
