# src/constants.py
"""
Defines constant string values used throughout the Project Chimera game.

This includes UI text, menu options, standard messages, and valid inputs.
Using constants helps maintain consistency and makes updates easier.
"""

# General constants
EXIT_MESSAGE = "\nExiting Project Chimera. Stay vigilant."


class MainMenuStrings:
    """Contains string constants specifically for the main menu."""
    TITLE = "=========================\n   PROJECT CHIMERA\n========================="
    ENTER_TO_CONTINUE = "Please press Enter to continue..."
    MAIN_MENU_TITLE = "\n----- MAIN MENU -----"  # Added spaces for readability
    NEW_GAME = "[N]ew Game"
    LOAD_GAME = "[L]oad Game"
    OPTIONS = "[O]ptions"
    QUIT = "[Q]uit"
    INPUT_REQUEST = "\nPlease enter your selection to continue: "
    # List of valid lowercase inputs for the main menu
    PROPER_INPUT_RESPONSES = ['n', 'l', 'o', 'q']
    INVALID_SELECTION = "Your selection is not valid. Please try again."

# You might add other classes here for different parts of the game later, e.g.:
# class GameMessages:
#     SAVE_SUCCESS = "Game saved successfully."
#     LOAD_FAILED = "Failed to load save file."
