from DocumentationGenerator.html_builder import HtmlBuilder


def test_generateHtml():
    expected_output = """<!DOCTYPE html>
<html lang="en" data-bs-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Documentation</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-LN+7fdVzj6u52u30Kp6M/trliBMCMKTyK833zpbD+pXdCLuTusPj697FH4R/5mcr" crossorigin="anonymous">
</head>
<body>
    <div class="container mx-4" id="root">

<h4 class=''>Hello World</h4>
<p class=''>hi</p>
<br>
<a href='https://google.com' class=''>hello</a>
<div class='row px-5'><p class=''><span class=''>Test</span>
</p>
</div>
    </div>
</body>
</html>"""
    result = HtmlBuilder(generateInitalHtml=True) \
        .createH4(contents="Hello World") \
        .createParagraph(contents="hi") \
        .createLinebreak() \
        .createLink(contents="hello", link="https://google.com") \
        .createDiv("row", "px-5", contents=HtmlBuilder(generateInitalHtml=False)
                   .createParagraph(contents=HtmlBuilder(generateInitalHtml=False)
                                    .createSpan(contents="Test")
                                    )
                   ) \
        .build()

    assert expected_output == result
