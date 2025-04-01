# tests/test_opening_scene.py
"""
Unit tests for the opening scene logic in src/opening_scene.py.
"""
import pytest
from unittest.mock import Mock

# Import types for pytest fixtures
from _pytest.monkeypatch import MonkeyPatch
# from _pytest.capture import CaptureFixture # Not used directly here yet

from src import opening_scene
from src import utilities # To mock the utility function
from src.constants import OpeningScreenMessages # To check the argument

# --- Test Functions ---

def test_opening_scene_start_calls_utility(monkeypatch: MonkeyPatch) -> None:
    """
    Tests that opening_scene_start calls utilities.display_text_sequentially
    with the correct text.
    """
    # Arrange: Mock the utility function
    mock_display_seq = Mock(spec=utilities.display_text_sequentially)
    monkeypatch.setattr(utilities, "display_text_sequentially", mock_display_seq)

    # Act: Run the function to be tested
    opening_scene.opening_scene_start()

    # Assert: Verify the mock was called correctly
    mock_display_seq.assert_called_once_with(OpeningScreenMessages.INTRO)
