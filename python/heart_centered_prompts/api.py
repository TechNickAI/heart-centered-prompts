"""
API for accessing heart-centered AI prompts.
"""

from pathlib import Path
from typing import Literal

DetailLevelType = Literal["comprehensive", "standard", "concise", "terse"]
CollectionType = Literal["align_to_love"]


def get_prompt(detail_level: DetailLevelType = "standard", collection: CollectionType = "align_to_love") -> str:
    """
    Get a heart-centered AI prompt.

    Args:
        detail_level: Controls the prompt's verbosity and complexity:
            - "terse": Minimal version (~200 tokens)
            - "concise": Shorter version (~500 tokens)
            - "standard": Balanced approach (~1000 tokens)
            - "comprehensive": Detailed guidance (~2000+ tokens)

        collection: The prompt collection to use:
            - "align_to_love": Heart-centered AI alignment prompts

    Returns:
        The prompt text as a string

    Raises:
        FileNotFoundError: If the requested prompt file doesn't exist
        ValueError: If an invalid detail_level or collection is provided
    """
    # Validate inputs
    valid_collections = ["align_to_love"]
    valid_detail_levels = ["comprehensive", "standard", "concise", "terse"]

    if collection not in valid_collections:
        raise ValueError(f"Collection '{collection}' not found. Available collections: {valid_collections}")

    if detail_level not in valid_detail_levels:
        raise ValueError(f"Detail level '{detail_level}' not found. Available detail levels: {valid_detail_levels}")

    # Get the package directory where prompts are stored
    current_file = Path(__file__).resolve()
    package_dir = current_file.parent
    prompt_path = package_dir / "prompts" / collection / f"{detail_level}.txt"

    if not prompt_path.exists():
        installation_message = (
            "Prompt files may not have been copied during installation. "
            "If you're running from the source directory, try installing with: "
            "'pip install -e .' from the 'python' directory."
        )
        raise FileNotFoundError(f"Prompt file not found at {prompt_path}. {installation_message}")

    # Use Path.open() instead of open()
    with prompt_path.open("r", encoding="utf-8") as f:
        return f.read()
