# tests/test_opening_scene.py
"""
Unit tests for the opening scene display in src/opening_scene.py.
"""

import time
import pytest # Import pytest to use fixtures

from src import opening_scene
# We don't strictly need constants here unless we want to check exact text,
# which might be brittle. Let's focus on execution and basic output for now.

def test_opening_scene_start_runs_and_prints(monkeypatch, capsys):
    """
    Tests that opening_scene_start executes without error, runs quickly
    by patching sleep, and prints some output.

    Args:
        monkeypatch: pytest fixture to modify modules/functions during tests.
        capsys: pytest fixture to capture stdout/stderr.
    """
    # Arrange: Patch time.sleep to do nothing
    def dummy_sleep(seconds):
        """A dummy function to replace time.sleep."""
        # print(f"Skipping sleep({seconds})") # Optional: for debugging the patch
        pass
    monkeypatch.setattr(time, "sleep", dummy_sleep)
    # Alternative using src.opening_scene directly if time is imported there as 'import time'
    # monkeypatch.setattr(opening_scene.time, "sleep", dummy_sleep)

    # Act: Run the function that displays the opening scene
    try:
        opening_scene.opening_scene_start()
    except Exception as e:
        # Fail the test if any exception occurs during execution
        pytest.fail(f"opening_scene.opening_scene_start() raised an exception: {e}")

    # Assert: Check that something was printed to standard output
    captured = capsys.readouterr()
    assert captured.out, "opening_scene_start() should have printed output to stdout."
    # Optional: A more specific check (e.g., check if the first line is present)
    # from src.constants import OpeningScreenMessages
    # assert OpeningScreenMessages.INTRO[0] in captured.out

    # No need for explicit assert True if no exception occurred and captured.out is non-empty