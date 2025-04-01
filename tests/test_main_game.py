# tests/test_main_game.py
"""
Unit tests for the main game logic in src/main_game.py.
"""
import pytest
from unittest.mock import Mock
from typing import Iterator, Any, Optional # Added typing imports

# Import types for pytest fixtures
from _pytest.monkeypatch import MonkeyPatch
from _pytest.capture import CaptureFixture

# Modules involved in the test
from src import main_game
from src import opening_scene
from src import utilities
from src.constants import BriefingMessages
from src.enums import GameState as GameStateEnum  # Added import for GameStateEnum
# --- Test Functions ---

def test_start_new_game_flow(monkeypatch: MonkeyPatch, capsys: CaptureFixture) -> None:
    """
    Tests the start_new_game function's execution flow:
    - Calls opening_scene_start (mocked).
    - Clears screen (mocked).
    - Calls display_text_sequentially for the memo (mocked).
    - Waits for acknowledgement input (mocked).
    - Runs without error and prints debug message.
    """
    # Arrange: Mock dependencies
    mock_opening = Mock(spec=opening_scene.opening_scene_start)
    mock_clear = Mock(spec=utilities.clear_screen)
    mock_display_seq = Mock(spec=utilities.display_text_sequentially)

    monkeypatch.setattr(opening_scene, "opening_scene_start", mock_opening)
    monkeypatch.setattr(utilities, "clear_screen", mock_clear)
    monkeypatch.setattr(utilities, "display_text_sequentially", mock_display_seq)

    # Mock input for acknowledgement
    inputs: Iterator[str] = iter([''])
    def mock_input_that_prints(prompt: Optional[str] = None) -> str:
        if prompt:
            print(prompt, end='') # type: ignore
        try:
            return next(inputs)
        except StopIteration:
            raise EOFError("Mock input called too many times.")
    monkeypatch.setattr('builtins.input', mock_input_that_prints)

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

    # Check that the acknowledgement prompt was printed by the mock input
    assert "Press Enter to acknowledge briefing..." in captured.out

    # Check that the final debug message is printed (output after mocks)
    assert "[DEBUG: Proceeding to Thorne's residence - To be implemented]" in captured.out
