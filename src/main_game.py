# Modify src/main_game.py

# Modify src/main_game.py
import src.utilities as utilities # Keep this import
import src.opening_scene as opening_scene # Keep this import
from src.constants import BriefingMessages # Keep this import
import logging

logger = logging.getLogger(__name__)

def start_new_game():
    """Initiates the sequence for starting a new game."""
    logger.info("New game selected. Starting sequence.")

    # 1. Display the premonition (Calls the refactored function)
    opening_scene.opening_scene_start()
    logger.info("Opening scene/premonition display complete.")

    # --- Transition happens here ---

    # 2. Clear screen for briefing
    logger.debug("Clearing screen for briefing memo.")
    utilities.clear_screen()

    # 3. Display the briefing memo sequentially
    logger.info("Displaying Finch briefing memo sequentially.")
    # Use the utility function instead of print()
    utilities.display_text_sequentially(BriefingMessages.FINCH_MEMO_CHIMERA)

    # 4. Pause for player acknowledgement
    input("\nPress Enter to acknowledge briefing...")
    logger.info("Briefing acknowledged by player.")

    # --- What happens next? ---
    logger.debug("Proceeding to first interactive scene (Not implemented yet).")
    print("\n[DEBUG: Proceeding to Thorne's residence - To be implemented]")