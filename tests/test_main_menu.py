# tests/test_main_menu.py
"""
Unit tests for the main menu logic in src/main_menu.py.
Uses pytest fixtures monkeypatch (for input/external calls) and capsys (for output).
"""

import pytest

# Modules involved in the test
from src import main_menu
from src import utilities
from src import main_game
from src.constants import MainMenuStrings, EXIT_MESSAGE

# --- Mocking Setup ---

# Counters to track mock function calls
mock_clear_screen_calls = 0
mock_start_new_game_calls = 0

def mock_clear_screen():
    """Mock version of utilities.clear_screen."""
    global mock_clear_screen_calls
    mock_clear_screen_calls += 1
    # print("[Mock clear_screen called]") # Optional debug print

def mock_start_new_game():
    """Mock version of main_game.start_new_game."""
    global mock_start_new_game_calls
    mock_start_new_game_calls += 1
    # print("[Mock start_new_game called]") # Optional debug print

# --- Pytest Fixture to Reset Mocks ---

@pytest.fixture(autouse=True)
def reset_mocks_before_each_test():
    """Automatically resets mock call counters before each test function."""
    global mock_clear_screen_calls, mock_start_new_game_calls
    mock_clear_screen_calls = 0
    mock_start_new_game_calls = 0

# --- Test Functions ---

def test_main_menu_quit_immediately(monkeypatch, capsys):
    """Tests the flow: Show title -> Press Enter -> Show menu -> Input 'q' -> Exit."""
    # Arrange: Simulate user pressing Enter, then 'q'
    # Use iter to provide sequential inputs to the mocked 'input'
    inputs = iter(['', 'q'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs)) # Mock input()
    monkeypatch.setattr(utilities, 'clear_screen', mock_clear_screen) # Mock clear_screen

    # Act: Run the main menu function
    main_menu.display_main_menu()

    # Assert: Check output and mock calls
    captured = capsys.readouterr() # Capture printed output
    assert mock_clear_screen_calls >= 3 # Title display, Menu display, Final clear
    assert MainMenuStrings.TITLE in captured.out
    assert MainMenuStrings.MAIN_MENU_TITLE in captured.out
    assert MainMenuStrings.QUIT in captured.out # Check the quit option text
    assert EXIT_MESSAGE in captured.out # Check the final exit message

def test_main_menu_start_new_game(monkeypatch, capsys):
    """Tests the flow: Enter -> 'n' -> Enter (after game msg) -> 'q'."""
    # Arrange: Simulate inputs for title, 'n', returning from game, then 'q'
    inputs = iter(['', 'n', '', 'q'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr(utilities, 'clear_screen', mock_clear_screen)
    monkeypatch.setattr(main_game, 'start_new_game', mock_start_new_game) # Mock game start

    # Act
    main_menu.display_main_menu()

    # Assert
    captured = capsys.readouterr()
    assert mock_clear_screen_calls >= 5 # Title, Menu, After 'n', Menu again, Final clear
    assert mock_start_new_game_calls == 1 # Check that start_new_game was called once
    assert "Starting New Game..." in captured.out # Check user-facing message
    assert EXIT_MESSAGE in captured.out # Ensure it eventually quits

def test_main_menu_invalid_input_then_quit(monkeypatch, capsys):
    """Tests the flow: Enter -> Invalid input 'x' -> Enter (ack error) -> 'q'."""
    # Arrange: Simulate inputs for title, invalid choice, ack error, then 'q'
    inputs = iter(['', 'x', '', 'q'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr(utilities, 'clear_screen', mock_clear_screen)
    # No need to mock start_new_game for this path

    # Act
    main_menu.display_main_menu()

    # Assert
    captured = capsys.readouterr()
    # Title, Menu, After error, Menu again, Final clear
    assert mock_clear_screen_calls >= 5
    # Check that the invalid selection message appeared
    assert MainMenuStrings.INVALID_SELECTION in captured.out
    # Check that the prompt to continue after error appeared
    assert "Press Enter to try again..." in captured.out
    # Check that the main menu title appeared at least twice (initial + after error)
    assert captured.out.count(MainMenuStrings.MAIN_MENU_TITLE) >= 2
    assert EXIT_MESSAGE in captured.out # Ensure it eventually quits

def test_main_menu_case_insensitive_input(monkeypatch, capsys):
    """Tests that input 'N' is treated the same as 'n'."""
    # Arrange: Use uppercase 'N'
    inputs = iter(['', 'N', '', 'q'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr(utilities, 'clear_screen', mock_clear_screen)
    monkeypatch.setattr(main_game, 'start_new_game', mock_start_new_game)

    # Act
    main_menu.display_main_menu()

    # Assert
    captured = capsys.readouterr()
    assert mock_start_new_game_calls == 1 # Verify game started even with 'N'
    assert "Starting New Game..." in captured.out
    assert EXIT_MESSAGE in captured.out

def test_main_menu_load_game_path(monkeypatch, capsys):
    """Tests the (currently not implemented) 'Load Game' path."""
    inputs = iter(['', 'l', '', 'q']) # Enter, 'l', Enter (after msg), 'q'
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr(utilities, 'clear_screen', mock_clear_screen)

    # Act
    main_menu.display_main_menu()

    # Assert
    captured = capsys.readouterr()
    assert "Loading Game... (Not implemented yet)" in captured.out
    assert EXIT_MESSAGE in captured.out

def test_main_menu_options_path(monkeypatch, capsys):
    """Tests the (currently not implemented) 'Options' path."""
    inputs = iter(['', 'o', '', 'q']) # Enter, 'o', Enter (after msg), 'q'
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr(utilities, 'clear_screen', mock_clear_screen)

    # Act
    main_menu.display_main_menu()

    # Assert
    captured = capsys.readouterr()
    assert "Opening Options... (Not implemented yet)" in captured.out
    assert EXIT_MESSAGE in captured.out
