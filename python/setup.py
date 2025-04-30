"""
Setup script for heart_centered_prompts.
"""

from pathlib import Path

from setuptools import find_packages, setup

# Read the contents of README.md
readme_path = Path(__file__).parent / "README.md"
with readme_path.open("r", encoding="utf-8") as f:
    long_description = f.read()

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
    zip_safe=False,
)
