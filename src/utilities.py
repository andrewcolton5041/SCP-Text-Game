# src/utilities.py
"""
General utility functions for the game.
"""
import time
import logging
import os
import platform
from typing import List, Optional, Union # Added typing imports

from .constants import OtherConstants # Assuming OtherConstants has SLEEP

logger = logging.getLogger(__name__)

def clear_screen() -> None:
    """Clears the terminal screen."""
    system_platform = platform.system()
    if system_platform == "Windows":
        os.system('cls')
    else:
        # Assume Linux, macOS, or other POSIX-compliant systems
        os.system('clear')
    logger.debug(f"Screen cleared on platform: {system_platform}")

def display_text_sequentially(
    text_data: Union[str, List[str]],
    delay: Optional[float] = None
) -> None:
    """
    Displays text line by line with a delay between each line.

    Args:
        text_data: Either a list of strings or a single multi-line string.
        delay (Optional[float]): Seconds to pause between lines.
                                 Defaults to OtherConstants.SLEEP.
    """
    if delay is None:
        delay = OtherConstants.SLEEP

    lines: List[str] = []
    if isinstance(text_data, str):
        # Split multi-line string into lines, preserving empty lines
        lines = text_data.splitlines()
    elif isinstance(text_data, list):
        lines = text_data
    else:
        logger.error(
            f"Unsupported text_data type for sequential display: {type(text_data)}"
        )
        # Using type ignore as print is untyped, consider logging or raising error
        print(f"[Error: Cannot display text of type {type(text_data)} sequentially]") # type: ignore
        return # Or raise an error

    logger.debug(f"Displaying {len(lines)} lines sequentially with delay {delay}s.")
    for line in lines:
        print(line) # type: ignore # print is untyped
        try:
            time.sleep(delay)
        except InterruptedError:
            logger.warning("Sequential display sleep interrupted.")
            # Optionally re-raise or handle differently
            break # Exit loop if sleep is interrupted
    logger.debug("Sequential display complete.")
