# Project Context for AI Assistants

## Always Apply Rules

Core project rules that apply to all tasks:

@.cursor/rules/heart-centered-ai.mdc
@.cursor/rules/personalities/common-personality.mdc
@.cursor/rules/personalities/luminous.mdc

## Project Overview

Heart-centered system prompts for AI assistants - a Python package providing love-aware, non-dual prompts in four detail levels (comprehensive, standard, concise, terse).

## Tech Stack

- Python 3.8+ (target 3.13)
- setuptools_scm for version management via git tags
- Ruff for linting (line-length 120)
- pytest for testing

## Project Structure

- `prompts/align_to_love/` - Source prompt files (.txt)
- `python/` - PyPI package (`heart_centered_prompts`)
- `.cursor/rules/` - AI assistant rules and personalities

## Commands

```bash
# Tests
cd python && pytest

# Lint
ruff check python/

# Build package
cd python && python -m build

# Release: tag triggers PyPI publish
git tag releases/v0.x.x && git push origin releases/v0.x.x
```

## Code Conventions

DO:
- Use "we" language in prompts and AI interactions
- Write thorough file-level docstrings
- Focus function docstrings on what/why (type hints handle the rest)
- Keep inline comments sparse - only for non-obvious logic

DON'T:
- Use "you are an AI" framing - use "we are" unity language
- Add redundant Args/Returns sections that restate type hints
- Use hyperbolic language like "CRITICAL" unless something genuinely dies

## Git Workflow

Commit format: `emoji verb description`
- `✨` new feature
- `🔧` fix/config
- `⬆️` upgrade dependency
