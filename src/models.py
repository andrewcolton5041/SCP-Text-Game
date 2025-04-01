# src/models.py (partial update to fix the name collision)
"""
Data models for Project Chimera using dataclasses.
"""
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Set, Union
from enum import Enum

from .enums import (
    CharacterState, 
    MentalState, 
    LocationState, 
    MissionState,
    AnomalyState, 
    TrustLevel, 
    GameState as GameStateEnum,  # Renamed import to avoid collision
    InteractionState
)


@dataclass
class CharacteristicStats:
    """Character base attributes/characteristics."""
    strength: int = 50
    constitution: int = 50
    size: int = 50
    intelligence: int = 50
    power: int = 50
    dexterity: int = 50
    appearance: int = 50
    education: int = 50


@dataclass
class DerivedStats:
    """Stats calculated from base characteristics."""
    hp: int = 10
    max_hp: int = 10
    ms: int = 50  # Mental stability
    max_ms: int = 50
    mp: int = 10  # Magic points
    max_mp: int = 10
    db: Any = 0  # Damage bonus (can be string like "+1D4" or int)
    build: int = 0
    move: int = 8


@dataclass
class CombatRoll:
    """Combat roll information for an attack type."""
    damage: str  # Damage dice notation (e.g. "1D3", "1D10")
    att_per_round: int = 1
    range: Optional[int] = None  # For ranged weapons


@dataclass
class Item:
    """Base class for all game items."""
    name: str
    type: str
    still_have: bool = True
    quantity: Any = 1  # Can be int or "Varies"
    
    # Optional common attributes with defaults
    wearing: bool = False
    charged: bool = False
    on: bool = False
    loaded: bool = False
    
    # Container contents
    contents: Dict[str, Any] = field(default_factory=dict)
    empty: bool = False
    
    # Specialized attributes
    damage_dice: Optional[str] = None
    healing: Optional[str] = None
    effect: Optional[str] = None
    potency: Optional[str] = None
    access_level: Optional[int] = None
    still_activated: bool = True
    ammo_capacity: Optional[int] = None
    ammo_type: Optional[str] = None
    content_summary: Optional[str] = None
    anomalous_state: Optional[AnomalyState] = None


@dataclass
class Background:
    """Character background information."""
    specialization: str = ""
    reason_joining_found: str = ""
    ideology: str = ""
    contact: str = ""
    incidents: str = ""
    possession: str = ""
    description: str = ""


@dataclass
class InvestigativeSkills:
    """Investigative skills for a character."""
    spot_hidden: int = 0
    listen: int = 0
    library_use: int = 0
    psychology: int = 0
    forensics: int = 0


@dataclass
class CombatSurvivalSkills:
    """Combat and survival skills for a character."""
    handgun: int = 0
    brawl: int = 0
    dodge: int = 0
    stealth: int = 0
    first_aid: int = 0
    melee_weapon_blunt: int = 0
    throw: int = 0


@dataclass
class TechnicalKnowledgeSkills:
    """Technical and knowledge-based skills."""
    computer_use: int = 0
    mechanical_repair: int = 0
    electrical_repair: int = 0
    anomalous_theory: int = 0
    foundation_lore: int = 0
    anomalous_studies: int = 0
    archaeology: int = 0
    history: int = 0
    knowledge_folklore: int = 0
    knowledge_herbalism: int = 0
    occult: int = 0
    knowledge_local_area: int = 0
    knowledge_gois: int = 0
    knowledge_goi_xxx: int = 0
    knowledge_occult: int = 0
    knowledge_anomalous_history: int = 0


@dataclass
class SocialSkills:
    """Social interaction skills."""
    charm: int = 0
    fast_talk: int = 0
    intimidate: int = 0
    persuade: int = 0
    credit_rating: int = 0


@dataclass
class OtherSkills:
    """Miscellaneous skills including languages."""
    drive_auto: int = 0
    navigate: int = 0
    language_english: int = 0
    language_spanish: int = 0
    language_quechua: int = 0
    english: int = 0  # Alternative naming in some character files
    spanish: int = 0  # Alternative naming
    sense_anomalous: int = 0


@dataclass
class SkillSet:
    """Complete set of skills for a character."""
    investigative: InvestigativeSkills = field(default_factory=InvestigativeSkills)
    combat_survival: CombatSurvivalSkills = field(default_factory=CombatSurvivalSkills)
    technical_knowledge: TechnicalKnowledgeSkills = field(default_factory=TechnicalKnowledgeSkills)
    social: SocialSkills = field(default_factory=SocialSkills)
    other: OtherSkills = field(default_factory=OtherSkills)


