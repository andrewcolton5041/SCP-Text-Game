# src/opening_scene.py
"""
Handles the display of the game's introductory opening scene sequence.
"""

import logging
from .constants import OpeningScreenMessages # Keep constants import
from . import utilities # Import utilities module

logger = logging.getLogger(__name__)

def opening_scene_start():
    """
    Displays the opening scene text sequentially using the utility function.
    """
    logger.info("Starting opening scene display.")
    # Use the utility function now
    utilities.display_text_sequentially(OpeningScreenMessages.INTRO)
    logger.info("Opening scene display complete.")

    # Placeholder for what happens after the intro text finishes
    # print("\nOpening scene complete.") # Example placeholder - logging replaces this need for debugging