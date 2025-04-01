# src/opening_scene.py
"""
Handles the display of the opening premonition scene.
"""
import logging
from typing import NoReturn, Optional

from .constants import OpeningScreenMessages
from . import utilities

# Configure logger for this module
logger: logging.Logger = logging.getLogger(__name__)

def opening_scene_start() -> None:
    """
    Displays the opening scene text sequentially using the utility function.
    
    Logs the start and completion of the opening scene display.
    """
    logger.info("Starting opening scene display.")
    
    try:
        # Use the utility function to display text sequentially
        utilities.display_text_sequentially(OpeningScreenMessages.INTRO)
        logger.info("Opening scene display complete.")
    except Exception as e:
        logger.error(f"Error during opening scene display: {e}", exc_info=True)
        raise