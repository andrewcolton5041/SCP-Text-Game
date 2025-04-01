# tests/test_main_game.py
"""
Unit tests for the main game logic in src/main_game.py.
"""
import pytest
from unittest.mock import Mock # Import Mock

# Modules involved in the test
from src import main_game
from src import opening_scene
from src import utilities # Import utilities
from src.constants import BriefingMessages # Use BriefingMessages

# --- Remove Global Flags and Dummy Functions ---
# Remove:
# mock_opening_scene_called = False
# def dummy_opening_scene_start(): ...
# def dummy_sleep(seconds): ... # Keep if mocking time.sleep is still needed elsewhere
# mock_clear_screen_calls = 0 # Remove if added previously
# def mock_clear_screen(): ... # Remove if added previously

def test_start_new_game_flow(monkeypatch, capsys):
    """
    Tests the start_new_game function's execution flow:
    - Calls opening_scene_start (mocked).
    - Clears screen (mocked).
    - Prints the briefing memo sequentially (via mocked utility).
    - Waits for acknowledgement input.
    - Runs without error.
    """
    # Arrange: Mock dependencies
    mock_opening = Mock(spec=opening_scene.opening_scene_start)
    mock_clear = Mock(spec=utilities.clear_screen)
    mock_display_seq = Mock(spec=utilities.display_text_sequentially) # Mock the utility

    monkeypatch.setattr(opening_scene, "opening_scene_start", mock_opening)
    monkeypatch.setattr(utilities, "clear_screen", mock_clear)
    monkeypatch.setattr(utilities, "display_text_sequentially", mock_display_seq) # Patch the utility

    # Mock input for acknowledgement
    inputs = iter([''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Act: Run the function to be tested
    try:
        main_game.start_new_game()
    except Exception as e:
        pytest.fail(f"main_game.start_new_game() raised an exception: {e}")

    # Assert: Verify mocks were called and correct arguments passed
    captured = capsys.readouterr()

    mock_opening.assert_called_once()
    mock_clear.assert_called_once()
    # Check that display_text_sequentially was called with the memo
    mock_display_seq.assert_called_once_with(BriefingMessages.FINCH_MEMO_CHIMERA)

    # Check that the final debug message is printed (output after mocks)
    assert "[DEBUG: Proceeding to Thorne's residence - To be implemented]" in captured.out