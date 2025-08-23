from DocumentationGenerator.python import parser, datatypes
from pathlib import Path
import pytest


def test_EqualTo():
    filename: str = Path("test/python/assets/simple.py")
    tree: str = parser.parseFromFile(filename)

    functions: list[datatypes.Function] = parser.parseFunctionsFromTree(tree)

    assert functions[0].__eq__(functions[0])
    assert not functions[0].__eq__(functions[1])

    with pytest.raises(TypeError):
        functions[0].__eq__(1)
