# src/opening_scene.py
"""
Handles the display of the game's introductory opening scene sequence.
"""

import os
import time
import logging # Import the logging module

# Import constants from the local package
from src.constants import OpeningScreenMessages, OtherConstants

# Get a logger instance for this module
logger = logging.getLogger(__name__)


def opening_scene_start():
    """
    Displays the opening scene text line by line with a timed delay.
    """
    logger.info("Starting opening scene display.")

    # Iterate through the list of intro messages defined in constants
    for line in OpeningScreenMessages.INTRO:
        print(line)
        # Pause execution briefly between lines for dramatic effect
        # logger.debug(f"Displayed line: {line.strip()[:30]}...") # Optional: Log each line (can be verbose)
        time.sleep(OtherConstants.SLEEP)

    logger.info("Opening scene display complete.")

    # Placeholder for what happens after the intro text finishes
    # print("\nOpening scene complete.") # Example placeholder - logging replaces this need for debugging