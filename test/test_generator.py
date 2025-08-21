from DocumentationGenerator import parser, generator, datatypes
import ast


def test_generatorHTMLForFunction():
    filename: str = "test/assets/simple.py"
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
