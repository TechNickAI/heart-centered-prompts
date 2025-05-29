import logging
import shutil
import sys
from pathlib import Path

logger = logging.getLogger(__name__)

# Define paths using pathlib
CURRENT_FILE_PATH = Path(__file__).resolve()
PYTHON_DIR = CURRENT_FILE_PATH.parent
ROOT_DIR = (PYTHON_DIR / "..").resolve()
SOURCE_PROMPTS_DIR = ROOT_DIR / "prompts" / "align_to_love"
DEST_PROMPTS_DIR = PYTHON_DIR / "heart_centered_prompts" / "prompts" / "align_to_love"
PROMPT_FILES = ["comprehensive.txt", "standard.txt", "concise.txt", "terse.txt"]


def copy_prompt_files():
    """
    Copies prompt files from the source directory to the destination directory.
    Creates the destination directory if it doesn't exist.
    Logs success or error messages.
    """
    logger.info(f"Source prompts directory: {SOURCE_PROMPTS_DIR}")
    logger.info(f"Destination prompts directory: {DEST_PROMPTS_DIR}")

    if not SOURCE_PROMPTS_DIR.is_dir():
        logger.error(f"Source directory '{SOURCE_PROMPTS_DIR}' not found.")
        logger.error("Please ensure this script runs from 'python' dir & root 'prompts' dir exists.")
        sys.exit(1)

    missing_source_files = False
    for filename in PROMPT_FILES:
        source_file = SOURCE_PROMPTS_DIR / filename
        if not source_file.is_file():
            logger.error(f"Source prompt file '{source_file}' not found.")
            missing_source_files = True

    if missing_source_files:
        logger.error("One or more source prompt files are missing. Please check your repository structure.")
        sys.exit(1)

    # Create destination directory if it doesn't exist
    DEST_PROMPTS_DIR.mkdir(parents=True, exist_ok=True)
    logger.info(f"Ensured destination directory exists: {DEST_PROMPTS_DIR}")

    copied_count = 0
    for filename in PROMPT_FILES:
        source_file = SOURCE_PROMPTS_DIR / filename
        destination_file = DEST_PROMPTS_DIR / filename
        shutil.copy2(source_file, destination_file)
        logger.info(f"Copied '{filename}' to '{DEST_PROMPTS_DIR}'")
        copied_count += 1

    if copied_count == len(PROMPT_FILES):
        logger.info("✅ All prompt files copied successfully.")
    else:
        logger.warning(f"Only {copied_count}/{len(PROMPT_FILES)} prompt files were copied.")
        logger.warning("If you see errors above, please address them.")
        logger.warning(
            f"If prompt files are still missing in '{DEST_PROMPTS_DIR}', you may need to run this script again:"
        )
        logger.warning("  cd python && python copy_prompts.py")
        sys.exit(1)


if __name__ == "__main__":
    # Adjust CWD if script is run from repository root
    # This logic assumes the script is in the 'python' directory.
    if Path.cwd().name != "python":
        # Check if we are in the repository root by looking for the 'python' subdirectory
        prospective_python_dir = Path.cwd() / "python"
        if prospective_python_dir.is_dir() and (prospective_python_dir / CURRENT_FILE_PATH.name).exists():
            logger.info(f"Changing current directory to: {prospective_python_dir}")
            # os.chdir is fine here as Path.cwd() will reflect the change.
            # No direct pathlib equivalent for changing cwd.
            import os

            os.chdir(prospective_python_dir)
        else:
            logger.warning(f"Script is in {PYTHON_DIR}, but CWD is {Path.cwd()}. Paths might be incorrect.")
            logger.warning("Please run from the 'python' directory or the repository root.")

    # Create __init__.py in python/heart_centered_prompts/prompts/ if it doesn't exist
    prompts_init_path = PYTHON_DIR / "heart_centered_prompts" / "prompts" / "__init__.py"
    if not prompts_init_path.exists():
        logger.info(f"Creating missing __init__.py at {prompts_init_path}")
        with prompts_init_path.open("w") as f:
            f.write("# This file makes Python treat the 'prompts' directory as a package.\n")

    # Create __init__.py in python/heart_centered_prompts/prompts/align_to_love/ if it doesn't exist
    align_to_love_init_path = DEST_PROMPTS_DIR / "__init__.py"
    if not align_to_love_init_path.exists():
        logger.info(f"Creating missing __init__.py at {align_to_love_init_path}")
        with align_to_love_init_path.open("w") as f:
            f.write("# This file makes Python treat the 'align_to_love' directory as a package.\n")

    copy_prompt_files()
