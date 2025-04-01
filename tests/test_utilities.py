# tests/test_utilities.py
"""
Unit tests for the utility functions in src/utilities.py.
"""

# No need to import pytest explicitly unless using fixtures like monkeypatch/capsys yet

from src import utilities # Import the module we are testing

def test_clear_screen_runs_without_error():
    """
    Tests that utilities.clear_screen() executes without raising an exception.

    Note: This test does not verify that the screen *was actually cleared*,
    as that involves complex OS interaction checks. It only checks for runtime
    errors during the function call.
    """
    try:
        utilities.clear_screen()
        # If the function call completes without error, the test passes implicitly.
        assert True # Explicitly assert True for clarity if no exception occurred
    except Exception as e:
        # If any exception occurs, fail the test
        assert False, f"utilities.clear_screen() raised an exception: {e}"

# Add more test functions here for other utilities as they are added.
# For example:
# def test_another_utility_function():
#     result = utilities.another_function(input)
#     assert result == expected_output