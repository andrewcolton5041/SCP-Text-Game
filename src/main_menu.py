# src/main_menu.py
"""
Handles the display and interaction for the game's main menu.
"""
import logging
import src.utilities as utilities
import src.main_game as main_game
from src.constants import MainMenuStrings, EXIT_MESSAGE

logger = logging.getLogger(__name__)

# --- Helper Functions ---

def _print_menu_options():
    """Prints the main menu options to the console."""
    print(MainMenuStrings.MAIN_MENU_TITLE)
    print(MainMenuStrings.NEW_GAME)
    print(MainMenuStrings.LOAD_GAME)
    print(MainMenuStrings.OPTIONS)
    print(MainMenuStrings.QUIT)
    print()  # Add a blank line for spacing

def _get_valid_menu_input() -> str:
    """
    Prompts the user for input and validates it against allowed menu options.

    Loops until valid input ('n', 'l', 'o', 'q') is received.

    Returns:
        str: The validated lowercase user selection.
    """
    while True:
        selection = input(MainMenuStrings.INPUT_REQUEST)
        logger.debug(f"User input received: '{selection}'")
        selection_lower = selection.lower()

        if selection_lower not in MainMenuStrings.PROPER_INPUT_RESPONSES:
            logger.warning(f"Invalid menu selection: '{selection}'")
            print(MainMenuStrings.INVALID_SELECTION)
            input("Press Enter to try again...")
            # Re-draw the menu after invalid input message
            logger.debug("Re-drawing main menu after invalid input.")
            utilities.clear_screen()
            _print_menu_options() # Call helper to reprint
        else:
            logger.info(f"Valid menu selection: '{selection_lower}'")
            return selection_lower # Return the valid input

# --- Main Menu Function (Refactored) ---

def display_main_menu():
    """
    Displays the game title, waits, then shows and handles the main menu.
    """
    logger.debug("Clearing screen for title display.")
    utilities.clear_screen()
    print(MainMenuStrings.TITLE)
    print(MainMenuStrings.ENTER_TO_CONTINUE)
    input()
    logger.info("Title screen acknowledged by user.")

    # Main menu loop
    while True:
        logger.debug("Clearing screen for main menu display.")
        utilities.clear_screen()
        _print_menu_options() # Use helper to print
        logger.info("Main menu displayed.")

        selection = _get_valid_menu_input() # Use helper to get valid input

        # Handle the valid selection
        if selection == 'q':
            logger.info("User selected Quit.")
            utilities.clear_screen()
            print(EXIT_MESSAGE)
            break # Exit the main menu loop

        elif selection == 'n':
            logger.info("User selected New Game.")
            utilities.clear_screen()
            print("\nStarting New Game...")
            main_game.start_new_game()
            input("Press Enter to return to menu...")
            logger.debug("Returned to main menu after New Game attempt.")

        elif selection == 'l':
            logger.info("User selected Load Game.")
            utilities.clear_screen()
            print("\nLoading Game... (Not implemented yet)")
            input("Press Enter to return to menu...")
            logger.debug("Returned to main menu after Load Game attempt.")

        elif selection == 'o':
            logger.info("User selected Options.")
            utilities.clear_screen()
            print("\nOpening Options... (Not implemented yet)")
            input("Press Enter to return to menu...")
            logger.debug("Returned to main menu after Options attempt.")

# --- (Keep the __main__ block if needed for direct testing) ---
# Note: The __main__ block might need adjustments if it relied on the old structure.