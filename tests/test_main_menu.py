# tests/test_main_menu.py
"""
Unit tests for the main menu logic in src/main_menu.py.
Uses pytest fixtures monkeypatch (for input/external calls) and capsys (for output).
"""
import pytest
from unittest.mock import Mock # Import Mock

# Modules involved in the test
from src import main_menu
from src import utilities
from src import main_game
from src.constants import MainMenuStrings, EXIT_MESSAGE

# --- Test Functions (Updated) ---

def test_main_menu_quit_immediately(monkeypatch, capsys):
    """Tests the flow: Show title -> Press Enter -> Show menu -> Input 'q' -> Exit."""
    # Arrange: Simulate user pressing Enter, then 'q'
    inputs = iter(['', 'q'])

    # Define mock input function that prints prompt
    def mock_input_that_prints(prompt=None):
        if prompt:
            print(prompt, end='') # Print the prompt like the real input()
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
    # Expected calls: Title clear, Menu clear, Final clear on quit
    assert mock_clear.call_count >= 3
    assert MainMenuStrings.TITLE in captured.out
    # Check that the prompt for the title screen was printed
    assert MainMenuStrings.ENTER_TO_CONTINUE in captured.out
    assert MainMenuStrings.MAIN_MENU_TITLE in captured.out
    # Check that the prompt for menu input was printed
    assert MainMenuStrings.INPUT_REQUEST in captured.out
    assert MainMenuStrings.QUIT in captured.out
    assert EXIT_MESSAGE in captured.out

def test_main_menu_start_new_game(monkeypatch, capsys):
    """Tests the flow: Enter -> 'n' -> Enter (after game msg) -> 'q'."""
    # Arrange: Simulate inputs
    inputs = iter(['', 'n', '', 'q'])

    # Define mock input function that prints prompt
    def mock_input_that_prints(prompt=None):
        if prompt:
            print(prompt, end='')
        try:
            return next(inputs)
        except StopIteration:
            raise EOFError("Mock input called too many times.")
    monkeypatch.setattr('builtins.input', mock_input_that_prints)

    # Create Mocks
    mock_clear = Mock(spec=utilities.clear_screen)
    mock_start_game = Mock(spec=main_game.start_new_game)
    monkeypatch.setattr(utilities, 'clear_screen', mock_clear)
    monkeypatch.setattr(main_game, 'start_new_game', mock_start_game)

    # Act
    main_menu.display_main_menu()

    # Assert
    captured = capsys.readouterr()
    # Expected calls: Title, Menu, After 'n', Menu again, Final clear
    assert mock_clear.call_count >= 5
    mock_start_game.assert_called_once() # Verify game start was called exactly once
    assert "Starting New Game..." in captured.out
    # Check that the prompt after game message was printed
    assert "Press Enter to return to menu..." in captured.out
    assert EXIT_MESSAGE in captured.out

def test_main_menu_invalid_input_then_quit(monkeypatch, capsys):
    """Tests the flow: Enter -> Invalid input 'x' -> Enter (ack error) -> 'q'."""
    # Arrange: Simulate inputs
    inputs = iter(['', 'x', '', 'q'])

    # Define mock input function that prints prompt
    def mock_input_that_prints(prompt=None):
        if prompt:
            print(prompt, end='')
        try:
            return next(inputs)
        except StopIteration:
            raise EOFError("Mock input called too many times.")
    monkeypatch.setattr('builtins.input', mock_input_that_prints)

    # Create Mock
    mock_clear = Mock(spec=utilities.clear_screen)
    monkeypatch.setattr(utilities, 'clear_screen', mock_clear)
    # No need to mock start_new_game for this path

    # Act
    main_menu.display_main_menu()

    # Assert
    captured = capsys.readouterr()
    # Expected calls: Title, Menu, After invalid input ack, Menu again, Final clear
    assert mock_clear.call_count >= 4 # Corrected count
    assert MainMenuStrings.INVALID_SELECTION in captured.out
    # Check that the prompt for invalid input acknowledgement was printed
    assert "Press Enter to try again..." in captured.out
    # Check menu title appears at least twice (initial + after invalid)
    assert captured.out.count(MainMenuStrings.MAIN_MENU_TITLE) >= 2
    assert EXIT_MESSAGE in captured.out

def test_main_menu_case_insensitive_input(monkeypatch, capsys):
    """Tests that input 'N' is treated the same as 'n'."""
    # Arrange: Use uppercase 'N'
    inputs = iter(['', 'N', '', 'q'])

    # Define mock input function that prints prompt
    def mock_input_that_prints(prompt=None):
        if prompt:
            print(prompt, end='')
        try:
            return next(inputs)
        except StopIteration:
            raise EOFError("Mock input called too many times.")
    monkeypatch.setattr('builtins.input', mock_input_that_prints)

    # Create Mocks
    mock_clear = Mock(spec=utilities.clear_screen)
    mock_start_game = Mock(spec=main_game.start_new_game)
    monkeypatch.setattr(utilities, 'clear_screen', mock_clear)
    monkeypatch.setattr(main_game, 'start_new_game', mock_start_game)

    # Act
    main_menu.display_main_menu()

    # Assert
    captured = capsys.readouterr()
    mock_start_game.assert_called_once() # Verify game started even with 'N'
    assert "Starting New Game..." in captured.out
    assert "Press Enter to return to menu..." in captured.out
    assert EXIT_MESSAGE in captured.out

def test_main_menu_load_game_path(monkeypatch, capsys):
    """Tests the (currently not implemented) 'Load Game' path."""
    inputs = iter(['', 'l', '', 'q'])

    # Define mock input function that prints prompt
    def mock_input_that_prints(prompt=None):
        if prompt:
            print(prompt, end='')
        try:
            return next(inputs)
        except StopIteration:
            raise EOFError("Mock input called too many times.")
    monkeypatch.setattr('builtins.input', mock_input_that_prints)

    mock_clear = Mock(spec=utilities.clear_screen)
    monkeypatch.setattr(utilities, 'clear_screen', mock_clear)

    # Act
    main_menu.display_main_menu()

    # Assert
    captured = capsys.readouterr()
    assert "Loading Game... (Not implemented yet)" in captured.out
    assert "Press Enter to return to menu..." in captured.out
    assert EXIT_MESSAGE in captured.out

def test_main_menu_options_path(monkeypatch, capsys):
    """Tests the (currently not implemented) 'Options' path."""
    inputs = iter(['', 'o', '', 'q'])

    # Define mock input function that prints prompt
    def mock_input_that_prints(prompt=None):
        if prompt:
            print(prompt, end='')
        try:
            return next(inputs)
        except StopIteration:
            raise EOFError("Mock input called too many times.")
    monkeypatch.setattr('builtins.input', mock_input_that_prints)

    mock_clear = Mock(spec=utilities.clear_screen)
    monkeypatch.setattr(utilities, 'clear_screen', mock_clear)

    # Act
    main_menu.display_main_menu()

    # Assert
    captured = capsys.readouterr()
    assert "Opening Options... (Not implemented yet)" in captured.out
    assert "Press Enter to return to menu..." in captured.out
    assert EXIT_MESSAGE in captured.out
