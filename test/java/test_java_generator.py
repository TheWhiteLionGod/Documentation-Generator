from DocumentationGenerator.java import generator, datatypes, parser
from pathlib import Path
import jast


def test_generateHTMLForFunction():
    filename: Path = Path("test/java/assets/simple.java")
    tree: jast.Module = parser.parseFromFile(filename)
    function: datatypes.Function = parser.parseFunctionFromTree(tree)[0]
    html: str = generator.generateHTMLForFunction(function)

    expected_output: str = """<span class='text-primary'>public static</span>
<span class='text-success'>void</span>
<span class='text-warning'>main(</span>
<span class='text-success'>arraytype</span>
<span class=''>args</span>
<span class='text-warning'>);</span>
"""

    assert html == expected_output


def test_generateHTMLForClass():
    filename: Path = Path("test/java/assets/simple.java")
    tree: jast.Module = parser.parseFromFile(filename)
    cls: datatypes.Class = parser.parseClassesFromTree(tree)[0]
    html: str = generator.generateHTMLForClass(cls)

    expected_output: str = """<span class='text-primary'>public</span>
<span class='text-primary'>class</span>
<span class='text-success'>simple</span>
<span class='text-primary'>extends</span>
<span class='text-success'>parent_class</span>
<span class='text-primary'>implements</span>
<span class='text-success'>Interface</span>
<span class=''>, </span>
<span class='text-success'>test_interface</span>
<span class=''>{ </span>
<br>
<div class='mx-4'><p class='my-2'><span class='text-primary'>public static</span>
<span class='text-success'>void</span>
<span class='text-warning'>main(</span>
<span class='text-success'>arraytype</span>
<span class=''>args</span>
<span class='text-warning'>);</span>
</p>
</div>
<br>
<span class=''>}</span>
"""

    assert html == expected_output


def test_generateHTMLForInterface():
    filename: Path = Path("test/java/assets/interface.java")
    tree: jast.Module = parser.parseFromFile(filename)
    interface: datatypes.Interface = parser.parseInterfacesFromTree(tree)[0]
    html: str = generator.generateHTMLForInterface(interface)

    expected_output: str = """<span class='text-primary'>public</span>
<span class='text-primary'>interface</span>
<span class='text-success'>Interface</span>
<span class='text-primary'>extends</span>
<span class='text-success'>test_interface</span>
<span class=''>{ </span>
<br>
<div class='mx-4'><p class='my-2'><span class='text-success'>@Override</span>
<br>
<span class='text-primary'></span>
<span class='text-success'>void</span>
<span class='text-warning'>method1(</span>
<span class='text-primary'>final</span>
<span class='text-success'>double</span>
<span class=''>arg1</span>
<span class=''>, </span>
<span class='text-success'>int</span>
<span class=''>arg2</span>
<span class='text-warning'>);</span>
</p>
</div>
<br>
<span class=''>}</span>
"""

    assert html == expected_output
