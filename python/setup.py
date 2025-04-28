"""
Setup script for heart_centered_prompts.
"""

import os
import shutil
from pathlib import Path

from setuptools import find_packages, setup
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info
from setuptools.command.install import install

# Read the contents of README.md
readme_path = Path(__file__).parent / "README.md"
with readme_path.open("r", encoding="utf-8") as f:
    long_description = f.read()


def copy_prompts(target_dir):
    """
    Copy prompts from project root to the package at build/install time.

    This keeps a single source of truth for prompts.
    """
    # Path to the package directory where prompts will be stored
    prompts_pkg_dir = Path(target_dir) / "heart_centered_prompts" / "prompts"

    # Create prompts directory in package if it doesn't exist
    prompts_pkg_dir.mkdir(parents=True, exist_ok=True)

    # Path to the prompts directory in project root (two levels up from setup.py)
    project_root = Path(__file__).parent.parent
    prompts_src_dir = project_root / "prompts"

    # Only continue if the source directory exists
    if not prompts_src_dir.exists():
        return

    # Copy each collection directory
    for collection_dir in prompts_src_dir.iterdir():
        if collection_dir.is_dir():
            collection_pkg_dir = prompts_pkg_dir / collection_dir.name
            collection_pkg_dir.mkdir(parents=True, exist_ok=True)

            # Copy all prompt files in this collection
            for prompt_file in collection_dir.glob("*.txt"):
                dest_file = collection_pkg_dir / prompt_file.name
                shutil.copy2(prompt_file, dest_file)


class CustomInstall(install):
    def run(self):
        copy_prompts(self.build_lib)
        install.run(self)


class CustomDevelop(develop):
    def run(self):
        copy_prompts(self.setup_path)
        develop.run(self)


class CustomEggInfo(egg_info):
    def run(self):
        egg_base = self.egg_base or os.curdir
        copy_prompts(egg_base)
        egg_info.run(self)


setup(
    name="heart_centered_prompts",
    use_scm_version=True,
    description="Heart-centered system prompts for AI assistants",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="TechnickAI",
    url="https://github.com/technickai/heart-centered-prompts",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
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
        "heart_centered_prompts": ["prompts/**/*.txt"],
    },
    cmdclass={
        "install": CustomInstall,
        "develop": CustomDevelop,
        "egg_info": CustomEggInfo,
    },
    zip_safe=False,
)
