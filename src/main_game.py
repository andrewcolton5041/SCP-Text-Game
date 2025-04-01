# src/main_game.py
"""
Contains the core logic for starting and running a new game session.
"""
import logging
from typing import Optional, Dict, Any

import src.utilities as utilities
import src.opening_scene as opening_scene
from src.constants import BriefingMessages
from src.enums import (
    GameState as GameStateEnum, 
    InteractionState, 
    CharacterState, 
    MentalState
)
from src.models import (
    Character, 
    GameState as GameStateModel, 
    Location
)

# Configure logger for this module
logger: logging.Logger = logging.getLogger(__name__)


class GameSession:
    """
    Manages a single game session, including state transitions and the main game loop.
    Centralizes game state management and control flow.
    """
    
    def __init__(self) -> None:
        """Initialize a new game session with default states."""
        self.game_state: Optional[GameStateModel] = None
        self.current_state: GameStateEnum = GameStateEnum.INITIALIZING
        self.interaction_state: InteractionState = InteractionState.EXPLORATION
        logger.info("Game session initialized with state %s", self.current_state)
    
    def transition_to(self, new_state: GameStateEnum) -> None:
        """
        Transition to a new game state.
        
        Args:
            new_state (GameStateEnum): The new state to transition to.
        """
        logger.info("Game state transition: %s -> %s", self.current_state, new_state)
        old_state: GameStateEnum = self.current_state
        self.current_state = new_state
        
        # Update game_state object if it exists
        if self.game_state:
            self.game_state.current_game_state = new_state
        
        # Handle state-specific transitions
        if new_state == GameStateEnum.NEW_GAME:
            self._initialize_new_game()
        elif new_state == GameStateEnum.PLAYING:
            if old_state == GameStateEnum.NEW_GAME:
                self._start_gameplay()
    
    def set_interaction_state(self, new_interaction_state: InteractionState) -> None:
        """
        Set the current interaction mode.
        
        Args:
            new_interaction_state (InteractionState): The new interaction state.
        """
        logger.info(
            "Interaction mode changed: %s -> %s", 
            self.interaction_state, 
            new_interaction_state
        )
        self.interaction_state = new_interaction_state
        
        # Update game_state object if it exists
        if self.game_state:
            self.game_state.current_interaction_state = new_interaction_state
    
    def _initialize_new_game(self) -> None:
        """Initialize a new game with default player and starting location."""
        # Create player character
        player: Character = Character(name="Agent Rook", age=34)
        
        # Create initial game state
        self.game_state = GameStateModel(
            player=player,
            current_location="thorne_residence",  # Starting location
        )
        
        # Add starting location
        start_location: Location = Location(
            name="Dr. Thorne's Residence",
            description="A modest apartment showing signs of a struggle."
        )
        self.game_state.locations["thorne_residence"] = start_location
        
        logger.info("New game initialized with player %s", player.name)
    
    def _start_gameplay(self) -> None:
        """Transition from setup to active gameplay."""
        # Any additional setup needed before gameplay starts
        self.set_interaction_state(InteractionState.EXPLORATION)
    
    def main_game_loop(self) -> None:
        """Run the main game loop based on current state."""
        logger.info("Entering main game loop in state %s", self.current_state)
        
        # Keep running until game ends
        while self.current_state not in (GameStateEnum.GAME_OVER, GameStateEnum.QUITTING):
            if self.current_state == GameStateEnum.PLAYING:
                self._handle_playing_state()
            elif self.current_state == GameStateEnum.DIALOGUE:
                self._handle_dialogue_state()
            elif self.current_state == GameStateEnum.COMBAT:
                self._handle_combat_state()
            elif self.current_state == GameStateEnum.PAUSED:
                self._handle_paused_state()
            else:
                # Unhandled state, break to avoid infinite loop
                logger.error("Unhandled game state: %s", self.current_state)
                break
    
    def _handle_playing_state(self) -> None:
        """Handle the main PLAYING state logic."""
        # Placeholder for game command parsing
        command: str = input("\nWhat would you like to do? ")
        logger.debug("Player input: %s", command)
        
        # Simple command parsing placeholder
        if command.lower() in ("quit", "exit"):
            self.transition_to(GameStateEnum.QUITTING)
        else:
            print("Command not implemented yet.")
    
    def _handle_dialogue_state(self) -> None:
        """Handle dialogue interaction state."""
        print("Dialogue system not implemented yet.")
        self.transition_to(GameStateEnum.PLAYING)
    
    def _handle_combat_state(self) -> None:
        """Handle combat interaction state."""
        print("Combat system not implemented yet.")
        self.transition_to(GameStateEnum.PLAYING)
    
    def _handle_paused_state(self) -> None:
        """Handle game paused state."""
        print("\nGame is paused. Resume or quit?")
        choice: str = input("[R]esume or [Q]uit: ").lower()
        
        if choice.startswith("r"):
            self.transition_to(GameStateEnum.PLAYING)
        elif choice.startswith("q"):
            self.transition_to(GameStateEnum.QUITTING)


# Global game session instance
_game_session: Optional[GameSession] = None


def start_new_game() -> GameStateEnum:
    """
    Initiates the sequence for starting a new game.
    
    Returns:
        GameStateEnum: The final state of the game after startup sequence.
    """
    global _game_session
    logger.info("New game selected. Starting sequence.")
    
    # Create new game session
    _game_session = GameSession()
    
    # 1. Transition to NEW_GAME state
    _game_session.transition_to(GameStateEnum.NEW_GAME)
    
    # 2. Display the premonition
    opening_scene.opening_scene_start()
    logger.info("Opening scene/premonition display complete.")
    
    # 3. Clear screen for briefing
    logger.debug("Clearing screen for briefing memo.")
    utilities.clear_screen()
    
    # 4. Display the briefing memo sequentially
    logger.info("Displaying Finch briefing memo sequentially.")
    utilities.display_text_sequentially(BriefingMessages.FINCH_MEMO_CHIMERA)
    
    # 5. Pause for player acknowledgement
    input("\nPress Enter to acknowledge briefing...")
    logger.info("Briefing acknowledged by player.")
    
    # 6. Transition to active gameplay state
    _game_session.transition_to(GameStateEnum.PLAYING)
    
    print("[DEBUG: Proceeding to Thorne's residence - To be implemented]")
    
    # 7. Start the main game loop
    try:
        _game_session.main_game_loop()
    except Exception as e:
        logger.error("Error in main game loop: %s", e, exc_info=True)
        print(f"\nAn error occurred: {e}")
    
    logger.info("Game session ended.")
    return _game_session.current_state