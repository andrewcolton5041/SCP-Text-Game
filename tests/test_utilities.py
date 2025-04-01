# tests/test_utilities.py
"""
Unit tests for the utility functions in src/utilities.py.
"""
import pytest
import time
from unittest.mock import Mock
from typing import List, Any, Optional, Callable

# Import types for pytest fixtures
from _pytest.monkeypatch import MonkeyPatch
from _pytest.capture import CaptureFixture

from src import utilities
from src.constants import OtherConstants # For default sleep time

import logging
logger = logging.getLogger(__name__)

# --- Fixtures ---

@pytest.fixture(autouse=True)
def mock_sleep(monkeypatch: MonkeyPatch) -> Mock:
    """Mock time.sleep to avoid actual pauses and track calls."""
    mock_sleep_obj: Mock = Mock(spec=time.sleep)
    monkeypatch.setattr(time, "sleep", mock_sleep_obj)
    return mock_sleep_obj # Return the mock object for potential assertions

# --- Test Functions ---

def test_clear_screen(
    monkeypatch: MonkeyPatch, 
    caplog: pytest.LogCaptureFixture
) -> None:
    """Tests that clear_screen calls the correct os.system command and logs."""
    # Set the logger level to ensure it captures debug messages
    caplog.set_level(logging.DEBUG)
    
    # We don't know the platform, so mock os.system
    mock_os_system: Mock = Mock()
    monkeypatch.setattr(utilities.os, "system", mock_os_system)
    # Mock platform.system to control the path taken
    monkeypatch.setattr(utilities.platform, "system", lambda: "Linux") # Example: Linux

    utilities.clear_screen()

    mock_os_system.assert_called_once_with('clear')
    assert "Screen cleared on platform: Linux" in caplog.text


def test_display_text_sequentially_with_string(
    capsys: CaptureFixture, 
    mock_sleep: Mock
) -> None:
    """Test displaying a multi-line string sequentially."""
    test_string: str = "Line 1\nLine 2\n\nLine 4"
    expected_lines: List[str] = ["Line 1", "Line 2", "", "Line 4"]
    expected_output: str = "\n".join(expected_lines) + "\n" # print adds newline

    utilities.display_text_sequentially(test_string, delay=0.01)

    captured = capsys.readouterr()
    assert captured.out == expected_output
    assert mock_sleep.call_count == len(expected_lines) # Sleep called for each line
    # Check if delay was passed correctly (optional)
    mock_sleep.assert_called_with(0.01)


def test_display_text_sequentially_with_list(
    capsys: CaptureFixture, 
    mock_sleep: Mock
) -> None:
    """Test displaying a list of strings sequentially."""
    test_list: List[str] = ["First line.", "Second line.", "Third."]
    expected_output: str = "\n".join(test_list) + "\n"

    utilities.display_text_sequentially(test_list, delay=0.01)

    captured = capsys.readouterr()
    assert captured.out == expected_output
    assert mock_sleep.call_count == len(test_list)


def test_display_text_sequentially_uses_default_delay(
    monkeypatch: MonkeyPatch, 
    mock_sleep: Mock
) -> None:
    """Verify default delay is used if none provided."""
    # mock_sleep fixture already patches time.sleep
    test_list: List[str] = ["Test"]
    utilities.display_text_sequentially(test_list)

    assert mock_sleep.call_count == 1
    # Assert that sleep was called with the default value from constants
    mock_sleep.assert_called_once_with(OtherConstants.SLEEP)


def test_display_text_sequentially_handles_unsupported_type(
    capsys: CaptureFixture, 
    mock_sleep: Mock, 
    caplog: pytest.LogCaptureFixture
) -> None:
    """Test handling of unsupported data types."""
    test_data: int = 12345
    # Add type: ignore comment to tell mypy this specific line is intentional
    utilities.display_text_sequentially(test_data) # type: ignore[arg-type]
    captured = capsys.readouterr()

    assert "Error: Cannot display text" in captured.out
    assert "Unsupported text_data type" in caplog.text
    assert mock_sleep.call_count == 0 # Should not sleep if error occurs early