# Add to tests/test_utilities.py
import pytest
import time
from src import utilities
from src.constants import OtherConstants # For default sleep time

# Mock time.sleep globally for utility tests if needed, or per test
@pytest.fixture(autouse=True)
def mock_sleep(monkeypatch):
    """Mock time.sleep to avoid actual pauses during tests."""
    mock_sleep.call_count = 0 # Use function attribute to track calls
    def dummy_sleep(seconds):
        mock_sleep.call_count += 1
        # print(f"Mock sleep called with {seconds}s") # Optional debug
    monkeypatch.setattr(time, "sleep", dummy_sleep)
    return mock_sleep # Return the mock object/tracker if needed

def test_display_text_sequentially_with_string(capsys, mock_sleep):
    """Test displaying a multi-line string sequentially."""
    test_string = "Line 1\nLine 2\n\nLine 4"
    expected_lines = ["Line 1", "Line 2", "", "Line 4"]
    expected_output = "\n".join(expected_lines) + "\n" # print adds newline

    utilities.display_text_sequentially(test_string, delay=0.01) # Use small delay

    captured = capsys.readouterr()
    assert captured.out == expected_output
    assert mock_sleep.call_count == len(expected_lines) # Sleep called for each line

def test_display_text_sequentially_with_list(capsys, mock_sleep):
    """Test displaying a list of strings sequentially."""
    test_list = ["First line.", "Second line.", "Third."]
    expected_output = "\n".join(test_list) + "\n"

    utilities.display_text_sequentially(test_list, delay=0.01)

    captured = capsys.readouterr()
    assert captured.out == expected_output
    assert mock_sleep.call_count == len(test_list)

def test_display_text_sequentially_uses_default_delay(monkeypatch):
    """Verify default delay is used if none provided."""
    sleep_seconds_recorded = []
    def record_sleep(seconds):
        sleep_seconds_recorded.append(seconds)
    monkeypatch.setattr(time, "sleep", record_sleep)

    utilities.display_text_sequentially(["Test"])

    assert len(sleep_seconds_recorded) == 1
    assert sleep_seconds_recorded[0] == OtherConstants.SLEEP

def test_display_text_sequentially_handles_unsupported_type(capsys, mock_sleep):
    """Test handling of unsupported data types."""
    test_data = 12345
    utilities.display_text_sequentially(test_data)
    captured = capsys.readouterr()
    assert "Error: Cannot display text" in captured.out
    assert mock_sleep.call_count == 0 # Should not sleep if error occurs early