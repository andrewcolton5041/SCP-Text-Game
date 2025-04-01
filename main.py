# main.py
"""
Main entry point for the SCP Text Adventure Game.
Sets up logging and starts the main menu.
"""
import logging
from src.main_menu import display_main_menu  # Import the specific function

# --- Logging Configuration ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)

# --- Main Function ---
def main() -> None:
    """
    Sets up the game environment and starts the main menu.
    """
    logger.info("=================================================")
    logger.info("      Project Chimera - Game Initializing      ")
    logger.info("=================================================")
    # Add any initial setup steps here
    logger.debug("Initial setup complete. Displaying main menu.")
    display_main_menu()  # Use the directly imported function
    logger.info("=================================================")
    logger.info("      Project Chimera - Game Exited            ")
    logger.info("=================================================")

# --- Execution Guard ---
if __name__ == "__main__":
    main()