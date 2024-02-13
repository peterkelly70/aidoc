# aidoc.py

This Python script, `aidoc.py`, is designed to automatically generate documentation for a given project. It uses OpenAI's GPT-4 model to analyze the code and create human-readable explanations of the code's logic and structure in Markdown format.

## Installation

To install and set up the script, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies with the following command:

\```bash
pip install -r requirements.txt
\```

## Dependencies

The script depends on several Python libraries:

- `os`
- `sys`
- `random`
- `requests`
- `argparse`
- `json`
- `dotenv`
- `openai`

Make sure to install these dependencies before running the script.

## Environment Variables

The script requires an OpenAI API key, which should be stored as an environment variable named `OPENAI_API_KEY`.
This should be stored in .env

## Usage

The script is run from the command line and requires the path to the project directory as an argument. The argument is passed with the `-p` or `--projectdir` flag.

Example:

\```bash
python aidoc.py -p /path/to/your/project
\```

## Functionality

The script traverses the project directory and generates documentation for each `.php` and `.py` file it finds. The documentation for each file is saved in a `Documentation` directory within the project directory, with the same relative path as the original file and an `.md` extension.

## Customization

The file types for which the script generates documentation can be customized by modifying the `if` statement in the `generate_project_documentation` function.

## Output

The script prints the path to each file for which it generates documentation, as well as the path to the saved documentation file.

## Contributing

Contributions are welcome! Please read the contributing guidelines before making any changes.

## License

This project is licensed under the terms of the MIT license.
