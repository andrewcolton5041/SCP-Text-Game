# main.py
"""
Main entry point for the SCP Text Adventure Game.
Sets up logging and starts the main menu.
"""
import logging
import src.main_menu as main_menu
# Import other necessary modules like configuration loaders if added later

# --- Logging Configuration ---
# Basic configuration, can be expanded later (e.g., file logging)
logging.basicConfig(
    level=logging.INFO, # Set default level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
# You might want to set different levels for different modules later
# logging.getLogger('src.some_noisy_module').setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# --- Main Function ---
def main() -> None:
    """
    Sets up the game environment and starts the main menu.
    """
    logger.info("=================================================")
    logger.info("      Project Chimera - Game Initializing      ")
    logger.info("=================================================")
    # Add any initial setup steps here (e.g., loading config, checking files)
    logger.debug("Initial setup complete. Displaying main menu.")
    main_menu.display_main_menu()
    logger.info("=================================================")
    logger.info("      Project Chimera - Game Exited            ")
    logger.info("=================================================")

# --- Execution Guard ---
if __name__ == "__main__":
    main()
