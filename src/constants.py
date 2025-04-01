# src/constants.py
"""
Defines constant string values used throughout the Project Chimera game.

This includes UI text, menu options, standard messages, and valid inputs.
Using constants helps maintain consistency and makes updates easier.
"""
from typing import Final, List

# General constants
EXIT_MESSAGE: Final[str] = "\nExiting Project Chimera. Stay vigilant."


class MainMenuStrings:
    """Contains string constants specifically for the main menu."""
    TITLE: Final[str] = "=========================\n   PROJECT CHIMERA\n========================="
    ENTER_TO_CONTINUE: Final[str] = "Please press Enter to continue..."
    MAIN_MENU_TITLE: Final[str] = "\n----- MAIN MENU -----"  # Added spaces for readability
    NEW_GAME: Final[str] = "[N]ew Game"
    LOAD_GAME: Final[str] = "[L]oad Game"
    OPTIONS: Final[str] = "[O]ptions"
    QUIT: Final[str] = "[Q]uit"
    INPUT_REQUEST: Final[str] = "\nPlease enter your selection to continue: "
    
    # List of valid lowercase inputs for the main menu
    PROPER_INPUT_RESPONSES: Final[List[str]] = ['n', 'l', 'o', 'q']
    INVALID_SELECTION: Final[str] = "Your selection is not valid. Please try again."


class OpeningScreenMessages:
    """Contains string constants for the opening scene sequence."""
    INTRO: Final[List[str]] = [
        "// PREMONITION FRAGMENT - SOURCE UNKNOWN - CORRELATION: AGENT ROOK\n\n",
        "You are standing in the sterile white corridor of a high-security",
        "Foundation wing... reinforced door marked... DIRECTOR A. FINCH..",
        "sudden, sharp *crack* echoes from within... sound of something heavy",
        "collapsing... ice-cold dread... override the lock sequence...",
        "\n\n// FRAGMENT END - SIGNAL LOST //"
    ]


class OtherConstants:
    """Contains miscellaneous constants used in the game."""
    SLEEP: Final[float] = 1.0  # Default sleep time in seconds for text pacing


# Logging-related constants
LOGGING_FORMAT: Final[str] = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
LOGGING_DATE_FORMAT: Final[str] = '%Y-%m-%d %H:%M:%S'
LOGGING_FILENAME: Final[str] = 'game.log'
FILEMODE_W: Final[str] = 'w'
LOGGING_START: Final[str] = "Application started."
LOGGING_GAMESTART: Final[str] = "Displaying main menu."
LOGGING_STOP: Final[str] = "Application finished."


class BriefingMessages:
     """Contains messages related to mission briefings."""
     FINCH_MEMO_CHIMERA: Final[str] = """
**MEMORANDUM**

**TO:** Agent Rook
**FROM:** O5 Council Liaison - Director Alistair Finch
**DATE:** 18/07/20██
**SUBJECT:** Project Chimera - Urgent Operational Mandate

Agent,

You are being assigned lead operational role for **Project Chimera**. 
This initiative concerns the recent, highly irregular death of Dr. Aris Thorne, formerly of Site-19's Parazoology Division. 
Thorne was found deceased in his off-site residence under circumstances exhibiting anomalous influence. 
Standard memetic/cognitohazard screening protocols are in effect for all personnel involved.

Thorne left behind fragmented research materials referencing the ill-fated **"Obsidian Gate Expedition"** (OGE) conducted in 1998.
The OGE officially concluded with the loss of several personnel and the containment of a minor spatial anomaly (SCP-████ - designation pending review). 
Thorne was a junior researcher attached to the support team.

His final, corrupted data fragments suggest the OGE encountered something far more significant than 
reported – a nexus of anomalous activity potentially linked to an unclassified, 
multifaceted hostile entity or Group of Interest (GoI-███ - designation "The Sculptors of Misery"). 
Thorne's research indicates this entity's influence is not localized and may be connected to several recent,
seemingly disparate anomalous incidents across multiple continents.

Your primary objective is to investigate Thorne's death, 
reconstruct his final research, and follow the trail originating from the OGE. 
You will assess the nature and extent of the threat posed by GoI-███ and its potential connection to the OGE findings. 
This investigation will likely require deployment to multiple international Foundation facilities and potentially unsecured locations.

Failure is not an option.
The preliminary threat assessment suggests a potential K-Class Scenario if GoI-███'s objectives are realized.
Proceed with extreme caution. 
Further directives will follow based on your initial findings at Thorne's residence.

**Secure. Contain. Protect.**
"""
# Adjust internal spacing/newlines as needed for desired console output.