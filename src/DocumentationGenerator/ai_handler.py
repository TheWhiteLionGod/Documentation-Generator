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


def requestModuleDoc(module: str, language: str, config: dict[str, str]) -> str:
    """Given a Module/File, it will return the AI generated documentation"""
    message = f"""
You are an expert in static code analysis and technical documentation.

Your task: produce accurate, plain-text documentation for the following Abstract Syntax Tree (AST).
The AST may represent either Python 3.x or Java code.

Output must include ONLY the following three sections in this exact order and wording:
OVERVIEW:
USAGE EXAMPLES:
EXPECTED OUTPUT:

Rules:
1) Preserve all symbol names (classes, methods, functions, parameters) exactly as they appear in the AST.
2) If any information is missing (types, behavior, output), write "Unknown" rather than guessing.
3) Do not fabricate behavior or example results. Base your output strictly on the AST content (docstrings, literals, returns, print statements, etc.).
4) USAGE EXAMPLES must use the actual names and expected calling patterns from the AST.
5) EXPECTED OUTPUT must describe what the example produces (printed text, returned value, etc.), or "Unknown" if not determinable from the AST.
6) Keep output short, technical, and plain text (no Markdown, no HTML, no code fences).

Input:
Language: {language}  # Either "Python" or "Java"
AST:
<<AST_START>>
{module}
<<AST_END>>

Example of the desired output format:
OVERVIEW:
This module defines a class 'DataProcessor' for handling CSV files and a utility function 'merge_records'.
- 'DataProcessor' provides methods to load, filter, and export data.
- 'merge_records' combines two lists of dictionaries based on a matching key.

USAGE EXAMPLES:
processor = DataProcessor(file_path="input.csv", delimiter=";")
filtered = processor.filter_rows(min_age=18, max_age=30, include_inactive=False)
processor.export("filtered_output.csv")

merged = merge_records(records_a=[{{"id": 1, "name": "Alice"}}],
                       records_b=[{{"id": 1, "score": 95}}],
                       key="id")

EXPECTED OUTPUT:
- The 'filter_rows' call returns a list of rows matching the specified criteria.
- The 'export' method writes the filtered data to "filtered_output.csv".
- The 'merge_records' function returns a merged list based on the 'id' field.
- Exact values depend on input data; no hardcoded sample output is visible in the AST.

Self-check (silent, do not print steps):
- Ensure USAGE EXAMPLES match actual parameter names and defaults.
- Ensure EXPECTED OUTPUT is derived from explicit return/print/throw/raise nodes only.
- Do not rename or invent classes, functions, or fields.
- Do not include Markdown or HTML formatting.
- Output only the three requested sections.

Now generate the documentation.
"""

    return sendRequest(config["AI_HOST"], config["MODEL"], message)

