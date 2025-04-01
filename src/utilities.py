# src/utilities.py
"""
Provides utility functions used across the Project Chimera game,
such as clearing the terminal screen.
"""

import os
import logging # Import the logging module
import time
from src.constants import OtherConstants

# Get a logger instance for this module
logger = logging.getLogger(__name__)

def clear_screen():
    """Clears the terminal screen based on the operating system."""
    logger.debug(f"Clearing screen (os.name: {os.name}).") # Log the attempt
    # Uses 'cls' for Windows (nt) and 'clear' for Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')
    
def display_text_sequentially(text_data, delay=None):
    """
    Displays text line by line with a delay between each line.

    Args:
        text_data: Either a list of strings or a single multi-line string.
        delay (float, optional): Seconds to pause between lines.
                                 Defaults to OtherConstants.SLEEP.
    """
    if delay is None:
        delay = OtherConstants.SLEEP

    lines = []
    if isinstance(text_data, str):
        # Split multi-line string into lines, preserving empty lines
        lines = text_data.splitlines()
    elif isinstance(text_data, list):
        lines = text_data
    else:
        logger.error(f"Unsupported text_data type for sequential display: {type(text_data)}")
        print(f"[Error: Cannot display text of type {type(text_data)} sequentially]")
        return # Or raise an error

    logger.debug(f"Displaying {len(lines)} lines sequentially with delay {delay}s.")
    for line in lines:
        print(line)
        try:
            time.sleep(delay)
        except InterruptedError:
            logger.warning("Sequential display sleep interrupted.")
            break # Exit loop if sleep is interrupted
    logger.debug("Sequential display complete.")