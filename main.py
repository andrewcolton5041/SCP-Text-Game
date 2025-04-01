# main.py
"""
Main entry point for the SCP Text Adventure Game.
Sets up logging and starts the main menu.
"""
import logging
import sys
from typing import Optional

from src.main_menu import display_main_menu  # Import the specific function
from src.enums import GameState

# --- Logging Configuration ---
def configure_logging() -> None:
    """
    Configure logging for the application.
    
    Sets up logging with a standard format and INFO level logging.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

# --- Main Function ---
def main() -> Optional[int]:
    """
    Sets up the game environment and starts the main menu.
    
    Returns:
        Optional[int]: Exit code (None for successful exit, or error code)
    """
    try:
        # Configure logging
        configure_logging()
        
        # Get logger for this module
        logger = logging.getLogger(__name__)
        
        # Log game initialization
        logger.info("=================================================")
        logger.info("      Project Chimera - Game Initializing      ")
        logger.info("=================================================")
        
        # Add any initial setup steps here
        logger.debug("Initial setup complete. Displaying main menu.")
        
        # Display main menu and get final game state
        final_state: GameState = display_main_menu()
        
        # Log game exit
        logger.info("=================================================")
        logger.info("      Project Chimera - Game Exited            ")
        logger.info("=================================================")
        
        return 0  # Successful exit
    
    except Exception as e:
        # Log any unexpected errors
        logging.error(f"Unexpected error occurred: {e}", exc_info=True)
        return 1  # Error exit code

# --- Execution Guard ---
if __name__ == "__main__":
    sys.exit(main() or 0)