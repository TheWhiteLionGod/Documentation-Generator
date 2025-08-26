from DocumentationGenerator.java import parser, datatypes
from pathlib import Path
import jast


def test_parseFromFile():
    filename: Path = Path("test/java/assets/simple.java")
    result: jast.Module = parser.parseFromFile(filename)

    expected_output: str = """public class simple extends parent_class implements Interface, test_interface {
    public static void main(String[] args) {
        System.out.println("simple.java");
    }
    ;
}"""
    assert jast.unparse(result) == expected_output


def test_parseDirectory():
    directory: Path = Path("test/java/assets")
    result: jast.Module = parser.parseDirectory(directory)

    assert len(result.keys()) == 4


def test_parseFunctionFromTree():
    filename: Path = Path("test/java/assets/simple.java")
    tree: jast.Module = parser.parseFromFile(filename)
    result: datatypes.Function = parser.parseFunctionFromTree(tree)[0]

    assert result.modifiers == ["public", "static"]
    assert result.annotations == []
    assert result.args == [["args", "arraytype", []]]
    assert ' '.join(result.result) == "void"
    assert result.name == "main"


def test_parseInterfacesFromTree():
    filename: Path = Path("test/java/assets/interface.java")
    tree: jast.Module = parser.parseFromFile(filename)
    result: datatypes.Interface = parser.parseInterfacesFromTree(tree)[0]

    assert result.modifiers == ["public"]
    assert result.name == "Interface"
    assert len(result.functions) == 1
    assert result.parent == "test_interface"


def test_parseClassesFromTree():
    filename: Path = Path("test/java/assets/simple.java")
    tree: jast.Module = parser.parseFromFile(filename)
    result: datatypes.Class = parser.parseClassesFromTree(tree)[0]

    assert result.name == "simple"
    assert result.modifiers == ["public"]
    assert result.parent == "parent_class"
    assert len(result.permits) == 0
    assert len(result.interfaces) == 2
    assert len(result.functions) == 1
