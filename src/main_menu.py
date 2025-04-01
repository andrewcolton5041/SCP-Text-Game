# src/main_menu.py
"""
Handles the display and interaction for the game's main menu.
"""
import logging
import src.utilities as utilities
import src.main_game as main_game
from src.constants import MainMenuStrings, EXIT_MESSAGE
from src.enums import GameState as GameStateEnum

logger = logging.getLogger(__name__)


class MainMenu:
    """
    Manages the main menu display and interaction.
    Uses enum-based state management for menu navigation.
    """

    def __init__(self):
        """Initialize the main menu with default state."""
        self.current_state = GameStateEnum.MAIN_MENU
        logger.debug("MainMenu initialized in state %s", self.current_state)

    def display_title_screen(self):
        """Display the game title and wait for acknowledgement."""
        logger.debug("Clearing screen for title display.")
        utilities.clear_screen()
        print(MainMenuStrings.TITLE)
        print(MainMenuStrings.ENTER_TO_CONTINUE)
        input()  # Wait for any key
        logger.info("Title screen acknowledged by user.")

    def display_menu_options(self):
        """Display the main menu options."""
        print(MainMenuStrings.MAIN_MENU_TITLE)
        print(MainMenuStrings.NEW_GAME)
        print(MainMenuStrings.LOAD_GAME)
        print(MainMenuStrings.OPTIONS)
        print(MainMenuStrings.QUIT)
        print()  # Add a blank line for spacing

    def get_valid_menu_input(self):
        """
        Prompt for and validate user menu selection.

        Returns:
            str: The validated lowercase user selection.
        """
        while True:
            selection = input(MainMenuStrings.INPUT_REQUEST)
            logger.debug("User input received: '%s'", selection)
            selection_lower = selection.lower()

            if selection_lower not in MainMenuStrings.PROPER_INPUT_RESPONSES:
                logger.warning("Invalid menu selection: '%s'", selection)
                print(MainMenuStrings.INVALID_SELECTION)
                input("Press Enter to try again...")
                # Re-draw the menu after invalid input message
                logger.debug("Re-drawing main menu after invalid input.")
                utilities.clear_screen()
                self.display_menu_options()
            else:
                logger.info("Valid menu selection: '%s'", selection_lower)
                return selection_lower  # Return the valid input

    def handle_menu_selection(self, selection):
        """
        Handle a validated menu selection.

        Args:
            selection (str): The user's menu selection.

        Returns:
            bool: True if menu should continue, False if should exit.
        """
        if selection == 'q':
            logger.info("User selected Quit.")
            utilities.clear_screen()
            print(EXIT_MESSAGE)
            self.current_state = GameStateEnum.QUITTING  # Fixed: GameState -> GameStateEnum
            return False  # Exit the menu loop

        elif selection == 'n':
            logger.info("User selected New Game.")
            utilities.clear_screen()
            print("\nStarting New Game...")
            self.current_state = GameStateEnum.NEW_GAME  # Fixed: GameState -> GameStateEnum
            # Start new game and get final state
            final_state = main_game.start_new_game()
            # Record the state for potential future use
            self.current_state = final_state
            input("Press Enter to return to menu...")
            logger.debug("Returned to main menu after New Game.")
            self.current_state = GameStateEnum.MAIN_MENU  # Fixed: GameState -> GameStateEnum
            return True  # Continue the menu loop

        elif selection == 'l':
            logger.info("User selected Load Game.")
            utilities.clear_screen()
            print("\nLoading Game... (Not implemented yet)")
            input("Press Enter to return to menu...")
            logger.debug("Returned to main menu after Load Game attempt.")
            return True  # Continue the menu loop

        elif selection == 'o':
            logger.info("User selected Options.")
            utilities.clear_screen()
            print("\nOpening Options... (Not implemented yet)")
            input("Press Enter to return to menu...")
            logger.debug("Returned to main menu after Options attempt.")
            return True  # Continue the menu loop

        # Should never reach here due to input validation
        return True


def display_main_menu():
    """
    Display and handle the main menu until user quits.
    Entry point for the main menu system.
    """
    menu = MainMenu()
    menu.display_title_screen()

    # Main menu loop
    continue_menu = True
    while continue_menu:
        logger.debug("Clearing screen for main menu display.")
        utilities.clear_screen()
        menu.display_menu_options()
        logger.info("Main menu displayed.")

        selection = menu.get_valid_menu_input()
        continue_menu = menu.handle_menu_selection(selection)

    logger.info("Exited main menu with state %s", menu.current_state)
    return menu.current_state