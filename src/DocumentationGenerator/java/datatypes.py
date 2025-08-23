"""This Module defines the Structures to hold Function and Class Data"""
import jast


class Function:
    """This class holds Function Data"""
    def __init__(self, modifiers: list[jast._jast.JAST], name: str, args: jast._jast.params, result: jast._jast.jtype):
        """Init Method"""
        self.modifiers: list[str] = [type(modifier).__name__.lower() for modifier in modifiers if not isinstance(modifier, jast._jast.Annotation)]
        self.annotations: list[str] | None = ['.'.join(modifier.name.identifiers) for modifier in modifiers if isinstance(modifier, jast._jast.Annotation)]
        
        self.name: str = name
        
        self.args: list[list[str]] = [
            [
                arg.id.id, 
                
                type(arg.type).__name__.lower()
                if not isinstance(arg.type, jast._jast.Coit) 
                else self.arg.type.id + "<>"
                
                "final" 
                if "final" in ["final" for modifier in modifiers if type(modifier).__name__.lower() == "final"] 
                else ""
            ]
            for arg in args.parameters
        ]
        
        self.result: list[str] = [
                type(result).__name__.lower()
                if not isinstance(result, jast._jast.Coit)
                else result.id + "<>",

                [type(modifier).__name__.lower() for modifier in modifiers]
            ]
 