# Developer Guide for Heart-Centered Prompts

This document explains how to work with this repository and publish new versions to PyPI.

## Understanding Version Management with setuptools_scm

This project uses `setuptools_scm` to automatically manage versions based on Git tags. This eliminates the need to manually update version numbers in code files.

### How It Works

1. The version is determined directly from Git tags and the state of the working directory
2. When you create a Git tag like `v0.1.0`, setuptools_scm uses this to set the package version
3. For commits after a tag, setuptools_scm creates versions like `0.1.0.dev4+g1234abc` (development version)
4. The version is dynamically determined at build/install time

### Benefits

- No need to manually update version numbers in code
- Version numbers always match Git tags
- Development versions clearly indicate they are not releases
- Clean workflow for publishing new versions

## Publishing to PyPI

Follow these steps to publish a new version to PyPI:

### 1. Ensure Your Code is Ready

```bash
# Make sure all changes are committed
git status

# Run tests
cd python
pytest
```

### 2. Create a New Git Tag

```bash
# First push all your regular commits
git push origin main  # (or whatever branch you're on)

# Create a new version tag locally
git tag releases/v0.2.0  # Update version number as needed

# Push the tag to GitHub (separate command)
git push origin releases/v0.2.0
```

**Important**: Git requires separate push commands for commits and tags. Your normal `git push` only pushes commits, not tags.

### 3. Manual Publishing (if not using GitHub Actions)

If you need to publish manually:

```bash
# Navigate to the python directory
cd python

# Build the package
python -m build

# Upload to PyPI
twine upload dist/*
```

### 4. Using GitHub Actions for Automatic Publishing

Our repository is configured with GitHub Actions to automatically publish to PyPI when a new `releases/v*` tag is pushed. The workflow:

1. Detects the new tag
2. Sets up Python
3. Builds the package
4. Publishes to PyPI using the stored API token

To make this work:

- Ensure the `PYPI_API_TOKEN` secret is set in your GitHub repository settings
- Simply create and push a tag following the pattern `releases/v*`

### Setting Up Your PyPI API Token

PyPI no longer accepts username/password authentication. You must use API tokens:

1. Log in to your PyPI account at https://pypi.org/
2. Go to Account Settings → API tokens
3. Click "Add API token"
4. Set a token name (e.g., "GitHub Actions Upload")
5. Select "Entire account (all projects)" or choose a specific project
6. Copy the generated token (You'll only see it once!)

Then add it to your GitHub repository:

1. Go to your GitHub repository → Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Name: `PYPI_API_TOKEN`
4. Value: (paste your PyPI token)
5. Click "Add secret"

The GitHub action is configured to use this token automatically.

## Working with Local Development Versions

When developing locally:

```bash
# Install in development mode
cd python
pip install -e .

# This will use the Git version information for the package
```

## Troubleshooting

If you encounter issues with versions:

1. Make sure your Git repository has at least one tag
2. Check that setuptools_scm is properly installed in your development environment
3. For package import errors during development, you may need to install the package in editable mode
