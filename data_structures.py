# Python Data Structures Tutorial
## Using Game Development Examples

---

## Table of Contents
1. [Lists](#lists)
2. [Dictionaries](#dictionaries)
3. [Tuples](#tuples)
4. [Sets](#sets)
5. [Nested Structures](#nested-structures)
6. [Queues and Stacks](#queues-and-stacks)
7. [Advanced Examples](#advanced-examples)

---

## Lists
**What they are:** Ordered, mutable collections that can hold any type of data.

**When to use in games:** Inventories, enemy waves, bullet arrays, action sequences, leaderboards

### Basic List Operations

```python
# Creating a player inventory
inventory = ["sword", "health potion", "shield", "map"]

# Adding items
inventory.append("magic scroll")  # Add to end
inventory.insert(0, "legendary bow")  # Add at specific position

# Removing items
inventory.remove("map")  # Remove specific item
last_item = inventory.pop()  # Remove and return last item
first_item = inventory.pop(0)  # Remove and return first item

# Accessing items
first_weapon = inventory[0]
last_weapon = inventory[-1]

# Slicing
first_three = inventory[0:3]
everything_but_first = inventory[1:]

print(f"Inventory: {inventory}")
print(f"Total items: {len(inventory)}")
```

### Example: Enemy Wave System

```python
# Creating waves of enemies
wave_1 = ["goblin", "goblin", "orc"]
wave_2 = ["orc", "orc", "troll"]
wave_3 = ["dragon"]

all_waves = [wave_1, wave_2, wave_3]

# Spawning enemies from current wave
current_wave_index = 0
current_wave = all_waves[current_wave_index]

print(f"Wave {current_wave_index + 1}: {current_wave}")

# Spawn each enemy
for enemy in current_wave:
    print(f"Spawning {enemy}...")
    
# Check if wave is complete
if len(current_wave) == 0:
    current_wave_index += 1
    print("Wave complete!")
```

### Example: Managing Active Bullets

```python
# List to track all bullets in the game
active_bullets = []

# Bullet data: [x, y, velocity_x, velocity_y, damage]
def shoot_bullet(x, y, angle, speed, damage):
    import math
    vx = speed * math.cos(math.radians(angle))
    vy = speed * math.sin(math.radians(angle))
    bullet = [x, y, vx, vy, damage]
    active_bullets.append(bullet)

# Shoot some bullets
shoot_bullet(100, 200, 45, 10, 25)
shoot_bullet(100, 200, 90, 15, 30)

# Update all bullets
def update_bullets():
    for bullet in active_bullets[:]:  # Use slice to avoid modification issues
        bullet[0] += bullet[2]  # Update x
        bullet[1] += bullet[3]  # Update y
        
        # Remove if out of bounds
        if bullet[0] < 0 or bullet[0] > 800 or bullet[1] < 0 or bullet[1] > 600:
            active_bullets.remove(bullet)

update_bullets()
print(f"Active bullets: {len(active_bullets)}")
```

### List Comprehensions for Games

```python
# Generate starting health for 5 enemies
enemy_health = [100 for _ in range(5)]

# Create coordinates for a grid
grid_positions = [(x, y) for x in range(10) for y in range(10)]

# Filter alive enemies
enemies = [{"name": "goblin", "health": 50}, 
           {"name": "orc", "health": 0}, 
           {"name": "troll", "health": 200}]
alive_enemies = [e for e in enemies if e["health"] > 0]
print(f"Alive enemies: {alive_enemies}")

# Double all damage values
base_damage = [10, 15, 20, 25]
critical_damage = [d * 2 for d in base_damage]
print(f"Critical damage: {critical_damage}")
```

---

## Dictionaries
**What they are:** Unordered collections of key-value pairs. Fast lookup by key.

**When to use in games:** Player stats, item properties, game settings, entity attributes, save data

### Basic Dictionary Operations

```python
# Player stats
player = {
    "name": "Hero",
    "level": 5,
    "health": 100,
    "max_health": 100,
    "mana": 50,
    "max_mana": 50,
    "position": (100, 200),
    "inventory": ["sword", "potion"]
}

# Accessing values
print(f"Player: {player['name']}")
print(f"Health: {player['health']}/{player['max_health']}")

# Safe access with get (returns None if key doesn't exist)
xp = player.get("experience", 0)  # Returns 0 if "experience" key doesn't exist

# Adding/updating values
player["experience"] = 1250
player["level"] = 6

# Removing values
del player["position"]  # Remove key-value pair
mana = player.pop("mana")  # Remove and return value

# Checking if key exists
if "health" in player:
    print("Player has health stat")

# Iterating through dictionary
for key, value in player.items():
    print(f"{key}: {value}")

# Get all keys or values
stats = list(player.keys())
values = list(player.values())
```

### Example: Item Database

```python
# Database of items with properties
items = {
    "sword": {
        "type": "weapon",
        "damage": 25,
        "durability": 100,
        "rarity": "common",
        "value": 50
    },
    "fire_staff": {
        "type": "weapon",
        "damage": 40,
        "element": "fire",
        "mana_cost": 10,
        "rarity": "rare",
        "value": 200
    },
    "health_potion": {
        "type": "consumable",
        "healing": 50,
        "rarity": "common",
        "value": 25
    },
    "dragon_armor": {
        "type": "armor",
        "defense": 75,
        "fire_resistance": 50,
        "rarity": "legendary",
        "value": 1000
    }
}

# Using an item
def use_item(item_name, player):
    if item_name not in items:
        print(f"{item_name} doesn't exist!")
        return
    
    item = items[item_name]
    
    if item["type"] == "consumable":
        heal_amount = item["healing"]
        player["health"] = min(player["health"] + heal_amount, player["max_health"])
        print(f"Healed {heal_amount} HP!")
    elif item["type"] == "weapon":
        print(f"Equipped {item_name} - Damage: {item['damage']}")

# Get all weapons
weapons = {name: props for name, props in items.items() if props["type"] == "weapon"}
print(f"Available weapons: {list(weapons.keys())}")

# Sort items by value
sorted_items = sorted(items.items(), key=lambda x: x[1]["value"], reverse=True)
print(f"Most valuable item: {sorted_items[0][0]}")
```

### Example: Game State Management

```python
# Complete game state
game_state = {
    "current_level": 1,
    "score": 15000,
    "time_elapsed": 324.5,
    "difficulty": "hard",
    "player": {
        "x": 400,
        "y": 300,
        "health": 85,
        "ammo": 50
    },
    "enemies": [
        {"type": "zombie", "x": 100, "y": 200, "health": 30},
        {"type": "skeleton", "x": 700, "y": 400, "health": 20}
    ],
    "flags": {
        "boss_defeated": False,
        "secret_found": True,
        "game_over": False
    }
}

# Update game state
def take_damage(amount):
    game_state["player"]["health"] -= amount
    if game_state["player"]["health"] <= 0:
        game_state["flags"]["game_over"] = True
        print("Game Over!")

# Access nested data
player_pos = (game_state["player"]["x"], game_state["player"]["y"])
print(f"Player at {player_pos}")

# Save game state (simplified)
import json
save_data = json.dumps(game_state, indent=2)
print("Game saved!")
```

---

## Tuples
**What they are:** Ordered, immutable (unchangeable) collections. Faster than lists.

**When to use in games:** Coordinates, RGB colors, constant data, function returns with multiple values

### Basic Tuple Operations

```python
# Creating tuples
position = (100, 200)
color = (255, 0, 0)  # RGB for red
player_data = ("Hero", 10, 100, 50)

# Accessing elements (same as lists)
x = position[0]
y = position[1]

# Unpacking tuples
x, y = position
name, level, health, mana = player_data

print(f"Position: x={x}, y={y}")

# Tuples are immutable - this would cause an error:
# position[0] = 150  # TypeError!

# But you can create a new tuple
new_position = (position[0] + 10, position[1] + 5)
```

### Example: Position and Movement

```python
# Entity positions as tuples
player_pos = (400, 300)
enemy_positions = [
    (100, 150),
    (200, 250),
    (150, 100)
]

# Calculate distance between two points
def distance(pos1, pos2):
    import math
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]
    return math.sqrt(dx**2 + dy**2)

# Find closest enemy
closest_enemy = min(enemy_positions, key=lambda pos: distance(player_pos, pos))
print(f"Closest enemy at: {closest_enemy}")

# Move in a direction (returns new position)
def move(position, direction, speed):
    """
    direction: tuple (dx, dy) representing direction vector
    Returns new position tuple
    """
    new_x = position[0] + direction[0] * speed
    new_y = position[1] + direction[1] * speed
    return (new_x, new_y)

# Movement directions as tuples
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

player_pos = move(player_pos, UP, 5)
print(f"New position: {player_pos}")
```

### Example: Colors and Graphics

```python
# Define colors as tuples (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Team colors
TEAM_COLORS = {
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "green": (0, 255, 0)
}

# Return multiple values using tuples
def get_screen_bounds():
    width = 800
    height = 600
    return (width, height)

# Unpack the return value
screen_width, screen_height = get_screen_bounds()

# Sprite rectangle: (x, y, width, height)
player_rect = (100, 200, 32, 48)
enemy_rect = (300, 250, 32, 32)

def rects_collide(rect1, rect2):
    x1, y1, w1, h1 = rect1
    x2, y2, w2, h2 = rect2
    
    return (x1 < x2 + w2 and
            x1 + w1 > x2 and
            y1 < y2 + h2 and
            y1 + h1 > y2)

if rects_collide(player_rect, enemy_rect):
    print("Collision detected!")
```

---

## Sets
**What they are:** Unordered collections of unique elements. Very fast membership testing.

**When to use in games:** Tags, unique item collections, active effects, completed achievements

### Basic Set Operations

```python
# Creating sets
player_abilities = {"jump", "dash", "attack", "defend"}
unlocked_levels = {1, 2, 3, 5, 8}

# Adding elements
player_abilities.add("double_jump")
player_abilities.add("jump")  # Duplicates are ignored

# Removing elements
player_abilities.remove("defend")  # Raises error if not found
player_abilities.discard("fly")  # Doesn't raise error if not found

# Checking membership (very fast!)
if "dash" in player_abilities:
    print("Player can dash!")

# Set operations
enemy_abilities = {"attack", "defend", "fly", "teleport"}

# Union - all abilities
all_abilities = player_abilities | enemy_abilities
# or: all_abilities = player_abilities.union(enemy_abilities)

# Intersection - shared abilities
shared = player_abilities & enemy_abilities
# or: shared = player_abilities.intersection(enemy_abilities)

# Difference - abilities player has but enemy doesn't
unique_to_player = player_abilities - enemy_abilities

print(f"Player unique abilities: {unique_to_player}")
```

### Example: Achievement System

```python
# All possible achievements
all_achievements = {
    "first_kill",
    "complete_tutorial",
    "reach_level_10",
    "defeat_boss",
    "collect_all_items",
    "speedrun",
    "pacifist",
    "no_damage"
}

# Player's unlocked achievements
player_achievements = {
    "first_kill",
    "complete_tutorial",
    "reach_level_10"
}

# Check if achievement unlocked
if "defeat_boss" in player_achievements:
    print("Boss defeated!")
else:
    print("Boss not yet defeated")

# Get remaining achievements
remaining = all_achievements - player_achievements
print(f"Achievements to unlock: {remaining}")

# Calculate completion percentage
completion = len(player_achievements) / len(all_achievements) * 100
print(f"Achievement completion: {completion:.1f}%")

# Unlock achievement
def unlock_achievement(name):
    if name in all_achievements and name not in player_achievements:
        player_achievements.add(name)
        print(f"🏆 Achievement unlocked: {name}!")
        return True
    return False

unlock_achievement("defeat_boss")
```

### Example: Entity Tag System

```python
# Tag system for entity behaviors and interactions
player_tags = {"player", "mortal", "physical"}
zombie_tags = {"enemy", "undead", "hostile", "physical"}
ghost_tags = {"enemy", "undead", "hostile", "ethereal"}
wall_tags = {"obstacle", "physical"}
door_tags = {"obstacle", "physical", "openable"}

# Check if entity can be damaged by physical attacks
def can_be_hit_by_physical(entity_tags):
    return "physical" in entity_tags

print(f"Can hit zombie: {can_be_hit_by_physical(zombie_tags)}")
print(f"Can hit ghost: {can_be_hit_by_physical(ghost_tags)}")

# Check if two entities can interact
def can_interact(tags1, tags2):
    # Both have "physical" tag
    return "physical" in tags1 and "physical" in tags2

print(f"Player can collide with wall: {can_interact(player_tags, wall_tags)}")

# Get all enemies
all_entities = [
    ("player", player_tags),
    ("zombie", zombie_tags),
    ("ghost", ghost_tags),
    ("wall", wall_tags)
]

enemies = [name for name, tags in all_entities if "enemy" in tags]
print(f"Enemies: {enemies}")

# Find entities with multiple tags
def has_all_tags(entity_tags, required_tags):
    return required_tags.issubset(entity_tags)

required = {"enemy", "undead"}
undead_enemies = [name for name, tags in all_entities if has_all_tags(tags, required)]
print(f"Undead enemies: {undead_enemies}")
```

### Example: Active Status Effects

```python
# Status effects currently on player
active_effects = {"speed_boost", "shield"}

# Apply new effect
def apply_effect(effect_name):
    active_effects.add(effect_name)
    print(f"Applied {effect_name}")

# Remove effect when it expires
def remove_effect(effect_name):
    active_effects.discard(effect_name)
    print(f"Removed {effect_name}")

# Check for specific effect
def has_effect(effect_name):
    return effect_name in active_effects

# Calculate player speed based on effects
def get_player_speed():
    base_speed = 5
    
    if "speed_boost" in active_effects:
        base_speed *= 1.5
    if "slow" in active_effects:
        base_speed *= 0.5
    if "frozen" in active_effects:
        base_speed = 0
    
    return base_speed

print(f"Current speed: {get_player_speed()}")

apply_effect("poison")
print(f"Active effects: {active_effects}")
```

---

## Nested Structures
**What they are:** Data structures inside other data structures.

**When to use in games:** Complex game entities, skill trees, inventory with item details, game maps

### Example: Complete Enemy System

```python
# Enemies with full data
enemies = [
    {
        "name": "Goblin Scout",
        "type": "goblin",
        "level": 3,
        "stats": {
            "health": 50,
            "max_health": 50,
            "attack": 10,
            "defense": 5,
            "speed": 8
        },
        "position": (100, 150),
        "inventory": ["rusty dagger", "small potion"],
        "abilities": {"quick_attack", "dodge"},
        "status_effects": set(),
        "ai_state": "patrol",
        "loot_table": [
            ("gold", 0.8, 10),  # (item, drop_chance, amount)
            ("health_potion", 0.3, 1),
            ("rusty_dagger", 0.5, 1)
        ]
    },
    {
        "name": "Fire Mage",
        "type": "mage",
        "level": 7,
        "stats": {
            "health": 80,
            "max_health": 80,
            "attack": 35,
            "defense": 10,
            "speed": 6,
            "mana": 100,
            "max_mana": 100
        },
        "position": (300, 200),
        "inventory": ["fire_staff", "mana_potion", "spell_book"],
        "abilities": {"fireball", "flame_shield", "teleport"},
        "status_effects": {"flame_aura"},
        "ai_state": "aggressive"
    }
]

# Access nested data
first_enemy = enemies[0]
print(f"Enemy: {first_enemy['name']}")
print(f"Health: {first_enemy['stats']['health']}/{first_enemy['stats']['max_health']}")
print(f"Position: {first_enemy['position']}")
print(f"Abilities: {first_enemy['abilities']}")

# Modify nested data
enemies[0]["stats"]["health"] -= 20
enemies[0]["status_effects"].add("poisoned")

# Find all enemies at low health
def get_low_health_enemies(enemy_list, threshold=0.3):
    low_health = []
    for enemy in enemy_list:
        health_percent = enemy["stats"]["health"] / enemy["stats"]["max_health"]
        if health_percent < threshold:
            low_health.append(enemy["name"])
    return low_health

# Find enemies with specific ability
def has_ability(enemy, ability_name):
    return ability_name in enemy.get("abilities", set())

mages = [e["name"] for e in enemies if has_ability(e, "fireball")]
print(f"Enemies with fireball: {mages}")
```

### Example: Inventory System with Item Instances

```python
# Player inventory with item instances
inventory = [
    {
        "id": "sword_001",
        "name": "Iron Sword",
        "type": "weapon",
        "durability": 75,
        "max_durability": 100,
        "stats": {"damage": 25, "attack_speed": 1.2},
        "enchantments": ["sharpness"],
        "equipped": True
    },
    {
        "id": "potion_001",
        "name": "Health Potion",
        "type": "consumable",
        "quantity": 5,
        "effects": {"heal": 50}
    },
    {
        "id": "armor_001",
        "name": "Leather Armor",
        "type": "armor",
        "slot": "chest",
        "durability": 40,
        "max_durability": 80,
        "stats": {"defense": 15, "weight": 5},
        "enchantments": []
    }
]

# Get equipped weapon
def get_equipped_weapon(inv):
    for item in inv:
        if item["type"] == "weapon" and item.get("equipped", False):
            return item
    return None

weapon = get_equipped_weapon(inventory)
if weapon:
    print(f"Equipped: {weapon['name']} (Durability: {weapon['durability']}/{weapon['max_durability']})")

# Use consumable
def use_consumable(inv, item_id, player):
    for item in inv:
        if item["id"] == item_id and item["type"] == "consumable":
            # Apply effects
            for effect, value in item["effects"].items():
                if effect == "heal":
                    player["health"] = min(player["health"] + value, player["max_health"])
                    print(f"Healed {value} HP!")
            
            # Reduce quantity or remove
            item["quantity"] -= 1
            if item["quantity"] <= 0:
                inv.remove(item)
            return True
    return False

# Count items by type
def count_by_type(inv):
    counts = {}
    for item in inv:
        item_type = item["type"]
        counts[item_type] = counts.get(item_type, 0) + 1
    return counts

print(f"Inventory breakdown: {count_by_type(inventory)}")
```

### Example: Skill Tree

```python
# Complex skill tree structure
skill_tree = {
    "warrior": {
        "name": "Warrior Path",
        "base_stats": {"strength": 5, "defense": 5},
        "skills": {
            "power_strike": {
                "name": "Power Strike",
                "level": 3,
                "max_level": 5,
                "unlocked": True,
                "requirements": {},
                "effects": {"damage_bonus": 30},
                "mana_cost": 10
            },
            "iron_skin": {
                "name": "Iron Skin",
                "level": 2,
                "max_level": 5,
                "unlocked": True,
                "requirements": {},
                "effects": {"defense_bonus": 20}
            },
            "whirlwind": {
                "name": "Whirlwind",
                "level": 0,
                "max_level": 3,
                "unlocked": False,
                "requirements": {"power_strike": 3, "level": 10},
                "effects": {"area_damage": 50, "radius": 5},
                "mana_cost": 30
            }
        }
    },
    "mage": {
        "name": "Mage Path",
        "base_stats": {"intelligence": 5, "mana": 50},
        "skills": {
            "fireball": {
                "name": "Fireball",
                "level": 5,
                "max_level": 5,
                "unlocked": True,
                "requirements": {},
                "effects": {"damage": 40, "burn_duration": 3},
                "mana_cost": 20
            },
            "meteor": {
                "name": "Meteor",
                "level": 0,
                "max_level": 3,
                "unlocked": False,
                "requirements": {"fireball": 5, "level": 20},
                "effects": {"damage": 200, "area": 10},
                "mana_cost": 100
            }
        }
    }
}

# Check if skill can be unlocked
def can_unlock_skill(player, class_name, skill_name):
    skill = skill_tree[class_name]["skills"][skill_name]
    
    if skill["unlocked"]:
        return False, "Already unlocked"
    
    requirements = skill["requirements"]
    
    # Check level requirement
    if "level" in requirements and player["level"] < requirements["level"]:
        return False, f"Requires level {requirements['level']}"
    
    # Check other skill requirements
    for req_skill, req_level in requirements.items():
        if req_skill == "level":
            continue
        other_skill = skill_tree[class_name]["skills"][req_skill]
        if other_skill["level"] < req_level:
            return False, f"Requires {req_skill} level {req_level}"
    
    return True, "Can unlock!"

# Test unlock
player = {"level": 12, "class": "warrior", "skill_points": 5}
can_unlock, message = can_unlock_skill(player, "warrior", "whirlwind")
print(f"Can unlock Whirlwind: {message}")

# Get all unlocked skills for a class
def get_unlocked_skills(class_name):
    return [skill_name for skill_name, skill_data in skill_tree[class_name]["skills"].items() 
            if skill_data["unlocked"]]

print(f"Unlocked warrior skills: {get_unlocked_skills('warrior')}")
```

---

## Queues and Stacks
**What they are:** Specialized data structures for ordered processing.

**When to use in games:** Action queues, command history, pathfinding, dialogue systems

### Using Collections.deque for Queues

```python
from collections import deque

# Queue (FIFO - First In, First Out)
# Used for: Turn order, action sequences, enemy spawn queue

# Enemy spawn queue
spawn_queue = deque(["goblin", "orc", "goblin", "troll"])

# Add to queue
spawn_queue.append("dragon")  # Add to end

# Process queue
while spawn_queue:
    enemy = spawn_queue.popleft()  # Remove from front
    print(f"Spawning {enemy}...")

# Action queue for turn-based game
action_queue = deque()

def queue_action(character, action, target):
    action_queue.append({
        "character": character,
        "action": action,
        "target": target
    })

queue_action("Hero", "attack", "Goblin")
queue_action("Goblin", "defend", "self")
queue_action("Mage", "cast_fireball", "Goblin")

# Process actions in order
while action_queue:
    action = action_queue.popleft()
    print(f"{action['character']} performs {action['action']} on {action['target']}")
```

### Stack Example (Undo System)

```python
# Stack (LIFO - Last In, First Out)
# Used for: Undo/redo, dialogue history, game states

# Dialogue history stack
dialogue_history = []

def show_dialogue(text, choices):
    # Save current state before showing new dialogue
    state = {
        "text": text,
        "choices": choices,
        "timestamp": "current"
    }
    dialogue_history.append(state)
    print(f"\n{text}")
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")

def go_back():
    if len(dialogue_history) > 1:
        dialogue_history.pop()  # Remove current
        previous = dialogue_history[-1]  # Get previous
        print(f"\nGoing back to: {previous['text']}")
        return previous
    else:
        print("Can't go back further")
        return None

# Dialogue flow
show_dialogue("You meet a stranger.", ["Greet", "Ignore", "Attack"])
show_dialogue("The stranger smiles.", ["Ask about quest", "Leave"])
show_dialogue("'I need your help,' they say.", ["Accept quest", "Decline"])

# Player wants to go back
go_back()
go_back()
```

### Example: Command History (for replay/demo)

```python
from collections import deque

# Command pattern for replay
command_history = []

class Command:
    def __init__(self, action, data):
        self.action = action
        self.data = data
        self.timestamp = 0  # Frame number

def record_command(action, data):
    cmd = Command(action, data)