@dataclass
class SpecialAbility:
    """Special abilities for entities like RBC-Prime."""
    name: str
    type: str = "Passive"
    range: Optional[str] = None
    effect: str = ""
    resistance: Optional[str] = None
    cost_mp: Optional[int] = None
    rate: Optional[int] = None
    unit: Optional[str] = None
    notes: Optional[str] = None
    value: Optional[int] = None


@dataclass
class Character:
    """Base character class for all NPCs and player character."""
    name: str
    age: Any  # Can be int or string like "70s"
    nationality: str = "Unknown"
    clearance_level: Optional[int] = None
    role: Optional[str] = None
    alias: bool = False  # True if name is an alias
    title: bool = False  # True if name is a title
    
    # Core stats
    characteristics: CharacteristicStats = field(default_factory=CharacteristicStats)
    derived_stats: DerivedStats = field(default_factory=DerivedStats)
    skills: SkillSet = field(default_factory=SkillSet)
    
    # Background
    background: Background = field(default_factory=Background)
    
    # Equipment and abilities
    combat_rolls: Dict[str, CombatRoll] = field(default_factory=dict)
    inventory: Dict[str, Item] = field(default_factory=dict)
    status_flags: Dict[str, Any] = field(default_factory=dict)
    special_abilities: Dict[str, SpecialAbility] = field(default_factory=dict)
    
    # State management (using enums)
    physical_state: CharacterState = CharacterState.NORMAL
    mental_state: MentalState = MentalState.STABLE
    trust_level: TrustLevel = TrustLevel.NEUTRAL
    
    # For special entities like Vance
    whisperer_state_mods: Optional[Dict[str, Any]] = None


@dataclass
class Location:
    """Game location/area."""
    name: str
    description: str
    connections: Dict[str, str] = field(default_factory=dict)  # Direction -> location_id
    items: List[str] = field(default_factory=list)  # Item IDs present in the location
    npcs: List[str] = field(default_factory=list)  # NPC IDs present in the location
    visited: bool = False
    locked_exits: Dict[str, bool] = field(default_factory=dict)  # Direction -> locked status
    state: LocationState = LocationState.SECURE
    anomaly_present: bool = False
    anomaly_state: Optional[AnomalyState] = None


@dataclass
class Mission:
    """Represents a mission or objective in the game."""
    id: str
    name: str
    description: str
    state: MissionState = MissionState.LOCKED
    prerequisites: List[str] = field(default_factory=list)  # List of mission IDs
    complete_conditions: Dict[str, Any] = field(default_factory=dict)
    rewards: Dict[str, Any] = field(default_factory=dict)
    related_npcs: List[str] = field(default_factory=list)
    related_locations: List[str] = field(default_factory=list)


@dataclass
class DialogueNode:
    """Represents a single node in a dialogue tree."""
    id: str
    text: str
    responses: Dict[str, str] = field(default_factory=dict)  # response_id -> next_node_id
    requirements: Dict[str, Any] = field(default_factory=dict)  # For conditional responses
    effects: Dict[str, Any] = field(default_factory=dict)  # State changes from this dialogue


# src/models.py (partial update to fix the name collision)
"""
Data models for Project Chimera using dataclasses.
"""
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Set, Union
from enum import Enum

from .enums import (
    CharacterState, 
    MentalState, 
    LocationState, 
    MissionState,
    AnomalyState, 
    TrustLevel, 
    GameState as GameStateEnum,  # Renamed import to avoid collision
    InteractionState
)

# ... [earlier code remains unchanged] ...

@dataclass
class GameState:
    """Tracks the overall state of the game."""
    player: Character
    current_location: str  # Location ID
    inventory: Dict[str, Item] = field(default_factory=dict)
    npcs: Dict[str, Character] = field(default_factory=dict)
    locations: Dict[str, Location] = field(default_factory=dict)
    game_flags: Dict[str, Any] = field(default_factory=dict)
    discovered_clues: Set[str] = field(default_factory=set)
    completed_objectives: Set[str] = field(default_factory=set)
    game_time: int = 0  # In-game time tracking (e.g., turns, minutes)
    missions: Dict[str, Mission] = field(default_factory=dict)
    
    # State tracking with enums - using renamed import
    current_game_state: GameStateEnum = GameStateEnum.INITIALIZING
    current_interaction_state: InteractionState = InteractionState.EXPLORATION
    active_dialogue: Optional[str] = None  # ID of active dialogue node if any