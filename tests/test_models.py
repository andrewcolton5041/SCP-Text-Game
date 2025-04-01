# tests/test_models.py
"""
Unit tests for the data models in src/models.py.
Tests dataclass initialization, default values, and basic functionality.
"""
import pytest
from src.models import (
    Character, Location, Item, GameState, 
    CharacteristicStats, DerivedStats, SkillSet,
    Background, CombatRoll, SpecialAbility
)

def test_character_creation():
    """Tests creating a Character with minimal and full parameters."""
    # Minimal character
    minimal_char = Character(name="Test Agent", age=30)
    assert minimal_char.name == "Test Agent"
    assert minimal_char.age == 30
    assert minimal_char.nationality == "Unknown"  # Default value
    
    # Character with more attributes
    detailed_char = Character(
        name="Agent Smith",
        age=35,
        nationality="British",
        clearance_level=3,
        role="Field Agent"
    )
    assert detailed_char.name == "Agent Smith"
    assert detailed_char.age == 35
    assert detailed_char.nationality == "British"
    assert detailed_char.clearance_level == 3
    assert detailed_char.role == "Field Agent"
    
    # Verify defaults are created
    assert isinstance(detailed_char.characteristics, CharacteristicStats)
    assert isinstance(detailed_char.derived_stats, DerivedStats)
    assert isinstance(detailed_char.skills, SkillSet)
    assert isinstance(detailed_char.background, Background)
    assert detailed_char.inventory == {}
    assert detailed_char.status_flags == {}

def test_characteristic_stats():
    """Tests the CharacteristicStats dataclass."""
    # Default stats
    default_stats = CharacteristicStats()
    assert default_stats.strength == 50
    assert default_stats.intelligence == 50
    
    # Custom stats
    custom_stats = CharacteristicStats(
        strength=65,
        constitution=60,
        intelligence=75
    )
    assert custom_stats.strength == 65
    assert custom_stats.constitution == 60
    assert custom_stats.intelligence == 75
    assert custom_stats.dexterity == 50  # Default value

def test_item_creation():
    """Tests creating various Item objects."""
    # Basic item
    basic_item = Item(name="Keycard", type="keycard")
    assert basic_item.name == "Keycard"
    assert basic_item.type == "keycard"
    assert basic_item.still_have is True
    assert basic_item.quantity == 1
    
    # Weapon with damage
    weapon = Item(
        name="Foundation Sidearm",
        type="weapon",
        damage_dice="1D10",
        loaded=True,
        ammo_capacity=15
    )
    assert weapon.name == "Foundation Sidearm"
    assert weapon.damage_dice == "1D10"
    assert weapon.loaded is True
    assert weapon.ammo_capacity == 15

def test_location_creation():
    """Tests creating Location objects."""
    # Simple location
    office = Location(
        name="Director's Office",
        description="A sterile white Foundation office."
    )
    assert office.name == "Director's Office"
    assert office.description == "A sterile white Foundation office."
    assert office.visited is False
    assert office.connections == {}
    assert office.items == []
    assert office.npcs == []
    
    # Location with connections
    corridor = Location(
        name="Main Corridor",
        description="A long, well-lit corridor.",
        connections={"north": "lab", "south": "office"},
        visited=True
    )
    assert corridor.connections == {"north": "lab", "south": "office"}
    assert corridor.visited is True

def test_game_state():
    """Tests creating and modifying GameState."""
    # Create test character and location
    player = Character(name="Agent Test", age=30)
    office = Location(
        name="Starting Room",
        description="Where you begin."
    )
    
    # Create game state
    game = GameState(
        player=player,
        current_location="office"
    )
    assert game.player.name == "Agent Test"
    assert game.current_location == "office"
    
    # Add location to game state
    game.locations["office"] = office
    assert "office" in game.locations
    assert game.locations["office"].name == "Starting Room"
    
    # Test adding game flags
    game.game_flags["met_director"] = True
    assert game.game_flags["met_director"] is True