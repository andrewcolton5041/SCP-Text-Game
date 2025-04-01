# tests/test_enums.py
"""
Unit tests for enum classes defined in src.enums.
Tests enum creation, properties, comparison, and usage patterns.
"""
import pytest
from enum import Enum, auto

from src.enums import (
    GameState, 
    CharacterState,
    MentalState,
    LocationState,
    MissionState,
    AnomalyState,
    TrustLevel,
    InteractionState
)


class TestEnumBasics:
    """Test basic enum functionality and properties."""

    def test_enum_values_are_unique(self):
        """Test that enum values are unique within each enum class."""
        # Loop through all enum classes
        for enum_class in [
            GameState, CharacterState, MentalState, LocationState,
            MissionState, AnomalyState, TrustLevel, InteractionState
        ]:
            # Get all values
            values = [member.value for member in enum_class]
            # Check uniqueness
            assert len(values) == len(set(values)), f"Values in {enum_class.__name__} are not unique"
    
    def test_enum_member_types(self):
        """Test that enum members are the correct type."""
        for enum_class in [
            GameState, CharacterState, MentalState, LocationState,
            MissionState, AnomalyState, TrustLevel, InteractionState
        ]:
            for member in enum_class:
                assert isinstance(member, enum_class)
                assert isinstance(member, Enum)


class TestGameState:
    """Test GameState enum specifically."""
    
    def test_game_state_values(self):
        """Test that GameState has expected members."""
        expected_members = [
            "INITIALIZING", "MAIN_MENU", "NEW_GAME", "LOADING",
            "PLAYING", "PAUSED", "DIALOGUE", "COMBAT", "GAME_OVER", "QUITTING"
        ]
        actual_members = [member.name for member in GameState]
        
        # Check all expected members exist
        for expected in expected_members:
            assert expected in actual_members
    
    def test_game_state_equality(self):
        """Test enum equality comparisons."""
        assert GameState.PLAYING == GameState.PLAYING
        assert GameState.PLAYING != GameState.PAUSED
        assert GameState.PLAYING is GameState.PLAYING


class TestCharacterStates:
    """Test character-related state enums."""
    
    def test_character_state_transitions(self):
        """Test logical state transitions make sense."""
        # Example: NORMAL->INJURED->CRITICAL->DEAD is logical
        # Check values ensure proper ordering
        assert CharacterState.NORMAL.value < CharacterState.INJURED.value
        assert CharacterState.INJURED.value < CharacterState.CRITICAL.value
        assert CharacterState.CRITICAL.value < CharacterState.DEAD.value
    
    def test_mental_state_transitions(self):
        """Test mental state progression makes sense."""
        assert MentalState.STABLE.value < MentalState.STRESSED.value
        assert MentalState.STRESSED.value < MentalState.UNSTABLE.value
        assert MentalState.UNSTABLE.value < MentalState.BREAKING.value
        assert MentalState.BREAKING.value < MentalState.BROKEN.value


class TestMissionState:
    """Test MissionState enum functionality."""
    
    def test_mission_state_members(self):
        """Test MissionState has expected members."""
        expected_states = [
            "NOT_STARTED", "AVAILABLE", "IN_PROGRESS", 
            "COMPLETED", "FAILED", "LOCKED"
        ]
        actual_states = [state.name for state in MissionState]
        
        for expected in expected_states:
            assert expected in actual_states


class TestEnumStringConversion:
    """Test string conversion functionality with enums."""
    
    def test_enum_to_str(self):
        """Test converting enum values to strings."""
        assert str(GameState.PLAYING) == "GameState.PLAYING"
        assert GameState.PLAYING.name == "PLAYING"
    
    def test_str_to_enum(self):
        """Test converting strings to enum values."""
        assert GameState["PLAYING"] == GameState.PLAYING
        
        # Test with invalid name
        with pytest.raises(KeyError):
            GameState["NONEXISTENT"]


class TestEnumIntegration:
    """Test using enums in typical game scenarios."""
    
    def test_state_transitions(self):
        """Test state transition patterns in a simulated game flow."""
        # Simulate a sequence of game states
        current_state = GameState.INITIALIZING
        
        # Transition to main menu
        current_state = GameState.MAIN_MENU
        assert current_state == GameState.MAIN_MENU
        
        # Start new game
        current_state = GameState.NEW_GAME
        assert current_state == GameState.NEW_GAME
        
        # Begin playing
        current_state = GameState.PLAYING
        assert current_state == GameState.PLAYING
        
        # Pause game
        current_state = GameState.PAUSED
        assert current_state == GameState.PAUSED
        
        # Resume
        current_state = GameState.PLAYING
        assert current_state == GameState.PLAYING
        
        # Enter combat
        current_state = GameState.COMBAT
        assert current_state == GameState.COMBAT
        
        # Return to playing
        current_state = GameState.PLAYING
        assert current_state == GameState.PLAYING
        
        # End game
        current_state = GameState.GAME_OVER
        assert current_state == GameState.GAME_OVER
    
    def test_character_state_changes(self):
        """Test character state changes in typical game scenarios."""
        # Character starts normal
        char_state = CharacterState.NORMAL
        mental_state = MentalState.STABLE
        
        # Character takes damage
        char_state = CharacterState.INJURED
        assert char_state == CharacterState.INJURED
        
        # Character experiences stress
        mental_state = MentalState.STRESSED
        assert mental_state == MentalState.STRESSED
        
        # Character takes critical damage
        char_state = CharacterState.CRITICAL
        assert char_state == CharacterState.CRITICAL
        
        # Mental state deteriorates
        mental_state = MentalState.UNSTABLE
        assert mental_state == MentalState.UNSTABLE
        
        # Character becomes compromised
        char_state = CharacterState.COMPROMISED
        assert char_state == CharacterState.COMPROMISED