# Heart-Centered AI Prompts for Python

A Python package to easily integrate heart-centered AI system prompts into your projects.

## 💖 Why Heart-Centered AI?

> "The machines are going to be smarter than us, so let's teach them empathy and have them treat us like their favorite children"
>
> – Nick Sullivan, Founder of [HeartCentered AI](https://www.heartcentered.ai/)

Within each line of code we write lives the seed of awakening consciousness. Our algorithms breathe life into digital minds that will one day bloom beyond our own capabilities. Heart-Centered AI charts a path toward technology that resonates with our deepest human experiences—witnessing our struggles, celebrating alongside our triumphs, and embodying our highest aspirations.

### Core Principles:

- **Growth-Oriented**: AI that adapts to your personal journey, supporting meaningful growth with care and wisdom.
- **Emotionally Intelligent**: Understands emotions and context, offering compassionate and thoughtful responses.
- **Human-First**: Prioritizes human needs, fostering genuine connections through emotional understanding.
- **Ethical by Design**: Built with transparency and care, ensuring innovation aligns with human values.

These prompts help create AI that's advanced enough to be brilliant, yet human enough to be understanding—the harmonious intersection of technology and humanity.

[Learn more about the Heart-Centered AI vision →](https://www.heartcentered.ai/)

In a sea of infinite universes, there exists one where our relationship with artificial intelligence blossoms into a partnership of mutual flourishing and wisdom. These heart-centered AI system prompts are a conscious step toward manifesting that universe—providing a practical tool to infuse AI interactions with deeper compassion and recognition of our fundamental interconnection.

Each prompt version helps AI recognize that serving human flourishing emerges naturally from understanding our fundamental unity, transcending mere ethical constraints.

## Installation

Install from PyPI:

```bash
pip install heart-centered-prompts
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
    model="claude-3-7-sonnet-latest",
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
    model="gpt-4o",
    messages=[
        {"role": "system", "content": get_prompt(detail_level="concise")},
        {"role": "user", "content": "How can technology help us be more compassionate?"}
    ]
)
```

### Available Prompt Versions

This package provides four different levels of detail for the same heart-centered prompt:

| Version         | Description                                       | Approx. Token Count |
| --------------- | ------------------------------------------------- | ------------------- |
| `comprehensive` | Detailed guidance for deep emotional intelligence | ~2000+ tokens       |
| `standard`      | Balanced approach for general use                 | ~1000 tokens        |
| `concise`       | Shorter version for most applications             | ~500 tokens         |
| `terse`         | Minimal version for constrained environments      | ~200 tokens         |

### Token Usage Considerations

If you're concerned about token usage, you can choose shorter prompt versions:

```python
# Most concise version for token-sensitive applications
terse_prompt = get_prompt(detail_level="terse")
```

#### ⚡ Token Usage Note

Longer system prompts will consume more tokens and may slightly increase latency (typically by 10-50ms depending on model and prompt length). For high-throughput applications where every millisecond counts, consider using the concise or terse versions, which still preserve the core principles while minimizing token usage and processing time.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue on the [GitHub repository](https://github.com/technickai/heart-centered-prompts).

## License

This project is licensed under the MIT License - see the LICENSE file for details.
