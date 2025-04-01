# tests/test_main_game.py
"""
Unit tests for the main game logic in src/main_game.py.
"""

import time
import pytest

# Modules involved in the test
from src import main_game
from src import opening_scene
from src.constants import GameMessages # Import the constant we expect to be printed

# Keep track of whether the mocked function was called
mock_opening_scene_called = False

def dummy_opening_scene_start():
    """A dummy function to replace opening_scene.opening_scene_start."""
    global mock_opening_scene_called
    mock_opening_scene_called = True
    # print("Dummy opening_scene_start called") # Optional debug print

def dummy_sleep(seconds):
    """A dummy function to replace time.sleep."""
    # print(f"Skipping sleep({seconds})") # Optional debug print
    pass

def test_start_new_game_flow(monkeypatch, capsys):
    """
    Tests the start_new_game function's basic execution flow:
    - Calls opening_scene_start (mocked).
    - Prints the game start confirmation message.
    - Runs without error and without actual sleep delay.

    Args:
        monkeypatch: pytest fixture to modify modules/functions.
        capsys: pytest fixture to capture stdout/stderr.
    """
    # Arrange: Reset call tracker and patch dependencies
    global mock_opening_scene_called
    mock_opening_scene_called = False # Ensure tracker is reset before test

    monkeypatch.setattr(opening_scene, "opening_scene_start", dummy_opening_scene_start)
    monkeypatch.setattr(time, "sleep", dummy_sleep)
    # Alternative for time.sleep if imported directly in main_game:
    # monkeypatch.setattr(main_game.time, "sleep", dummy_sleep)

    # Act: Run the function to be tested
    try:
        main_game.start_new_game()
    except Exception as e:
        pytest.fail(f"main_game.start_new_game() raised an exception: {e}")

    # Assert: Verify the mocked function was called and the correct output was printed
    captured = capsys.readouterr()

    assert mock_opening_scene_called, "opening_scene.opening_scene_start should have been called."
    assert GameMessages.GAME_START_CONFIRMATION in captured.out, \
        f"Expected '{GameMessages.GAME_START_CONFIRMATION}' in stdout, but got: '{captured.out}'"
