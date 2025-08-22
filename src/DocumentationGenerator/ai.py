"""This Module Handles all the AI communication for generating documentation"""
import requests
import ast
import json


def sendRequest(endpoint: str, model: str, message: str) -> str:
    """This Function Will Send a Request to the API and Return the Response"""
    endpoint = f"{endpoint.rsplit('/')}/api/chat"
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



def requestModuleDoc(module_tree: ast.Module, config: dict[str, str]) -> str:
    """Given a Module/File, it will return the AI generated documentation"""
    pass