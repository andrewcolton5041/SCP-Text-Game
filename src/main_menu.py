# src/main_menu.py
"""
Handles the display and interaction for the game's main menu.

Uses string constants defined in src.constants for display text.
Provides options for starting, loading, options, or quitting the game.
"""

import os
import logging # Import the logging module
import src.utilities as utilities
import src.main_game as main_game

# Import constants from the constants module within the same package
from src.constants import MainMenuStrings, EXIT_MESSAGE

# Get a logger instance for this module
logger = logging.getLogger(__name__)

def display_main_menu():
    """
    Displays the game title, waits for user confirmation, then shows the
    main menu options. Loops until valid input is received, then acts on
    the input or quits the application.
    """
    logger.debug("Clearing screen for title display.")
    utilities.clear_screen()
    print(MainMenuStrings.TITLE)
    print(MainMenuStrings.ENTER_TO_CONTINUE)
    input()  # Wait for user to press Enter
    logger.info("Title screen acknowledged by user.")

    # Main menu loop
    while True:
        logger.debug("Clearing screen for main menu display.")
        utilities.clear_screen()
        # Display menu options
        print(MainMenuStrings.MAIN_MENU_TITLE)
        print(MainMenuStrings.NEW_GAME)
        print(MainMenuStrings.LOAD_GAME)
        print(MainMenuStrings.OPTIONS)
        print(MainMenuStrings.QUIT)
        print()  # Add a blank line for spacing
        logger.info("Main menu displayed.")

        # Input validation loop
        while True:
            selection = input(MainMenuStrings.INPUT_REQUEST)
            logger.debug(f"User input received: '{selection}'") # Log raw input
            selection_lower = selection.lower()  # Convert to lowercase once

            # Check if the input is one of the allowed responses
            if selection_lower not in MainMenuStrings.PROPER_INPUT_RESPONSES:
                logger.warning(f"Invalid menu selection: '{selection}'") # Log invalid input
                print(MainMenuStrings.INVALID_SELECTION)
                input("Press Enter to try again...") # Pause for user feedback
                # Re-draw the menu after invalid input message
                logger.debug("Re-drawing main menu after invalid input.")
                utilities.clear_screen()
                print(MainMenuStrings.MAIN_MENU_TITLE)
                print(MainMenuStrings.NEW_GAME)
                print(MainMenuStrings.LOAD_GAME)
                print(MainMenuStrings.OPTIONS)
                print(MainMenuStrings.QUIT)
                print()
            else:
                logger.info(f"Valid menu selection: '{selection_lower}'") # Log valid input
                break  # Exit input validation loop when input is valid

        # Handle the valid selection
        if selection_lower == 'q':
            logger.info("User selected Quit.")
            utilities.clear_screen()
            print(EXIT_MESSAGE)  # Use the imported constant
            break  # Exit the main menu loop

        elif selection_lower == 'n':
            logger.info("User selected New Game.")
            utilities.clear_screen()
            print("\nStarting New Game...") # Keep user-facing message
            # TODO: Add call to the function that starts a new game
            main_game.start_new_game() # This function will log its own start
            input("Press Enter to return to menu...")  # Pause for user
            logger.debug("Returned to main menu after New Game attempt.")

        elif selection_lower == 'l':
            logger.info("User selected Load Game.")
            utilities.clear_screen()
            print("\nLoading Game... (Not implemented yet)")
            # TODO: Add call to the function that loads a saved game
            input("Press Enter to return to menu...")
            logger.debug("Returned to main menu after Load Game attempt.")


        elif selection_lower == 'o':
            logger.info("User selected Options.")
            utilities.clear_screen()
            print("\nOpening Options... (Not implemented yet)")
            # TODO: Add call to the function that shows the options screen
            input("Press Enter to return to menu...")
            logger.debug("Returned to main menu after Options attempt.")


# This block allows testing this module directly if needed
# Note: Running this directly might have issues with the relative import '.'
# unless run as a module (e.g., python -m src.main_menu)
# Also, logging won't be configured if run directly unless added here.
if __name__ == "__main__":
    # Simple mock for testing if constants aren't easily available
    class MockMainMenuStrings:
        TITLE = "== MOCK TITLE =="
        ENTER_TO_CONTINUE = "Press Enter..."
        MAIN_MENU_TITLE = "-- Mock Menu --"
        NEW_GAME = "[N] New"
        LOAD_GAME = "[L] Load"
        OPTIONS = "[O] Options"
        QUIT = "[Q] Quit"
        INPUT_REQUEST = "> "
        PROPER_INPUT_RESPONSES = ['n', 'l', 'o', 'q']
        INVALID_SELECTION = "Invalid."

    EXIT_MESSAGE = "Exiting Mock."

    # Override imported constants with mocks for isolated testing
    MainMenuStrings = MockMainMenuStrings
    # EXIT_MESSAGE is already defined locally here

    # Basic logging setup JUST for direct testing of this module
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(name)s - %(message)s')
    logger.info("Testing main_menu.py directly...") # Use the logger defined above

    display_main_menu()
    logger.info("Main menu test complete.") # Use the logger