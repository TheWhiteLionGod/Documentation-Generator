# Documentation Generator
This python module will take in your source directory, read through your python/java files, and generate documentation for it.

## Installation
```bash
pip install .
```

## Usage
### For Python Projects
**Important**: This project assumes your project structure is the following:
```markdown
.
|-- src
|   |-- {YOUR PROJECT}
|       |-- example.py
|-- pyproject.toml
|-- .env.secret(AI HOST + MODEL)
|-- .env.shared(OPTIONAL: Used If Unable To Get Project Data from pyproject.toml)
|
|   **File Structure Below Is Auto Generated**
|-- docs
|   |-- index.html
|   |-- {YOUR PROJECT}
|       |-- example.py.html
```

**Define *.env.secret* file**
1. Create File
```bash
touch .env.secret
```

2. Define the variables
```text
AI_HOST="{URL_ENDPOINT}"
MODEL="{MODEL: Ex. codegemma:instruct}"
```

**OPTIONAL: Define *.env.shared* file**
This file is used for metadata if we are unable to get it from pyproject.toml
1. Create File
```bash
touch .env.shared
```

2. Define the variables
```text
PROJECT_NAME={PROJECT_NAME}
PROJECT_VERSION={PROJECT_VERSION}
```

**Running Documentation Generator:**
```bash
python3 -m DocumentationGenerator
```

### For Java Projects
**Important**: This project assumes your project structure is the following:
```markdown
.
|-- src
|   |-- {YOUR PROJECT}
|       |-- example.java
|-- .env.secret(AI HOST + MODEL)
|-- .env.shared(Requried for Project Metadata)
|
|   **File Structure Below Is Auto Generated**
|-- docs
|   |-- index.html
|   |-- {YOUR PROJECT}
|       |-- example.java.html

```

**Define *.env.secret* file**
1. Create File
```bash
touch .env.secret
```

2. Define the variables
```text
AI_HOST="{URL_ENDPOINT}"
MODEL="{MODEL: Ex. codegemma:instruct}"
```

**Define *.env.shared* file**
This file is used for metadata
1. Create File
```bash
touch .env.shared
```

2. Define the variables
```text
PROJECT_NAME={PROJECT_NAME}
PROJECT_VERSION={PROJECT_VERSION}
```

**Running Documentation Generator:**
```bash
python3 -m DocumentationGenerator
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
