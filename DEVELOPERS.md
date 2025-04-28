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

Our repository is configured with GitHub Actions to automatically publish to PyPI when a new `releases/v*` tag is pushed.

We use PyPI's recommended "trusted publishing" approach, which allows secure authentication without API tokens. The workflow:

1. Detects the new tag
2. Sets up Python and builds the package
3. Publishes to PyPI using OpenID Connect (OIDC) authentication

#### Setting Up Trusted Publishing

> **Note:** We're currently using the API token method for authentication. The instructions below are for future reference if you want to migrate to trusted publishing.

To set up trusted publishing in the future:

1. Create an environment in your GitHub repository settings:

   - Go to Settings → Environments → New environment
   - Name it `pypi`
   - Add environment protection rules if desired

2. Configure trusted publishing on PyPI:

   - Log in to your PyPI account at https://pypi.org/
   - Navigate to your project
   - Go to "Settings" → "Publishing"
   - Set up a new publisher with:
     - Publisher: GitHub Actions
     - Owner: TechNickAI
     - Repository name: heart-centered-prompts
     - Workflow name: Publish Python Package
     - Environment name: pypi

3. Modify the GitHub workflow file to use trusted publishing:
   ```yaml
   jobs:
     deploy:
       name: Upload release to PyPI
       runs-on: ubuntu-latest
       environment:
         name: pypi
         url: https://pypi.org/p/heart-centered-prompts
       permissions:
         id-token: write
       steps:
         # ... existing steps ...
         - name: Publish package to PyPI
           uses: pypa/gh-action-pypi-publish@v1.8.10
           with:
             packages-dir: python/dist/
             # No password needed with trusted publishing
             verbose: true
             print-hash: true
   ```

No API tokens needed with trusted publishing - the connection between GitHub and PyPI is secured through OpenID Connect!

#### Using API Tokens (Current Method)

We're currently using API tokens for PyPI authentication. Here's how to set them up:

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
