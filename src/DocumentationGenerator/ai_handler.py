"""This Module Handles all the AI communication for generating documentation"""
import requests
import json
import ast


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
You are a core maintainer of this project and know the details on how to operate the app.
Create documentation for the following file given its Abstract Syntax Tree.

First, identify the purpose of the file and what its trying to achieve.
Next, provide example usage on how a user can utilize the file.
Be sure to keep it as accurate to the information given in the tree as possible.
Finally, provide the output for the example usage.

Be sure to keep it nice and simple for a user to understand.
**Make sure you return pure text. Avoid using formatting such as markdown.**

Here is the ast:
{module}
"""

    return sendRequest(config["AI_HOST"], config["MODEL"], message)


if __name__ == '__main__':
    from DocumentationGenerator.python import parser
    tree = parser.parseFromFile('src/DocumentationGenerator/java/parser.py')
    print(requestModuleDoc(ast.dump(tree), {"AI_HOST": "https://ollama.franceisnotreal.com/", "MODEL": "codegemma:instruct"}))
