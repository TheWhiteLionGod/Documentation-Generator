def createHeader(string: str) -> str:
    return f"<h4>{string}</h4>"


def createParagraph(string: str) -> str:
    return f"<p class='mt-1'>{string}</p>"


def createLineBreak() -> str:
    return "<br>"


def createDiv(*classes, contents: str) -> str:
    return f"<div class='{" ".join([class_ for class_ in classes])}'>{contents}</div>"

def setTextColor(string: str, color: str) -> str:
    return f"<span class='{color}'>{string}</span>"


def createHTML(contents: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en" data-bs-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Documentation</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-LN+7fdVzj6u52u30Kp6M/trliBMCMKTyK833zpbD+pXdCLuTusPj697FH4R/5mcr" crossorigin="anonymous">
</head>
<body>
    <div class="container-fluid" id="root">
        {contents}
    </div>
</body>
</html>
"""
