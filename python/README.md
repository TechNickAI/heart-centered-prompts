# Heart-Centered AI Prompts for Python

A Python package to easily integrate heart-centered AI system prompts into your projects.

## Installation

Since this package isn't published to PyPI yet, you can install it directly from GitHub:

```bash
pip install git+https://github.com/technickai/heart-centered-prompts.git#subdirectory=python
```

## Usage

The package provides a simple way to access different heart-centered AI prompts.

### Basic Usage

```python
from heart_centered_prompts import get_prompt

# Get the default prompt (align_to_love, standard version)
prompt = get_prompt()

# Get a specific detail level
terse_prompt = get_prompt(detail_level="terse")
concise_prompt = get_prompt(detail_level="concise")
comprehensive_prompt = get_prompt(detail_level="comprehensive")

# Use the prompt with your favorite AI API
# Example with Anthropic's Claude
import anthropic

client = anthropic.Anthropic(api_key="your_api_key")
response = client.messages.create(
    model="claude-3-opus-20240229",
    system=prompt,  # Use the heart-centered prompt
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "How can I implement a more ethical approach to AI?"}
    ]
)
```

### Available Prompts

Currently, the package supports the `align_to_love` collection with four detail levels:

- `comprehensive`: Detailed guidance for deep emotional intelligence (~2000+ tokens)
- `standard`: Balanced approach for general use (~1000 tokens)
- `concise`: Shorter version for most applications (~500 tokens)
- `terse`: Minimal version for constrained environments (~200 tokens)

```python
# Example with OpenAI
from openai import OpenAI
from heart_centered_prompts import get_prompt

client = OpenAI(api_key="your_api_key")
completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": get_prompt(detail_level="concise")},
        {"role": "user", "content": "How can technology help us be more compassionate?"}
    ]
)
```

### Token Usage Considerations

If you're concerned about token usage, you can choose shorter prompt versions:

```python
# Most concise version for token-sensitive applications
terse_prompt = get_prompt(detail_level="terse")
```

## Development

### Code Quality Tools

This project uses:

- **Ruff**: Fast Python linter and formatter
- **pre-commit**: Runs checks automatically before commits

To set up development environment:

```bash
# Clone the repository
git clone https://github.com/technickai/heart-centered-prompts.git
cd heart-centered-prompts/python

# Install dev dependencies
pip install pytest ruff pre-commit

# Install pre-commit hooks
pre-commit install
```

### Testing

To run tests locally:

```bash
# Navigate to the python directory
cd python

# Install development dependencies
pip install pytest

# Run tests
pytest
```

## Build

To build the package for distribution:

```bash
# Navigate to the python directory
cd python

# Install build dependencies
pip install build

# Build both source distribution and wheel
python -m build

# This creates:
# - dist/heart_centered_prompts-0.1.0.tar.gz (source distribution)
# - dist/heart_centered_prompts-0.1.0-py3-none-any.whl (wheel)
```

The build process automatically copies prompt files from the main repository into the package.
This ensures the Python package has access to the most recent versions of the prompts.

To install the locally built package:

```bash
pip install dist/heart_centered_prompts-0.1.0-py3-none-any.whl
```

### GitHub Actions

This repository includes GitHub Actions workflows that automatically build and test the package on both Python 3.8 and Python 3.13. The workflow is triggered on push to main and when pull requests are opened that affect the Python package.

You can also manually trigger the workflow from the Actions tab on GitHub.

## Future Features

- Support for additional prompt collections beyond `align_to_love`
- Custom prompt templates with variable substitution
- Integration helpers for popular AI APIs

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue on the [GitHub repository](https://github.com/technickai/heart-centered-prompts).

## License

This project is licensed under the MIT License - see the LICENSE file for details.
