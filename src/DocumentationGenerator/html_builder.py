"""Defines the Builder Architecture to Create HTML"""
from typing import Self


class HtmlBuilder:
    """This Class Provides Methods to Build HTML"""
    def __init__(self, generateInitalHtml: bool = True):
        """Defines the Builder. Takes in a bool to generate boilerplate html(html, head, and body tags)"""
        self.html = [""]
        if generateInitalHtml:
            self.generateInitalHtml()

    def generateInitalHtml(self):
        self.html = ["""<!DOCTYPE html>
<html lang="en" data-bs-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Documentation</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-LN+7fdVzj6u52u30Kp6M/trliBMCMKTyK833zpbD+pXdCLuTusPj697FH4R/5mcr" crossorigin="anonymous">
</head>
<body>
    <div class="container-fluid mx-4" id="root">
""",
                     """    </div>
</body>
</html>"""]

    def createH4(self, *classes, contents: 'str | HtmlBuilder') -> Self:
        """Creates a H4 Tag"""
        self.html.insert(-1, f"<h4 class='{' '.join([class_ for class_ in classes])}'>{contents}</h4>")
        return self

    def createParagraph(self, *classes, contents: 'str | HtmlBuilder') -> Self:
        """Creates a Paragraph Tag"""
        self.html.insert(-1, f"<p class='{' '.join([class_ for class_ in classes])}'>{contents}</p>")
        return self

    def createLinebreak(self) -> Self:
        """Creates a Br Tag"""
        self.html.insert(-1, "<br>")
        return self

    def createDiv(self, *classes, contents: 'str | HtmlBuilder') -> Self:
        """Creates a Div Tag"""
        self.html.insert(-1, f"<div class='{' '.join([class_ for class_ in classes])}'>{contents}</div>")
        return self

    def createSpan(self, *classes, contents: 'str | HtmlBuilder') -> Self:
        """Creates a Span Tag"""
        self.html.insert(-1, f"<span class='{' '.join([class_ for class_ in classes])}'>{contents}</span>")
        return self

    def build(self):
        """Returns the built html in the form of a string"""
        return "\n".join([html for html in self.html])

    def __str__(self):
        return self.build()
