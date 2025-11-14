"""File utility functions."""

import os
import re


def ensure_directory_exists(directory: str) -> str:
    """Ensure a directory exists, create if it doesn't.
    
    Args:
        directory: Path to the directory
        
    Returns:
        Absolute path to the directory
    """
    os.makedirs(directory, exist_ok=True)
    return os.path.abspath(directory)


def clean_filename(text: str, max_length: int = 50) -> str:
    """Clean text to be used as a filename.
    
    Args:
        text: Text to clean
        max_length: Maximum length of filename
        
    Returns:
        Cleaned filename-safe string
    """
    # Remove special characters
    cleaned = re.sub(r'[^\w\s-]', '', text)
    # Replace spaces with underscores
    cleaned = cleaned.strip().replace(' ', '_')
    # Limit length
    return cleaned[:max_length]

