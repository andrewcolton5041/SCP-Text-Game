# src/main_game.py
"""
Handles the core game logic after the main menu, such as starting a new game.
"""

import src.utilities
import src.opening_scene

def start_new_game():
    """Initiates the sequence for starting a new game."""
    # Call the function to display the opening scene
    src.opening_scene.opening_scene_start()
    # Placeholder for further game initialization or first scene
    # print("New game started...") # Example placeholder