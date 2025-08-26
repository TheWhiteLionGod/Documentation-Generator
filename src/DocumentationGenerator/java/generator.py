"""This File Generates Html for Classes, Interfaces, and Functions"""
from ..html_builder import HtmlBuilder
from . import datatypes


def generateHTMLForFunction(function: datatypes.Function) -> str:
    """Takes in A Function and Returns The HTML For It"""
    html = HtmlBuilder(False)
    for i, annotation in enumerate(function.annotations):
        html = html.createSpan("text-success", contents="@" + annotation).createLinebreak()

    html = html \
        .createSpan('text-primary', contents=' '.join(function.modifiers)) \
        .createSpan('text-success', contents=' '.join(function.result)) \
        .createSpan('text-warning', contents=function.name + "(") \
    
    for i, arg in enumerate(function.args):
        if len(arg) == 3:
            html = html.createSpan("text-primary", contents=arg[2])

        html = html \
            .createSpan("text-success", contents=arg[1]) \
            .createSpan(contents=arg[0])
        
        if len(function.args) != i + 1:
            html = html.createSpan(contents=", ")
    
    return html.createSpan('text-warning', contents=");").build()


def generateHTMLForClass(cls: datatypes.Class) -> str:
    """Takes in a Class and Generates the HTML for the Class and its Methods"""
    html = HtmlBuilder(False) \
        .createSpan('text-primary', contents=' '.join(cls.modifiers)) \
        .createSpan('text-primary', contents="class") \
        .createSpan('text-success', contents=cls.name)

    if cls.parent != "nonetype":
        html = html \
            .createSpan("text-primary", contents="extends") \
            .createSpan("text-success", contents=cls.parent)

    if cls.interfaces and cls.interfaces[0] is not None:
        html = html.createSpan("text-primary", contents="implements")
        for i, interface in enumerate(cls.interfaces):
            html = html.createSpan("text-success", contents=interface)

            if len(cls.interfaces) != i + 1:
                html.createSpan(", ")

    html = html \
        .createSpan(contents="{ ") \
        .createLinebreak() \

    if cls.functions:
        functions_html = HtmlBuilder(False)
        for function in cls.functions:
            functions_html = functions_html.createParagraph("my-2", contents=generateHTMLForFunction(function))

        html.createDiv("mx-4", contents=functions_html)
    return html.createLinebreak().createSpan(contents="}").build()


def generateHTMLForInterface(interface: datatypes.Interface) -> str:
    """Takes in a Class and Generates the HTML for the Class and its Methods"""
    html = HtmlBuilder(False) \
        .createSpan('text-primary', contents=' '.join(interface.modifiers)) \
        .createSpan('text-primary', contents="interface") \
        .createSpan('text-success', contents=interface.name)

    if interface.parent != "nonetype":
        print(interface.parent)
        html = html \
            .createSpan("text-primary", contents="extends") \
            .createSpan("text-success", contents=interface.parent)

    html = html \
        .createSpan(contents="{ ") \
        .createLinebreak() \

    if interface.functions:
        functions_html = HtmlBuilder(False)
        for function in interface.functions:
            functions_html = functions_html.createParagraph("my-2", contents=generateHTMLForFunction(function))

        html.createDiv("mx-4", contents=functions_html)
    return html.createLinebreak().createSpan(contents="}").build()


