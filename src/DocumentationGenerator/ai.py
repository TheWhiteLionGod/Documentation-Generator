"""This Module Handles all the AI communication for generating documentation"""
import requests
import ast
import json


def sendRequest(endpoint: str, model: str, message: str) -> str:
    """This Function Will Send a Request to the API and Return the Response"""
    endpoint = f"{endpoint}api/chat"
    payload: dict[str, any] = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ],
        "stream": False
    }

    try:
        response = requests.post(endpoint, json=payload, headers={'Content-Type': 'application/json'})
        response.raise_for_status()

        result: dict[str] = response.json()
        if result.get('message') and 'content' in result['message']:
            return result['message']['content']

        return f"Unexpected Response Format: {result}"
    except requests.exceptions.RequestException as e:
        return f"Request Failed: {e}"
    except json.JSONDecodeError as e:
        return f"Failed to parse json: {e}"
    except Exception as e:
        return f"Something went wrong: {e}"


def requestModuleDoc(module: str, config: dict[str, str]) -> str:
    """Given a Module/File, it will return the AI generated documentation"""
    message = f"""
You are a documentation generator.

You will be given an abstract syntax tree (AST) dump of a Python module.

Rules:
1. Document **only classes, functions, or methods that already have a docstring** in the AST.
2. Use the **exact names and argument structures** found in the AST. Never invent or change them.
3. If no docstring exists for an item, **skip it completely**.
4. Do not create new functions, classes, methods, or arguments that are not explicitly present.
5. Do not use markdown, headings, bullet points, or formatting. Output plain text only.
6. Do not talk about the benefits and limitations of the program.
7. The documentation should:
   - Restate and clarify the existing docstring in natural language.
   - Expand upon it if possible, but never guess functionality that is not mentioned.
   - Provide a brief usage example only if the docstring clearly indicates how.

Here is the AST:
{module}
"""

    return sendRequest(config["AI_HOST"], config["MODEL"], message)


if __name__ == '__main__':
    from DocumentationGenerator import parser
    # tree = parser.parseFromFile('src/DocumentationGenerator/html_builder.py')
    # print(requestModuleDoc(tree, {"AI_HOST": "https://ollama.franceisnotreal.com/", "MODEL": "codegemma:instruct"}))

    with open('src/DocumentationGenerator/html_builder.py', 'r') as f:
        module: str = f.read()
    print(requestModuleDoc(module, {"AI_HOST": "https://ollama.franceisnotreal.com/", "MODEL": "codegemma:instruct"}))
