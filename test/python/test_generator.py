from DocumentationGenerator import parser, generator, datatypes
from pathlib import Path
import ast


def test_generateHTMLForFunction():
    filename: str = Path("test/python/assets/simple.py")
    tree: ast.Module = parser.parseFromFile(filename)
    functions: datatypes.Function = parser.parseFunctionsFromTree(tree)
    html: str = generator.generateHTMLForFunction(functions[0])
    expected_output = """<span class='text-primary'>def</span>
<span class='text-warning'>loadFromJson(</span>
<span class=''><span class='text-primary'>filename</span>
<span class=''>: </span>
<span class='text-success'>str</span>
<span class=''>, </span>
<span class='text-primary'>one</span>
<span class=''>: </span>
<span class='text-success'>int</span>
<span class=''> = </span>
<span class='text-primary'>1</span>
<span class=''>, </span>
<span class='text-primary'>*args</span>
<span class=''>, </span>
<span class='text-primary'>isBool</span>
<span class=''>: </span>
<span class='text-success'>bool</span>
<span class=''>, </span>
<span class='text-primary'>isEmpty</span>
<span class=''>: </span>
<span class='text-success'>str</span>
<span class=''> = </span>
<span class='text-primary'>'False'</span>
<span class=''>, </span>
<span class='text-primary'>**kwargs</span>
</span>
<span class='text-warning'>)</span>
<span class=''> -> </span>
<span class='text-success'>dict</span>
<span class=''><br>
<span class=''>\"\"\"THIS IS A TEST DOC STRING IN SIMPLE.PY\"\"\"</span>
</span>
<span class=''> ...</span>
"""
    assert html == expected_output


def test_generateHTMLForClass1():
    filename: str = Path("test/python/assets/simple.py")
    tree: ast.Module = parser.parseFromFile(filename)

    classes: list[datatypes.Class] = parser.parseClassesFromTree(tree)
    html: str = generator.generateHTMLForClass(classes[0])

    expected_output = """<span class='text-primary'>class</span>
<span class='text-success'>Test</span>
<span class=''>: </span>
<br>
<span class=''>\"\"\"This is a Test class\"\"\"</span>
<div class='mx-4'><p class='my-2'><span class='text-primary'>def</span>
<span class='text-warning'>__init__(</span>
<span class=''><span class='text-primary'>self</span>
</span>
<span class='text-warning'>)</span>
<span class=''> -> </span>
<span class='text-success'>None</span>
<span class=''><br>
<span class=''>\"\"\"test  init\"\"\"</span>
</span>
<span class=''> ...</span>
</p>
</div>
"""
    assert html == expected_output


def test_generateHTMLForClass2():
    filename: str = Path("test/python/assets/simple.py")
    tree: ast.Module = parser.parseFromFile(filename)

    classes: list[datatypes.Class] = parser.parseClassesFromTree(tree)
    html: str = generator.generateHTMLForClass(classes[1])

    expected_output: str = """<span class='text-primary'>class</span>
<span class='text-success'>Test2</span>
<span class=''>: </span>
<br>
<span class=''>\"\"\"This is a test class 2\"\"\"</span>
<br>
<span class=''>...</span>
"""

    assert html == expected_output


def test_generateHTMLForClass3():
    filename: str = Path("test/python/assets/simple.py")
    tree: ast.Module = parser.parseFromFile(filename)

    classes: list[datatypes.Class] = parser.parseClassesFromTree(tree)
    html: str = generator.generateHTMLForClass(classes[2])

    expected_output: str = """<span class='text-primary'>class</span>
<span class='text-success'>Test3</span>
<span class='text-warning'>(</span>
<span class='text-success'>Test2</span>
<span class='text-warning'>)</span>
<span class=''>: </span>
<br>
<span class=''>\"\"\"This is a test class 3\"\"\"</span>
<br>
<span class=''>...</span>
"""

    assert html == expected_output


def test_generateHTMLForClass4():
    filename: str = Path("test/python/assets/simple.py")
    tree: ast.Module = parser.parseFromFile(filename)

    classes: list[datatypes.Class] = parser.parseClassesFromTree(tree)
    html: str = generator.generateHTMLForClass(classes[3])

    expected_output: str = """<span class='text-primary'>class</span>
<span class='text-success'>Test4</span>
<span class='text-warning'>(</span>
<span class='text-success'>Test</span>
<span class='text-warning'>)</span>
<span class=''>: </span>
<br>
<span class=''>\"\"\"This is a test class 4\"\"\"</span>
<div class='mx-4'><p class='my-2'><span class='text-primary'>def</span>
<span class='text-warning'>__init__(</span>
<span class=''><span class='text-primary'>self</span>
</span>
<span class='text-warning'>)</span>
<span class=''> -> </span>
<span class='text-success'>None</span>
<span class=''><br>
<span class=''>\"\"\"This is a init method\"\"\"</span>
</span>
<span class=''> ...</span>
</p>
</div>
"""

    assert html == expected_output


def test_generateHTMLForClass5():
    filename: str = Path("test/python/assets/simple.py")
    tree: ast.Module = parser.parseFromFile(filename)

    classes: list[datatypes.Class] = parser.parseClassesFromTree(tree)
    html: str = generator.generateHTMLForClass(classes[4])

    expected_output: str = """<span class='text-primary'>class</span>
<span class='text-success'>Test5</span>
<span class='text-warning'>(</span>
<span class='text-success'>Test</span>
<span class=''>, </span>
<span class='text-success'>Test2</span>
<span class='text-warning'>)</span>
<span class=''>: </span>
<br>
<span class=''>\"\"\"This is a test class 5\"\"\"</span>
<div class='mx-4'></div>
"""

    assert html == expected_output
