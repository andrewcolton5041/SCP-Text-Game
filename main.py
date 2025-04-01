# main.py
"""
Main entry point for the SCP Text Adventure Game.
Sets up logging and starts the main menu.
"""
import logging
import sys
from typing import Optional, Callable, Union, Type, TypeVar

from src.main_menu import display_main_menu
from src.enums import GameState

# Type variable for return type of menu function
T = TypeVar('T', bound=GameState)

# --- Logging Configuration ---
def configure_logging() -> None:
    """
    Configure logging for the application.
    
    Sets up logging with a standard format and INFO level logging.
    Configures basic logging with predefined format and date format.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

# --- Main Function ---
def main(
    menu_func: Optional[Callable[[], GameState]] = None, 
    log_config_func: Optional[Callable[[], None]] = None
) -> int:
    """
    Sets up the game environment and starts the main menu.
    
    Args:
        menu_func (Optional[Callable[[], GameState]], optional): 
            Function to display main menu. Defaults to display_main_menu.
        log_config_func (Optional[Callable[[], None]], optional): 
            Function to configure logging. Defaults to configure_logging.
    
    Returns:
        int: Exit code (0 for successful exit, 1 for error)
    """
    try:
        # Use provided or default logging configuration
        if log_config_func is None:
            log_config_func = configure_logging
        log_config_func()
        
        # Get logger for this module
        logger: logging.Logger = logging.getLogger(__name__)
        
        # Log game initialization
        logger.info("=================================================")
        logger.info("      Project Chimera - Game Initializing      ")
        logger.info("=================================================")
        
        # Add any initial setup steps here
        logger.debug("Initial setup complete. Displaying main menu.")
        
        # Use provided or default menu display function
        if menu_func is None:
            menu_func = display_main_menu
        
        # Display main menu and get final game state
        final_state: GameState = menu_func()
        
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