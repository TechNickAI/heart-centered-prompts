"""
Package-internal tests for heart_centered_prompts.

These tests are discoverable by `pytest --pyargs heart_centered_prompts`
and verify that the package works correctly after installation.
"""

from typing import Any, cast

import pytest

from . import get_prompt
from .api import DetailLevelType


def test_default_prompt():
    """Test that the default prompt (standard) can be retrieved."""
    prompt = get_prompt()
    assert prompt is not None
    assert len(prompt) > 0
    # Just verify it has substantial content
    assert len(prompt) > 500


def test_all_versions():
    """Test that all prompt detail levels can be retrieved."""
    detail_levels = ["terse", "concise", "standard", "comprehensive"]

    # Get all prompts to compare relative lengths
    prompts = {}
    for level in detail_levels:
        typed_level = cast(DetailLevelType, level)
        prompt = get_prompt(detail_level=typed_level)
        prompts[level] = prompt
        assert prompt is not None
        assert len(prompt) > 0

    # Check relative lengths instead of absolute values
    assert len(prompts["terse"]) < len(prompts["concise"])
    assert len(prompts["concise"]) < len(prompts["standard"])
    assert len(prompts["standard"]) < len(prompts["comprehensive"])


def test_invalid_collection():
    """Test that an invalid collection raises a ValueError."""
    with pytest.raises(ValueError):
        # We use Any to intentionally pass an invalid value for testing
        get_prompt(collection=cast(Any, "nonexistent"))


def test_invalid_detail_level():
    """Test that an invalid detail level raises a ValueError."""
    with pytest.raises(ValueError):
        # We use Any to intentionally pass an invalid value for testing
        get_prompt(detail_level=cast(Any, "nonexistent"))


def test_prompt_files_available():
    """Test that all expected prompt files are available after installation."""
    from pathlib import Path
    
    # Get the prompts directory
    prompts_dir = Path(__file__).parent / "prompts" / "align_to_love"
    
    # Check that all expected files exist
    expected_files = ["terse.txt", "concise.txt", "standard.txt", "comprehensive.txt"]
    for filename in expected_files:
        file_path = prompts_dir / filename
        assert file_path.exists(), f"Missing prompt file: {filename}"
        assert file_path.read_text().strip(), f"Empty prompt file: {filename}"