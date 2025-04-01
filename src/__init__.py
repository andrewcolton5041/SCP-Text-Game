# src/__init__.py
"""
Initialization file for the src package.
"""

# Import and expose the main functions
from .main_menu import display_main_menu
from .main_game import start_new_game
from .opening_scene import opening_scene_start

# This makes these functions available when importing from src
__all__ = ['display_main_menu', 'start_new_game', 'opening_scene_start']