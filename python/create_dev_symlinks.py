#!/usr/bin/env python3
"""
Development helper script to create symlinks to prompt files.

This allows development without running setup.py each time prompt files change.
Run this script from the python/ directory.
"""

import os
from pathlib import Path


def main():
    """Create symlinks from package prompts directory to root prompts."""
    python_dir = Path(__file__).parent
    root_dir = python_dir.parent
    
    # Source and destination directories
    source_dir = root_dir / "prompts" / "align_to_love"
    dest_dir = python_dir / "heart_centered_prompts" / "prompts" / "align_to_love"
    
    # Ensure destination directory exists
    dest_dir.mkdir(parents=True, exist_ok=True)
    
    if not source_dir.exists():
        print(f"Source directory not found: {source_dir}")
        return
    
    # Create symlinks for all .txt files
    for prompt_file in source_dir.glob("*.txt"):
        dest_file = dest_dir / prompt_file.name
        
        # Remove existing file/symlink if it exists
        if dest_file.exists() or dest_file.is_symlink():
            dest_file.unlink()
        
        # Create symlink
        try:
            dest_file.symlink_to(prompt_file)
            print(f"Created symlink: {dest_file} -> {prompt_file}")
        except OSError as e:
            print(f"Failed to create symlink for {prompt_file.name}: {e}")
            print("Falling back to copying file...")
            # Fallback to copying if symlinks aren't supported
            dest_file.write_text(prompt_file.read_text())
            print(f"Copied file: {dest_file}")


if __name__ == "__main__":
    main()