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
    # Standard version should be between 1000-2000 chars typically
    assert 1000 < len(prompt) < 2000


def test_all_versions():
    """Test that all prompt detail levels can be retrieved."""
    detail_levels = ["terse", "concise", "standard", "comprehensive"]

    for level in detail_levels:
        # Use cast to fix type checking issues in tests
        typed_level = cast(DetailLevelType, level)
        prompt = get_prompt(detail_level=typed_level)
        assert prompt is not None
        assert len(prompt) > 0

        # Check each version has appropriate length
        if level == "terse":
            assert len(prompt) < 1000
        elif level == "concise":
            assert len(prompt) < 1500
        elif level == "standard":
            assert 1000 < len(prompt) < 2000
        elif level == "comprehensive":
            assert len(prompt) > 2000


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
