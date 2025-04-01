# src/__init__.py
"""
Initialization file for the src package.
"""
from typing import Callable, Any

from .main_menu import display_main_menu
from .main_game import start_new_game
from .opening_scene import opening_scene_start

# This makes these functions available when importing from src
__all__: list[str] = ['display_main_menu', 'start_new_game', 'opening_scene_start']

# Explicitly type the exposed functions for better type checking
display_main_menu: Callable[[], Any] = display_main_menu
start_new_game: Callable[[], Any] = start_new_game
opening_scene_start: Callable[[], None] = opening_scene_start