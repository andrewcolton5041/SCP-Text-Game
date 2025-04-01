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


class OpeningScreenMessages:
    """Contains string constants for the opening scene sequence."""
    INTRO = [
        "// PREMONITION FRAGMENT - SOURCE UNKNOWN - CORRELATION: AGENT ROOK\n\n",
        "You are standing in the sterile white corridor of a high-security",
        "Foundation wing... reinforced door marked... DIRECTOR A. FINCH..",
        "sudden, sharp *crack* echoes from within... sound of something heavy",
        "collapsing... ice-cold dread... override the lock sequence...",
        "\n\n// FRAGMENT END - SIGNAL LOST //"
    ]


class OtherConstants:
    """Contains miscellaneous constants used in the game."""
    SLEEP = 1 # Default sleep time in seconds for text pacing
    
LOGGING_FORMAT = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
LOGGING_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
LOGGING_FILENAME = 'game.log'
FILEMODE_W = 'w'
LOGGING_START = "Application started."
LOGGING_GAMESTART = "Displaying main menu."
LOGGING_STOP = "Application finished."