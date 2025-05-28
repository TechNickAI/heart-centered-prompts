# Development Guide

## Setting up for Development

### Option 1: Using Symlinks (Recommended for Linux/macOS)

For development convenience, create symlinks to the root prompt files:

```bash
cd python/
python create_dev_symlinks.py
```

This creates symlinks from `heart_centered_prompts/prompts/` to the root `prompts/` directory, so you can edit the source files and immediately test without rebuilding.

### Option 2: Using setup.py (Cross-platform)

Install in development mode, which will copy files during installation:

```bash
cd python/
pip install -e .
```

Re-run this command whenever you modify prompt files.

## Running Tests

### External tests (during development)
```bash
cd python/
pytest tests/
```

### Package-internal tests (like CI does)
```bash
cd python/
pip install -e .  # Ensure package is installed
pytest --pyargs heart_centered_prompts
```

### All tests with coverage
```bash
cd python/
pytest --cov=heart_centered_prompts --cov-report=term
```

## CI/CD

The GitHub Actions workflow:
1. Installs the package (which copies prompt files via setup.py)
2. Runs external tests with coverage
3. Builds and installs the wheel
4. Runs package-internal tests with `pytest --pyargs heart_centered_prompts`

This ensures both development and installed package scenarios work correctly.