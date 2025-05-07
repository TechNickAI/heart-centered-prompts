"""
Tests for the get_prompt function.
"""

from typing import Any, cast

import pytest

from heart_centered_prompts import get_prompt
from heart_centered_prompts.api import DetailLevelType


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
