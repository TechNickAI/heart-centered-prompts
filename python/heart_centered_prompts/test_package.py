import pytest

from heart_centered_prompts import __version__, get_prompt
from heart_centered_prompts.api import DetailLevelType


def test_package_version():
    """Test that the package version is defined."""
    assert __version__ is not None


def test_get_prompt_valid_levels():
    """Test that get_prompt returns a non-empty string for all valid detail levels."""
    detail_levels: list[DetailLevelType] = ["terse", "concise", "standard", "comprehensive"]
    for level in detail_levels:
        prompt = get_prompt(detail_level=level)
        assert prompt is not None, f"Prompt for level '{level}' should not be None"
        assert isinstance(prompt, str), f"Prompt for level '{level}' should be a string"
        assert len(prompt) > 0, f"Prompt for level '{level}' should not be empty"


def test_get_prompt_invalid_level():
    """Test that get_prompt raises a ValueError for an invalid detail level."""
    invalid_level = "non_existent_level"
    with pytest.raises(ValueError) as excinfo:
        # We are intentionally passing an invalid type to test error handling.
        get_prompt(detail_level=invalid_level)  # type: ignore[arg-type]
    assert f"Detail level '{invalid_level}' not found" in str(excinfo.value)


def test_get_prompt_default_level():
    """Test that get_prompt returns the standard prompt by default."""
    default_prompt = get_prompt()
    standard_prompt = get_prompt(detail_level="standard")
    assert default_prompt == standard_prompt, "Default prompt should be the 'standard' prompt"
    assert len(default_prompt) > 0, "Default prompt should not be empty"
