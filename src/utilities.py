# src/utilities.py
"""
Provides utility functions used across the Project Chimera game,
such as clearing the terminal screen.
"""

import os
import logging # Import the logging module

# Get a logger instance for this module
logger = logging.getLogger(__name__)

def clear_screen():
    """Clears the terminal screen based on the operating system."""
    logger.debug(f"Clearing screen (os.name: {os.name}).") # Log the attempt
    # Uses 'cls' for Windows (nt) and 'clear' for Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')