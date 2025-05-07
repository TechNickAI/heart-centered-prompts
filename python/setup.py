"""
Setup script for heart_centered_prompts.
"""

import shutil
from pathlib import Path

from setuptools import find_packages, setup

# Read the contents of README.md
readme_path = Path(__file__).parent / "README.md"
with readme_path.open("r", encoding="utf-8") as f:
    long_description = f.read()

# Copy prompt files from project root to package
root_dir = Path(__file__).parent.parent
package_dir = Path(__file__).parent / "heart_centered_prompts"
prompts_dir = root_dir / "prompts"
package_prompts_dir = package_dir / "prompts"

# Ensure the base prompts directory exists
package_prompts_dir.mkdir(parents=True, exist_ok=True)

if prompts_dir.exists():
    for collection in prompts_dir.iterdir():
        if collection.is_dir():
            # Create collection directory if it doesn't exist
            collection_path = package_prompts_dir / collection.name
            collection_path.mkdir(parents=True, exist_ok=True)

            # Copy prompt files
            for prompt_file in collection.glob("*.txt"):
                dest_file = collection_path / prompt_file.name
                shutil.copy2(prompt_file, dest_file)

setup(
    name="heart_centered_prompts",
    use_scm_version={"root": "..", "relative_to": __file__},
    description="Heart-centered system prompts for AI assistants that foster compassion and interconnection",
    keywords="AI, prompts, heart-centered, compassion, consciousness, alignment, love, emotional intelligence",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="TechnickAI",
    license="MIT",
    url="https://github.com/technickai/heart-centered-prompts",
    project_urls={
        "Homepage": "https://heartcentered.ai",
        "Bug Tracker": "https://github.com/technickai/heart-centered-prompts/issues",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    python_requires=">=3.8",
    include_package_data=True,
    package_data={
        "heart_centered_prompts": ["prompts/*/*.txt"],
    },
    zip_safe=False,
)
