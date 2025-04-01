# src/enums.py
"""
Enum definitions for state management in Project Chimera.

This module defines various enumeration classes used to represent
discrete states throughout the game, improving type safety and code readability.
"""
from enum import Enum, auto


class GameState(Enum):
    """
    Represents the high-level state of the game application.
    Controls which game systems are active and how input is processed.
    """
    INITIALIZING = auto()
    MAIN_MENU = auto()
    NEW_GAME = auto()
    LOADING = auto()
    PLAYING = auto()
    PAUSED = auto()
    DIALOGUE = auto()
    COMBAT = auto()
    GAME_OVER = auto()
    QUITTING = auto()


class CharacterState(Enum):
    """
    Represents the current physical/mental state of a character.
    Affects available actions and potentially stat modifiers.
    """
    NORMAL = auto()
    INJURED = auto()  # HP below 50%
    CRITICAL = auto()  # HP below 25%
    COMPROMISED = auto()  # Under anomalous influence
    UNCONSCIOUS = auto()
    DEAD = auto()


class MentalState(Enum):
    """
    Represents a character's mental/psychological condition.
    Affects decision-making, available actions, and NPC interactions.
    """
    STABLE = auto()
    STRESSED = auto()  # MS below 75%
    UNSTABLE = auto()  # MS below 50%
    BREAKING = auto()  # MS below 25%
    BROKEN = auto()  # MS at 0


class LocationState(Enum):
    """
    Represents the current condition/status of a game location.
    Affects available interactions and potential hazards.
    """
    SECURE = auto()
    UNSECURED = auto()
    COMPROMISED = auto()
    ANOMALOUS = auto()  # Under active anomalous influence
    INACCESSIBLE = auto()


class MissionState(Enum):
    """
    Represents the current status of a mission or objective.
    Used to track progress through the game narrative.
    """
    NOT_STARTED = auto()
    AVAILABLE = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    FAILED = auto()
    LOCKED = auto()  # Prerequisites not met


class AnomalyState(Enum):
    """
    Represents the current status/phase of an anomalous entity or effect.
    Used for tracking containment status or threat levels.
    """
    DORMANT = auto()
    ACTIVE = auto()
    CONTAINED = auto()
    BREACHING = auto()
    UNCONTAINED = auto()


class TrustLevel(Enum):
    """
    Represents an NPC's level of trust/disposition toward the player.
    Affects dialogue options and available interactions.
    """
    HOSTILE = auto()
    SUSPICIOUS = auto()
    NEUTRAL = auto()
    TRUSTING = auto()
    LOYAL = auto()


class InteractionState(Enum):
    """
    Represents the current mode of interaction with the game world.
    Determines which command set is active and how input is processed.
    """
    EXPLORATION = auto()  # Moving between locations, examining
    DIALOGUE = auto()  # Talking to NPCs
    INVESTIGATION = auto()  # Detailed examination/evidence collection
    COMBAT = auto()  # Turn-based combat system
    INVENTORY = auto()  # Managing items
    DOCUMENT_REVIEW = auto()  # Reading found documents
    
