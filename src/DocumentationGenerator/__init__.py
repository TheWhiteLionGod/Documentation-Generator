import importlib


def detect_project_type(path="."):
    # Simple heuristic: check for common files
    from pathlib import Path
    path = Path(path)
    if any(path.glob("*.py")):
        return "python"
    elif any(path.glob("*.java")):
        return "java"
    else:
        raise ValueError("Could not detect project type. No Python or Java files found.")


def load_generator(path="."):
    project_type = detect_project_type(path)
    module_name = f"DocumentationGenerator.{project_type}"
    return importlib.import_module(module_name)
