# tests/test_main_menu.py
"""
Unit tests for the main menu logic in src/main_menu.py.
Uses pytest fixtures monkeypatch (for input/external calls) and capsys (for output).
"""
import pytest
from unittest.mock import Mock
from typing import Iterator, Optional, List # Added typing imports

# Import types for pytest fixtures
from _pytest.monkeypatch import MonkeyPatch
from _pytest.capture import CaptureFixture

# Modules involved in the test
from src import main_menu
from src import utilities
from src import main_game
from src.constants import MainMenuStrings, EXIT_MESSAGE

# --- Test Functions (Updated with Type Hints) ---

def test_main_menu_quit_immediately(monkeypatch: MonkeyPatch, capsys: CaptureFixture) -> None:
    """Tests the flow: Show title -> Press Enter -> Show menu -> Input 'q' -> Exit."""
    # Arrange: Simulate user pressing Enter, then 'q'
    inputs: Iterator[str] = iter(['', 'q'])

    # Define mock input function that prints prompt
    def mock_input_that_prints(prompt: Optional[str] = None) -> str:
        if prompt:
            print(prompt, end='') # type: ignore
        try:
            return next(inputs)
        except StopIteration:
            raise EOFError("Mock input called too many times.")
    monkeypatch.setattr('builtins.input', mock_input_that_prints)

    # Create Mock objects for external calls
    mock_clear = Mock(spec=utilities.clear_screen)
    monkeypatch.setattr(utilities, 'clear_screen', mock_clear)

    # Act: Run the main menu function
    main_menu.display_main_menu()

    # Assert: Check output and mock calls
    captured = capsys.readouterr()
    assert mock_clear.call_count >= 3
    assert MainMenuStrings.TITLE in captured.out
    assert MainMenuStrings.ENTER_TO_CONTINUE in captured.out
    assert MainMenuStrings.MAIN_MENU_TITLE in captured.out
    assert MainMenuStrings.INPUT_REQUEST in captured.out
    assert MainMenuStrings.QUIT in captured.out
    assert EXIT_MESSAGE in captured.out

def test_main_menu_start_new_game(monkeypatch: MonkeyPatch, capsys: CaptureFixture) -> None:
    """Tests the flow: Enter -> 'n' -> Enter (after game msg) -> 'q'."""
    inputs: Iterator[str] = iter(['', 'n', '', 'q'])

    def mock_input_that_prints(prompt: Optional[str] = None) -> str:
        if prompt:
            print(prompt, end='') # type: ignore
        try:
            return next(inputs)
        except StopIteration:
            raise EOFError("Mock input called too many times.")
    monkeypatch.setattr('builtins.input', mock_input_that_prints)

    mock_clear = Mock(spec=utilities.clear_screen)
    mock_start_game = Mock(spec=main_game.start_new_game)
    monkeypatch.setattr(utilities, 'clear_screen', mock_clear)
    monkeypatch.setattr(main_game, 'start_new_game', mock_start_game)

    main_menu.display_main_menu()

    captured = capsys.readouterr()
    assert mock_clear.call_count >= 5
    mock_start_game.assert_called_once()
    assert "Starting New Game..." in captured.out
    assert "Press Enter to return to menu..." in captured.out
    assert EXIT_MESSAGE in captured.out

def test_main_menu_invalid_input_then_quit(monkeypatch: MonkeyPatch, capsys: CaptureFixture) -> None:
    """Tests the flow: Enter -> Invalid input 'x' -> Enter (ack error) -> 'q'."""
    inputs: Iterator[str] = iter(['', 'x', '', 'q'])

    def mock_input_that_prints(prompt: Optional[str] = None) -> str:
        if prompt:
            print(prompt, end='') # type: ignore
        try:
            return next(inputs)
        except StopIteration:
            raise EOFError("Mock input called too many times.")
    monkeypatch.setattr('builtins.input', mock_input_that_prints)

    mock_clear = Mock(spec=utilities.clear_screen)
    monkeypatch.setattr(utilities, 'clear_screen', mock_clear)

    main_menu.display_main_menu()

    captured = capsys.readouterr()
    assert mock_clear.call_count >= 4
    assert MainMenuStrings.INVALID_SELECTION in captured.out
    assert "Press Enter to try again..." in captured.out
    assert captured.out.count(MainMenuStrings.MAIN_MENU_TITLE) >= 2
    assert EXIT_MESSAGE in captured.out

def test_main_menu_case_insensitive_input(monkeypatch: MonkeyPatch, capsys: CaptureFixture) -> None:
    """Tests that input 'N' is treated the same as 'n'."""
    inputs: Iterator[str] = iter(['', 'N', '', 'q'])

    def mock_input_that_prints(prompt: Optional[str] = None) -> str:
        if prompt:
            print(prompt, end='') # type: ignore
        try:
            return next(inputs)
        except StopIteration:
            raise EOFError("Mock input called too many times.")
    monkeypatch.setattr('builtins.input', mock_input_that_prints)

    mock_clear = Mock(spec=utilities.clear_screen)
    mock_start_game = Mock(spec=main_game.start_new_game)
    monkeypatch.setattr(utilities, 'clear_screen', mock_clear)
    monkeypatch.setattr(main_game, 'start_new_game', mock_start_game)

    main_menu.display_main_menu()

    captured = capsys.readouterr()
    mock_start_game.assert_called_once()
    assert "Starting New Game..." in captured.out
    assert "Press Enter to return to menu..." in captured.out
    assert EXIT_MESSAGE in captured.out

def test_main_menu_load_game_path(monkeypatch: MonkeyPatch, capsys: CaptureFixture) -> None:
    """Tests the (currently not implemented) 'Load Game' path."""
    inputs: Iterator[str] = iter(['', 'l', '', 'q'])

    def mock_input_that_prints(prompt: Optional[str] = None) -> str:
        if prompt:
            print(prompt, end='') # type: ignore
        try:
            return next(inputs)
        except StopIteration:
            raise EOFError("Mock input called too many times.")
    monkeypatch.setattr('builtins.input', mock_input_that_prints)

    mock_clear = Mock(spec=utilities.clear_screen)
    monkeypatch.setattr(utilities, 'clear_screen', mock_clear)

    main_menu.display_main_menu()

    captured = capsys.readouterr()
    assert "Loading Game... (Not implemented yet)" in captured.out
    assert "Press Enter to return to menu..." in captured.out
    assert EXIT_MESSAGE in captured.out

def test_main_menu_options_path(monkeypatch: MonkeyPatch, capsys: CaptureFixture) -> None:
    """Tests the (currently not implemented) 'Options' path."""
    inputs: Iterator[str] = iter(['', 'o', '', 'q'])

    def mock_input_that_prints(prompt: Optional[str] = None) -> str:
        if prompt:
            print(prompt, end='') # type: ignore
        try:
            return next(inputs)
        except StopIteration:
            raise EOFError("Mock input called too many times.")
    monkeypatch.setattr('builtins.input', mock_input_that_prints)

    mock_clear = Mock(spec=utilities.clear_screen)
    monkeypatch.setattr(utilities, 'clear_screen', mock_clear)

    main_menu.display_main_menu()

    captured = capsys.readouterr()
    assert "Opening Options... (Not implemented yet)" in captured.out
    assert "Press Enter to return to menu..." in captured.out
    assert EXIT_MESSAGE in captured.out
